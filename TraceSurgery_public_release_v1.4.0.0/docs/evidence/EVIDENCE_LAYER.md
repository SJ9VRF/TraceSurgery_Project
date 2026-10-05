# Evidence Layer

The polished homepage explains the project. This layer shows the work underneath it: hypotheses, failed repairs, raw branches, design changes, and the boundary between executed evidence and planned external study.

## At a glance - verified in this release

- **9 documented investigations**: 8 checkpoint/intervention investigations on the deterministic failure case + 1 500-task software-validation run.
- **3 failed repair attempts** that changed the mechanistic interpretation: checkpoint-0 state patch, checkpoint-1 action patch, checkpoint-1 suffix replan.
- **8 major decisions** recorded with alternatives, evidence, trade-offs, and outcomes.
- **4 unexpected findings** grounded in executed local evidence.
- **8 raw counterfactual branch records** plus a structured failure case and machine-readable eval tables.
- **0 fabricated frontier-model result rows.** External scientific tables remain pending until evidence passes the scientific gate.

## Read in this order

1. [`artifacts/experiment_logs/EXPERIMENT_JOURNAL.md`](../../artifacts/experiment_logs/EXPERIMENT_JOURNAL.md)
2. [`FAILED_EXPERIMENTS.md`](FAILED_EXPERIMENTS.md)
3. [`DECISION_LOG.md`](DECISION_LOG.md)
4. [`EVAL_TABLES.md`](EVAL_TABLES.md)
5. [`UNEXPECTED_FINDINGS.md`](UNEXPECTED_FINDINGS.md)
6. [`artifacts/qualitative_cases/CASE-001.md`](../../artifacts/qualitative_cases/CASE-001.md)
7. [`artifacts/README.md`](../../artifacts/README.md)

## Scientific story, without smoothing it into a perfect arc

The actual local sequence is:

**reproduce failure -> establish replay controls -> action repair works early -> state repair unexpectedly fails early -> suffix repair works early -> move past corruption -> action/suffix repair fail -> state repair works -> reinterpret the failure as a time-varying recoverability mechanism**.

That sequence is the reason TraceSurgery reports a checkpoint-indexed intervention surface rather than a single root-cause label.

## Git-history boundary

No historical commit sequence is fabricated. See `artifacts/git_history/HISTORY_POLICY.md`. New Evidence Layer work is preserved in a real Git bundle from the point history became available.
