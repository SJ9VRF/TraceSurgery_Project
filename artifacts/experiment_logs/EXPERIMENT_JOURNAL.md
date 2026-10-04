# Experiment Journal

> Evidence boundary: entries below are executed local causal investigations or software-validation runs. They are not frontier-model performance experiments.

## EXP-001 - Reproduce the recorded source failure

**Track:** `local_causal`

**Hypothesis.** The bundled corrupted trajectory should deterministically fail before any intervention.

**Setup.** Run the spreadsheet task using the recorded wrong write (summary=41) followed by finish.

**Result.** Source trajectory failed; final spreadsheet.summary=41 while the target is 42.

**Interpretation.** The source failure is reproducible enough to support local counterfactual branching.

**Next decision.** Require same-checkpoint no-intervention replay controls before interpreting repairs.

**Evidence.** `runs/demo_5min.json`

## EXP-002 - Replay-fidelity control at checkpoint 0

**Track:** `local_causal`

**Hypothesis.** Restoring checkpoint 0 and replaying the unchanged suffix should reproduce the source failure.

**Setup.** Checkpoint 0 + no intervention + original suffix.

**Result.** Failure reproduced; replay_matches_source=True.

**Interpretation.** Checkpoint 0 is locally admissible for causal comparison in this deterministic demo.

**Next decision.** Test intervention families at the same checkpoint.

**Evidence.** `runs/demo_5min.json`

## EXP-003 - Action surgery before state corruption

**Track:** `local_causal`

**Hypothesis.** Replacing the wrong set(summary=41) action with set(summary=42) should recover the task.

**Setup.** Checkpoint 0 + action_patch + replay remaining suffix.

**Result.** Recovered successfully; outcome_gain=1.

**Interpretation.** The early failure is action-localizable before the bad write is committed to state.

**Next decision.** Compare against state-only repair and suffix replanning.

**Evidence.** `runs/demo_5min.json`

## EXP-004 - State surgery before the corrupting action

**Track:** `local_causal`

**Hypothesis.** Repairing state at checkpoint 0 might be sufficient if the failure is already state-local.

**Setup.** Checkpoint 0 + oracle state_patch + original suffix.

**Result.** Did not recover; the subsequent recorded action writes 41 again.

**Interpretation.** State repair is insufficient before a future corrupting action; intervention timing matters.

**Next decision.** Test suffix replanning at checkpoint 0 and state repair after corruption.

**Evidence.** `runs/demo_5min.json`

## EXP-005 - Suffix replanning before state corruption

**Track:** `local_causal`

**Hypothesis.** Replacing the future suffix at checkpoint 0 should avoid the wrong write.

**Setup.** Checkpoint 0 + oracle suffix_replan.

**Result.** Recovered successfully; outcome_gain=1.

**Interpretation.** Before corruption, changing the continuation can be sufficient even without direct state editing.

**Next decision.** Move the intervention frontier to checkpoint 1 after the bad write.

**Evidence.** `runs/demo_5min.json`

## EXP-006 - Replay-fidelity control after state corruption

**Track:** `local_causal`

**Hypothesis.** Restoring checkpoint 1 and replaying the unchanged suffix should reproduce the failed final state.

**Setup.** Checkpoint 1 + no intervention + original finish action.

**Result.** Failure reproduced; replay_matches_source=True.

**Interpretation.** Checkpoint 1 is locally admissible and isolates the post-corruption regime.

**Next decision.** Compare action, state, and suffix interventions after corruption.

**Evidence.** `runs/demo_5min.json`

## EXP-007 - Action and suffix repair after corruption

**Track:** `local_causal`

**Hypothesis.** Changing only the remaining finish action or suffix may recover after the wrong value is already in state.

**Setup.** Checkpoint 1 + action_patch; separately checkpoint 1 + suffix_replan.

**Result.** Neither intervention recovered the task.

**Interpretation.** Once the wrong value is persistent state, changing a non-repairing terminal action/continuation is insufficient.

**Next decision.** Test direct state repair at checkpoint 1.

**Evidence.** `runs/demo_5min.json`

## EXP-008 - State surgery after corruption

**Track:** `local_causal`

**Hypothesis.** Repairing the corrupted spreadsheet state at checkpoint 1 should recover the task.

**Setup.** Checkpoint 1 + oracle state_patch + replay finish.

**Result.** Recovered successfully; outcome_gain=1.

**Interpretation.** The same failure changes mechanism across time: action-local before corruption, state-local after corruption.

**Next decision.** Use checkpoint-indexed intervention surfaces rather than a single root-cause label.

**Evidence.** `runs/demo_5min.json`

## EXP-009 - 500-task deterministic software-validation suite

**Track:** `software_validation`

**Hypothesis.** The harness, graders, task loading, and oracle paths should execute across the bundled validation suite without task/schema failures.

**Setup.** Run lint and oracle validation over tasks/suites/validation_500.yaml.

**Result.** 500/500 tasks passed oracle validation; 0 duplicate IDs; lint reported 0 errors / 0 warnings in the verified release.

**Interpretation.** The software-validation surface is broad enough to catch harness regressions, but it is not frontier-model evidence.

**Next decision.** Keep these results explicitly separated from external scientific performance tables.

**Evidence.** `runs/v1_validation/validation_report.json`, `runs/v1_validation/lint_report.json`
