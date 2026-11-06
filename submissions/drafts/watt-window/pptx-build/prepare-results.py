"""Regenerate the presentation evidence from the local, fictional example models."""
from __future__ import annotations

import json
import sys
from pathlib import Path

BUILD_DIR = Path(__file__).resolve().parent
WORKSPACE = BUILD_DIR.parents[4]
PROJECT = WORKSPACE / "projects" / "watt-window"
sys.path.insert(0, str(PROJECT))
from watt_window.core import sensitivity, solve  # noqa: E402


def read_example(name: str) -> dict:
    return json.loads((PROJECT / "examples" / name).read_text())


household = read_example("household.json")
results = {
    name: solve(read_example(f"{name}.json"))
    for name in ("household", "shop", "infeasible")
}
results["household_one_node"] = solve(household, 1)
results["sensitivity"] = sensitivity(household, read_example("sensitivity.json"))
(BUILD_DIR / "model-results.json").write_text(json.dumps(results, indent=2) + "\n")
print("Regenerated model-results.json; underlying inputs are fictional, not field measurements.")
