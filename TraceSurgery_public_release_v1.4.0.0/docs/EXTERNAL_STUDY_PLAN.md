# External Frontier Study Plan

This is the work required before TraceSurgery can be presented as an empirical frontier-agent result.

## Study A — Natural failure collection
Run multiple frontier/open computer-use agents on realistic stateful browser/desktop tasks. Store full trajectories, exact model/version, action budgets, costs, seeds where available, grader version, environment image/version, and reset provenance.

Primary output: naturally failed source trajectories with deterministic or sufficiently controlled checkpoint replay.

## Study B — Replay admissibility
For every candidate checkpoint, run no-intervention replay at least as often as preregistered. Define state equivalence before seeing outcome comparisons. Exclude or separately analyze checkpoints that fail replay fidelity.

## Study C — Recovery surface
For admissible checkpoints execute typed evaluator surgeries. At minimum:
- action patch;
- state restoration where semantically meaningful;
- suffix/oracle continuation upper bound.
Agent-realizable recovery methods are reported in a separate arm.

## Study D — Diagnosis faithfulness
Collect root-cause predictions from strong trace debuggers. Convert each prediction into a preregistered intervention test. Report both conventional localization and intervention-faithfulness metrics.

## Study E — Human calibration
Double-annotate a stratified subset for failure type, causal candidate, and recoverability. Report agreement and adjudication protocol. Humans do not override executed causal evidence; annotation answers a different question.

## Required analyses
- task success with task-level uncertainty;
- replay-fidelity rate by environment/task family;
- diagnosis faithfulness;
- recovery AUC and last recoverable checkpoint by intervention family;
- failure category × sufficient intervention type;
- horizon/statefulness slices;
- safety/cost/latency;
- negative and non-monotonic recovery surfaces;
- sensitivity to state-equivalence definition.

## Minimum publication gate
No headline causal claim until the preregistered baseline suite, replay controls, human calibration, and task-level statistical analysis are complete.
