# Claim Ledger

This ledger maps public-facing claims to the raw artifacts that support them. It exists to prevent narrative drift: if a number or mechanistic statement changes, the evidence verifier must change or fail.

**Boundary:** these are deterministic local software/causal-semantics claims. They are **not** frontier-model performance results.

| ID | Claim | Scope | Evidence |
|---|---|---|---|
| TS-C001 | 2/2 no-intervention control replays are replay-faithful in the deterministic local demo. | software semantics only | `runs/demo_5min.json` |
| TS-C002 | Exactly 3 intervention branches change the failed outcome to success in the deterministic local demo. | software semantics only | `runs/demo_5min.json` |
| TS-C003 | At intervention step 0, action_patch and suffix_replan recover the task while state_patch does not. | single deterministic failure case | `runs/demo_5min.json`<br>`artifacts/ablations/step0_action_patch.json`<br>`artifacts/ablations/step0_state_patch.json`<br>`artifacts/ablations/step0_suffix_replan.json` |
| TS-C004 | At intervention step 1, state_patch recovers the task while action_patch and suffix_replan do not. | single deterministic failure case | `runs/demo_5min.json`<br>`artifacts/ablations/step1_action_patch.json`<br>`artifacts/ablations/step1_state_patch.json`<br>`artifacts/ablations/step1_suffix_replan.json` |
| TS-C005 | The Evidence Layer contains 9 documented investigations: 8 local causal investigations and 1 software-validation run. | release process evidence | `artifacts/experiment_logs/experiment_journal.jsonl` |
| TS-C006 | The local intervention surface contains 3 failed repair attempts that changed the mechanistic interpretation. | single deterministic failure case | `runs/demo_5min.json`<br>`docs/evidence/FAILED_EXPERIMENTS.md` |
| TS-C007 | The Decision Log records 8 major design decisions. | project process evidence | `docs/evidence/DECISION_LOG.md` |
| TS-C008 | The Unexpected Findings log records 4 evidence-grounded findings. | project process evidence | `docs/evidence/UNEXPECTED_FINDINGS.md` |
| TS-C009 | No frontier-model comparison is populated in the released Evidence Layer. | claim discipline | `artifacts/eval_runs/EXTERNAL_RESULTS_PENDING.md`<br>`docs/PUBLIC_CLAIMS.md` |

## Reproduce the ledger

```bash
python scripts/verify_evidence_layer.py
```

A non-zero exit means at least one released claim no longer matches its raw evidence.
