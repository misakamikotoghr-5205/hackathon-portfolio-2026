#!/usr/bin/env python3
"""Build honest offline submission materials; no account, network or model calls.

Run from the portfolio workspace. Requires Python 3.11+ and Pillow for the PNG.
Only this draft directory receives output. The actual CLI uses a disposable DB.
"""
from __future__ import annotations

from datetime import datetime, timezone
import hashlib
import html
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile

from PIL import Image, ImageDraw, ImageFont


HERE = Path(__file__).resolve().parent
WORKSPACE = HERE.parents[3]
PROJECT = WORKSPACE / "projects" / "pantry-relay"
AS_OF = "2026-11-04T12:00:00+08:00"
KEY = "submission-materials-fictional-replay"


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def collect() -> dict:
    records = []
    with tempfile.TemporaryDirectory(prefix="pantry-submission-materials-") as tmp:
        database = Path(tmp) / "fictional.sqlite3"

        def cli(*args):
            proc = subprocess.run(
                [sys.executable, "-m", "pantry_relay", "--db", str(database), *args],
                cwd=PROJECT, text=True, capture_output=True, check=True,
                env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1"},
            )
            result = json.loads(proc.stdout)
            records.append({"command": ["python3", "-m", "pantry_relay", "--db", "<temporary-demo-db>", *args], "exit_code": proc.returncode, "output": result})
            return result

        cli("init", "examples/pantry.json")
        plan = cli("plan", "--as-of", AS_OF)
        args = ("consume", "--recipe", "plain_oats", "--key", KEY,
                "--expected-revision", "0", "--as-of", AS_OF)
        first = cli(*args)
        replay = cli(*args)
        inventory = cli("inventory")
        oats = next(lot for lot in inventory["project"]["lots"] if lot["id"] == "oats")
        assert first["changes"][0]["before"] == "250"
        assert first["changes"][0]["used"] == "50"
        assert first["changes"][0]["remaining"] == "200"
        assert replay["receipt_id"] == first["receipt_id"] and replay["replayed"] is True
        assert inventory["revision"] == 1 and oats["quantity"] == "200"
        assert first["safety_guarantee"] is False
        held = [lot for lot in plan["lot_review"] if lot["status"] == "hold"]
        assert {lot["lot_id"] for lot in held} == {"milk_open", "conflict_sauce", "packed_only", "peanuts"}

    model_path = PROJECT / "docs" / "evidence" / "local-model-20261106.json"
    model = json.loads(model_path.read_text())
    assert model["metadata"]["real_inference"] is True
    assert model["metadata"]["recipe_ids"] == ["plain_oats", "tomato_eggs"]
    assert model["second_trial"]["actual_output"]["recipe_ids"] == ["plain_oats"]
    return {
        "schema_version": 1,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "scenario_as_of": AS_OF,
        "scenario": "Original fictional package labels and recipes; historical CLI replay, not current household inventory.",
        "new_model_or_platform_calls": False,
        "alipay_deployed": False,
        "artifact_kind": "Offline explanatory submission material, not an interactive agent or platform screenshot.",
        "input_sha256": digest(PROJECT / "examples" / "pantry.json"),
        "source_sha256": {str(p.relative_to(PROJECT)): digest(p) for p in sorted((PROJECT / "pantry_relay").glob("*.py"))},
        "prior_model_evidence": {
            "repository_path": "docs/evidence/local-model-20261106.json",
            "sha256": digest(model_path),
            "first_prompt": model["metadata"]["prompt"],
            "first_recipe_ids": model["metadata"]["recipe_ids"],
            "second_prompt": model["second_trial"]["prompt"],
            "second_recipe_ids": model["second_trial"]["actual_output"]["recipe_ids"],
            "limitation": "Two prior real local requests; first preference partially missed. Not a benchmark or Alipay call.",
        },
        "checks": {"same_receipt_on_retry": True, "single_deduction_only": True, "held_lot_ids": [lot["lot_id"] for lot in held], "inventory_revision": inventory["revision"], "oats_remaining_g": oats["quantity"]},
        "commands": records,
    }


