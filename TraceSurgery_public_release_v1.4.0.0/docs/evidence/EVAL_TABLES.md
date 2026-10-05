# Real eval tables

## Local deterministic counterfactual demo

This is an executed **mechanics demonstration**, not a stochastic model benchmark. `N=2` means two admissible checkpoints on one recorded task; confidence intervals would be misleading here, so none are reported.

| Intervention family | Checkpoints N | Recoveries | Recovery rate | Mean replayed actions | Claim scope |
|---|---:|---:|---:|---:|---|
| No intervention | 2 | 0 | 0.00 | 1.5 | replay control |
| Action patch | 2 | 1 | 0.50 | 1.5 | local deterministic demo |
| State patch | 2 | 1 | 0.50 | 1.5 | privileged local diagnostic |
| Suffix replan | 2 | 1 | 0.50 | 1.5 | privileged local diagnostic |

**Raw table:** `artifacts/eval_runs/local_demo_eval.csv`  
**Raw branch records:** `artifacts/ablations/`  
**Source:** `runs/demo_5min.json`

## Software-validation table

| Validation surface | N | Passed | Failed | Interpretation |
|---|---:|---:|---:|---|
| Bundled deterministic task suite | 500 tasks | 500 | 0 | harness/oracle regression validation only |
| Duplicate task IDs | 500 tasks | 0 duplicates | - | suite integrity check |
| Task lint | 500 tasks | 0 errors / 0 warnings | - | schema/content lint |

These rows are **not model performance**.

## External model eval table

Pending. This table will be generated only from evidence records that pass `evidence-audit`. Required reporting includes `N`, repeated-trial count, task-cluster confidence intervals, exact model revision, benchmark version, grader revision, recovery metrics, latency, and cost when available.
