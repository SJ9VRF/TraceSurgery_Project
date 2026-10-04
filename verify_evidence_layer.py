#!/usr/bin/env python3
"""Recompute TraceSurgery Evidence Layer claims from raw artifacts.

This verifier checks local deterministic evidence only. It must not be used to
promote local software-validation results into frontier-model performance claims.
"""
from __future__ import annotations
import argparse, csv, json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def load_json(path: Path):
    return json.loads(path.read_text())

def compute(root: Path) -> dict:
    demo = load_json(root / "runs/demo_5min.json")
    branches = demo["branches"]
    controls = [b for b in branches if b["kind"] == "no_intervention"]
    interventions = [b for b in branches if b["kind"] != "no_intervention"]
    by_step = {}
    for b in branches:
        by_step.setdefault(int(b["intervention_step"]), {})[b["kind"]] = bool(b["success"])
    journal = [json.loads(x) for x in (root / "artifacts/experiment_logs/experiment_journal.jsonl").read_text().splitlines() if x.strip()]
    decisions = re.findall(r"^## D-\d+", (root / "docs/evidence/DECISION_LOG.md").read_text(), flags=re.M)
    findings = re.findall(r"^## U-\d+", (root / "docs/evidence/UNEXPECTED_FINDINGS.md").read_text(), flags=re.M)
    external = (root / "artifacts/eval_runs/EXTERNAL_RESULTS_PENDING.md").read_text().lower()
    return {
        "controls": len(controls),
        "faithful_controls": sum(b.get("replay_matches_source") is True for b in controls),
        "effective_interventions": sum(bool(b["success"]) for b in interventions),
        "failed_interventions": sum(not bool(b["success"]) for b in interventions),
        "step0": by_step.get(0, {}),
        "step1": by_step.get(1, {}),
        "journal_rows": len(journal),
        "journal_local_causal": sum(x.get("kind") == "local_causal" for x in journal),
        "journal_software_validation": sum(x.get("kind") == "software_validation" for x in journal),
        "decision_count": len(decisions),
        "unexpected_finding_count": len(findings),
        "external_pending": "pending" in external and "no frontier-model comparison is populated" in external,
    }

def verify(root: Path) -> dict:
    m = compute(root)
    expected0 = {"no_intervention": False, "action_patch": True, "state_patch": False, "suffix_replan": True}
    expected1 = {"no_intervention": False, "action_patch": False, "state_patch": True, "suffix_replan": False}
    checks = {
        "TS-C001": m["controls"] == 2 and m["faithful_controls"] == 2,
        "TS-C002": m["effective_interventions"] == 3,
        "TS-C003": m["step0"] == expected0,
        "TS-C004": m["step1"] == expected1,
        "TS-C005": m["journal_rows"] == 9 and m["journal_local_causal"] == 8 and m["journal_software_validation"] == 1,
        "TS-C006": m["failed_interventions"] == 3,
        "TS-C007": m["decision_count"] == 8,
        "TS-C008": m["unexpected_finding_count"] == 4,
        "TS-C009": m["external_pending"] is True,
    }
    # Published eval table must be derivable from raw branches.
    with (root / "artifacts/eval_runs/local_demo_eval.csv").open() as f:
        rows = {r["variant"]: r for r in csv.DictReader(f)}
    table_ok = True
    for kind in ["no_intervention", "action_patch", "state_patch", "suffix_replan"]:
        raw = [b for b in load_json(root / "runs/demo_5min.json")["branches"] if b["kind"] == kind]
        table_ok &= int(rows[kind]["checkpoints"]) == len(raw)
        table_ok &= int(rows[kind]["recoveries"]) == sum(bool(b["success"]) for b in raw)
    checks["published_eval_table_matches_raw"] = bool(table_ok)
    return {"ok": all(checks.values()), "checks": checks, "computed": m}

def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--root", default=str(ROOT))
    p.add_argument("--output")
    args = p.parse_args()
    report = verify(Path(args.root).resolve())
    text = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if args.output:
        Path(args.output).write_text(text)
    print(text, end="")
    return 0 if report["ok"] else 2

if __name__ == "__main__":
    raise SystemExit(main())
