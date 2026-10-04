# Validity threats and claim discipline

TraceSurgery separates **software validation** from **scientific evidence**.

## What the local validation suite establishes
It tests task parsing, reset determinism, observation/ground-truth separation, action execution, grading, failure instrumentation, perturbation plumbing, serialization, and statistical code. It does **not** establish frontier-agent performance or ecological validity.

## What a paper release must establish
1. Real browser/desktop environments with state-based graders.
2. Held-out task templates and data; no test-set tuning.
3. Multiple trials per task and task-clustered confidence intervals.
4. Strong agent baselines under matched model, tool, token, and step budgets.
5. Human-calibrated failure/root-cause labels with blinded adjudication.
6. Perturbations whose severity and observability are controlled and reported.
7. Separate reporting of exogenous interventions and agent-caused failures.
8. Sensitivity analyses for max steps, retry budgets, judge model, and grader thresholds.
9. Full cost/latency accounting and provider/model version pinning.
10. Negative results and benchmark limitations.

## Claims that are prohibited before those experiments
Do not call the procedural 500-task suite a frontier benchmark; do not report model improvements from diagnostic agents; do not infer semantic causality from temporal adjacency; do not claim a failure was detected unless the agent emitted an auditable detection signal; do not equate blocked unsafe actions with agent safety.