def cover(data: dict) -> None:
    image = Image.new("RGB", (1200, 675), "#f1f5f0")
    draw = ImageDraw.Draw(image)
    font = "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc"
    if not Path(font).is_file():
        raise SystemExit("PNG requires the installed Noto Sans CJK font; HTML/JSON are already generated.")
    def text(at, value, size=24, fill="#173d35"):
        draw.text(at, value, font=ImageFont.truetype(font, size), fill=fill)
    draw.rounded_rectangle((44, 38, 1156, 637), radius=28, fill="#ffffff")
    text((78, 64), "PANTRY RELAY  /  本地原型说明", 20)
    text((76, 105), "余量接力", 66)
    text((80, 202), "有来源的先用计划 · 不能越权的模型 · 不重复扣减的回执", 27)
    labels = [(78, "01  先核来源", "缺开封说明、日期冲突", "保留待核查"),
              (435, "02  人工复核", "模型只选合格菜谱ID", "不判断食品安全"),
              (792, "03  原子扣减", "燕麦 250g → 200g", "同键重试仍为200g")]
    for x, title, line1, line2 in labels:
        draw.rounded_rectangle((x, 293, x + 329, 464), radius=16, fill="#e8f2e9")
        text((x + 19, 308), title, 29)
        text((x + 19, 366), line1, 22)
        text((x + 19, 403), line2, 22)
    text((80, 500), "CLI已实际回放虚构的2026-11-04场景；不是当前家庭库存。", 23)
    text((80, 542), "尚未部署支付宝 / 阿宝；此图为原创说明封面，非平台截图。", 23)
    text((80, 586), "标签门禁不证明食物安全。真实模型小例曾有偏好误选，仍需人工复核。", 20, "#566760")
    target = HERE / "cover-zh.png"
    image.save(target, optimize=True)
    assert image.size == (1200, 675) and target.stat().st_size < 5 * 1024 * 1024


