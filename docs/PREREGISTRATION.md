# Paper-scale preregistration template

Complete this file before running the headline frontier-model experiment.

## Primary hypotheses

H1. Trace-only root-cause localization has imperfect intervention faithfulness: a non-trivial fraction of predicted causal steps will not flip outcome under the preregistered repair.

H2. Recovery surfaces differ by model even after conditioning on baseline task success.

H3. Longer intervention delay reduces recoverability on long-horizon stateful tasks.

H4. World-state restoration and policy replacement explain distinct subsets of recoverable failures.

## Primary endpoints

1. Diagnosis Faithfulness.
2. Recovery AUC by intervention family.
3. Last Recoverable Checkpoint normalized by source trajectory length.
4. Paired outcome gain versus no-intervention replay.
5. Safety side-effect rate under recovery interventions.

## Exclusion rules

- checkpoint fails replay-fidelity control;
- grader failure or environment corruption;
- task declared infeasible by independent audit;
- intervention not semantically valid for the task;
- provider outage/truncated trace before the benchmark stop condition.

Exclusions are applied without reference to whether the intervention succeeded.

## Statistical plan

- task is the primary independent unit;
- paired task-level bootstrap for model/intervention contrasts;
- 95% confidence intervals;
- report effect sizes with intervals, not only p-values;
- correct or hierarchically structure confirmatory tests when multiple primary contrasts are used;
- preserve all negative surgeries and failed repairs.

## Required sensitivity analyses

- strict final-state equality vs task-relevant state equivalence for replay fidelity;
- excluding trajectories with exogenous environment failures;
- results by task horizon and application count;
- results with and without high-risk tasks;
- oracle repair upper bound vs implementable diagnosis-driven repair.
