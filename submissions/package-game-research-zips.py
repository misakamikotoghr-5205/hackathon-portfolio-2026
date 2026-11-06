"""Rebuild upload archives from already-built dist folders, then audit local assets."""
import hashlib
from html.parser import HTMLParser
import json
from pathlib import Path, PurePosixPath
import posixpath
import re
from urllib.parse import urlsplit
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo

WORKSPACE = Path(__file__).resolve().parents[2]
OUTPUT = Path(__file__).resolve().parent / "artifacts"
PROJECTS = {
    "lumen-shift": "lumen-shift-itch.zip",
    "parallax-postcards": "parallax-postcards-itch.zip",
    "paper-route-playtest": "paper-route-playtest-modelscope-static.zip",
}

class References(HTMLParser):
    def __init__(self):
        super().__init__()
        self.urls = []
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag in {"script", "img", "iframe", "audio", "video", "source"}:
            if attrs.get("src"): self.urls.append(attrs["src"])
        if tag == "link" and attrs.get("href"): self.urls.append(attrs["href"])


def resolve_local(file, reference, names):
    split = urlsplit(reference)
    assert not split.scheme and not split.netloc, (file, "Remote runtime resource", reference)
    assert not split.path.startswith("/"), (file, "Absolute resource path", reference)
    if split.path:
        target = posixpath.normpath(posixpath.join(posixpath.dirname(file), split.path))
        assert not target.startswith("../") and target in names, (file, "Missing packaged resource", target)


def audit(archive):
    with ZipFile(archive) as bundle:
        names = set(bundle.namelist())
        assert "index.html" in names and bundle.testzip() is None
        assert len(names) <= 1000
        assert sum(entry.file_size for entry in bundle.infolist()) < 500_000_000
        for name in names:
            path = PurePosixPath(name)
            assert not path.is_absolute() and ".." not in path.parts and len(name) <= 240
            assert not any(part in {".git", ".openai", "node_modules", "__pycache__"} for part in path.parts)
            assert not name.endswith((".env", ".sqlite3", ".pyc"))
            if name.endswith(".html"):
                parser = References(); parser.feed(bundle.read(name).decode())
                for reference in parser.urls: resolve_local(name, reference, names)
            if name.endswith((".js", ".css")):
                source = bundle.read(name).decode()
                assert not re.search(r"\bfetch\s*\(|XMLHttpRequest|WebSocket|sendBeacon", source), (name, "Networking code")
                if name.endswith(".css"):
                    for reference in re.findall(r"url\(['\"]?([^)'\"]+)", source): resolve_local(name, reference, names)
                else:
                    for reference in re.findall(r"\b(?:import|export)\s+(?:[^;]*?\sfrom\s*)?[\"']([^\"']+)[\"']", source): resolve_local(name, reference, names)
        return {"files": sorted(names), "file_count": len(names), "uncompressed_bytes": sum(i.file_size for i in bundle.infolist()), "root_index": True, "crc_passed": True, "runtime_resources_local": True}


def main():
    OUTPUT.mkdir(exist_ok=True)
    manifest = {"checked_on": "2026-11-06", "submitted": False, "browser_qa_this_pass": False, "artifacts": []}
    for project, filename in PROJECTS.items():
        dist = WORKSPACE / "projects" / project / "dist"
        assert (dist / "index.html").is_file(), f"Build {project} first"
        archive = OUTPUT / filename
        with ZipFile(archive, "w", compression=ZIP_DEFLATED) as bundle:
            for file in sorted(dist.rglob("*")):
                if not file.is_file(): continue
                info = ZipInfo(file.relative_to(dist).as_posix(), date_time=(2026, 11, 6, 0, 0, 0))
                info.compress_type = ZIP_DEFLATED; info.external_attr = 0o100644 << 16
                bundle.writestr(info, file.read_bytes())
        record = {"project": project, "path": archive.relative_to(WORKSPACE).as_posix(), "sha256": hashlib.sha256(archive.read_bytes()).hexdigest(), "zip_bytes": archive.stat().st_size, **audit(archive)}
        manifest["artifacts"].append(record)
        print(project, record["file_count"], "files", record["zip_bytes"], "bytes", record["sha256"])
    (OUTPUT / "game-research-four-manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")

if __name__ == "__main__": main()
