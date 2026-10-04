# TraceSurgery: Don’t Guess What Broke. Intervene.

**Aura Yavary · 2026**

Long-horizon computer-use agents often fail in ways that look obvious only after the fact. A transcript may suggest a critical step, but a plausible explanation is not the same as a causal one. TraceSurgery treats a failed trajectory as an experiment: checkpoint the run, replay an untouched control, apply a preregistered intervention, replay the branch, and re-grade the executed outcome.

The central object is a **counterfactual recovery surface** over checkpoint time and intervention family. Instead of asking only whether an agent eventually succeeded, TraceSurgery asks which changes would have been sufficient to save the run, how long that opportunity remained, and whether a debugger's claimed root cause survives an executed repair test.

The current public artifact implements replay-fidelity gating, action/state/suffix interventions, diagnosis-faithfulness evaluation, provenance hashes, state-based grading, safety checks, deterministic local validation, task-level statistics, and a fail-closed scientific evidence pipeline. The bundled 500-task suite validates software semantics; it is deliberately not presented as frontier-agent performance evidence.

A small deterministic demo illustrates the difference between explanation and intervention. A spreadsheet agent writes `41` when the correct summary is `42`. At the first checkpoint, patching the action or replanning the suffix saves the task. Restoring the pre-state alone does not, because the unchanged suffix simply writes the wrong value again. At the next checkpoint, after the bad write has happened, a state repair succeeds. The mechanism—not just the final failure label—changes with time.

The next scientific step is an external study on realistic browser/desktop environments with matched baselines, repeated trials, human calibration where preregistered, and task-clustered uncertainty. Until those runs exist, TraceSurgery makes no SOTA or model-superiority claim.