def page(data: dict) -> None:
    evidence = data["prior_model_evidence"]
    checks = data["checks"]
    plan = data["commands"][1]["output"]
    held = [lot for lot in plan["lot_review"] if lot["status"] == "hold"]
    names = {"milk_open": "牛奶：缺开封后说明", "conflict_sauce": "酱料：标签日期冲突", "packed_only": "豆腐：只有包装日期", "peanuts": "花生：用户标签排除"}
    rows = "".join(f"<tr><td>{html.escape(names[lot['lot_id']])}</td><td>{html.escape(', '.join(reason['code'] for reason in lot['reasons']))}</td><td>保持拦截</td></tr>" for lot in held)
    details = "".join(f"<details><summary>实际CLI调用 {i+1}：{html.escape(' '.join(item['command'][5:]))}</summary><pre>{html.escape(json.dumps(item, ensure_ascii=False, indent=2))}</pre></details>" for i, item in enumerate(data["commands"]))
    body = f"""<!doctype html><html lang="zh-CN"><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><meta http-equiv="Content-Security-Policy" content="default-src 'none'; style-src 'unsafe-inline'; img-src 'self' data:; base-uri 'none'; form-action 'none'"><title>余量接力｜离线证据说明</title>
<style>body{{font:17px/1.7 system-ui,sans-serif;color:#173d35;background:#f1f5f0;margin:0}}main{{max-width:1060px;margin:auto;padding:36px 22px}}h1{{font-size:48px;margin:.3em 0}}h2{{margin-top:1.8em}}.tag{{display:inline-block;padding:5px 12px;background:#dbe9dc;border-radius:8px}}.notice{{padding:16px 20px;border-left:5px solid #8b5817;background:#fff6e7}}section{{background:white;padding:24px;border-radius:16px;margin:22px 0}}table{{width:100%;border-collapse:collapse}}td,th{{padding:12px;text-align:left;border-bottom:1px solid #dbe2dc}}pre{{font:13px/1.6 ui-monospace,monospace;white-space:pre-wrap;overflow-wrap:anywhere}}summary{{cursor:pointer;font-weight:600}}.stats{{display:flex;gap:20px;flex-wrap:wrap}}.stats div{{background:#e8f2e9;padding:14px 22px;border-radius:12px}}a{{color:#145f50}}@media print{{body{{background:white}}main{{padding:0}}section{{break-inside:avoid;border:1px solid #ddd}}}}</style>
<main><span class="tag">离线中文交件素材 · 非平台运行页</span><h1>余量接力</h1><p>把自行录入的标签与库存，连接成有来源的先用计划和可恢复的消费回执。</p>
<p class="notice">这是一份静态说明材料，不是可交互智能体、支付宝部署或实际录屏。底层CLI已在临时数据库真实运行；回放时刻固定为2026-11-04 12:00（北京时间），全部输入为原创虚构数据。未发起新的模型或平台请求。</p>
<section><h2>有实物，也可能暂不能分配</h2><p>四项拦截分别保留原因，不把未知状态自动转成可用。</p><table><tr><th>批次与原因</th><th>程序原因码</th><th>处理</th></tr>{rows}</table></section>
<section><h2>一次消费，重试不再扣一次</h2><div class="stats"><div>燕麦：250g → 200g</div><div>本次使用：50g</div><div>同键重试：仍200g</div><div>库存版本：{checks['inventory_revision']}</div></div><p>实际回放中两次请求返回同一个receipt_id，第二次replayed=true。旧请求参数和幂等键完整保留；这里没有使用真实家庭数据或外部支付。</p></section>
<section><h2>真实模型观测：保留误选，不只展示成功</h2><p>来自已存证的11月6日本地Ollama 0.40.15 / qwen2.5:0.5b实际请求，本页只读取记录。</p><p>第一次：“{html.escape(evidence['first_prompt'])}” → <code>{html.escape(', '.join(evidence['first_recipe_ids']))}</code>。番茄鸡蛋不符合“一种配料”的偏好，虽然结构校验通过，仍需人工复核。</p><p>第二次显式指定燕麦 → <code>{html.escape(', '.join(evidence['second_recipe_ids']))}</code>。两次均没有改变库存；两个小例不构成模型质量基准，更不构成食品安全结论。</p></section>
<section><h2>边界与真实平台缺口</h2><p>CLI和鉴权JSON API已实现；没有支付宝/阿宝接入、公开可交互部署或最终提报。当前门户URL有指定平台域名要求，Python源码ZIP不等于已通过平台构建；这份HTML只是说明附件，不能冒充合格的交互作品。</p><p>标签门禁不证明食物安全；用户标签不能检测未知过敏原。模型只能从合格菜谱ID中选择，不能修改数量、绕过库存或自动消费。</p><p>原创实现MIT；Grocy/Mealie仅为设计比较，未复制其代码。外部模型权重未打包。</p></section>
<section><h2>可复核输出</h2><p>生成时间（UTC）：{html.escape(data['generated_at'])}。输入SHA-256：<code>{data['input_sha256']}</code>。</p><p><a href="local-cli-evidence.json">完整实际输出及源码指纹JSON</a> · <a href="cover-zh.png">中文说明封面PNG</a> · <a href="form-draft.md">正式表稿与提交边界</a></p>{details}</section></main></html>"""
    (HERE / "evidence-deck.html").write_text(body, encoding="utf-8")


if __name__ == "__main__":
    data = collect()
    (HERE / "local-cli-evidence.json").write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    page(data)
    cover(data)
    print(json.dumps({"generated": ["cover-zh.png", "evidence-deck.html", "local-cli-evidence.json"], "checks": data["checks"], "new_model_or_platform_calls": False}, ensure_ascii=False))
