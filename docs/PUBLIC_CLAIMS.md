# Public Claims Policy

TraceSurgery is designed to make causal claims falsifiable. Public-facing claims must therefore be stricter than internal hypotheses.

## Claims currently supported by executable local evidence

- The framework can checkpoint a deterministic stateful environment, replay the original suffix, apply typed interventions, and re-grade the resulting branch.
- Intervention effects are marked causally usable only when a no-intervention control replay reproduces the source terminal state at the same checkpoint.
- The local validation suite contains 500 software-validation tasks and can be oracle-validated end to end.
- The framework records intervention provenance, branch hashes, state transitions, safety events, and task-level statistics.
- The external-study layer can atomically claim/resume planned runs, verify manifest hashes from disk, reject ineligible evidence, and fail closed before producing paper-ready summaries.

## Claims that are hypotheses, not results

- TraceSurgery improves diagnosis quality on frontier computer-use agents.
- Frontier models with similar task-success rates have measurably different recovery geometry.
- Any model, debugger, or recovery policy is state of the art under TraceSurgery.
- Results on the local deterministic validation suite transfer to OSWorld, BrowserGym, or production computer-use environments.

## Forbidden wording before external experiments

Do not write: “SOTA”, “outperforms”, “improves X%”, “best benchmark”, “proves root cause”, or “500 real-world tasks” unless the corresponding external experiment and audit evidence exists.

Preferred wording: “implements”, “tests locally”, “proposes”, “measures under replay-faithful checkpoints”, “external evaluation pending”.
