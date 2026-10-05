# Reproducibility contract

TraceSurgery treats reproducibility as part of causal validity, not release polish.

## Every source trial must persist

- task ID and task version;
- environment adapter and version;
- model/provider identifier;
- agent/harness commit;
- seed;
- exact pre-action observation;
- exact action payload;
- evaluator-only pre/post state or checkpoint identifier;
- grader version;
- perturbation/intervention events;
- latency/cost metadata when available.

## Every counterfactual branch must persist

- source trial ID;
- intervention kind and checkpoint;
- source checkpoint hash;
- continuation hash;
- final state hash;
- no-intervention replay-fidelity result for that checkpoint;
- outcome grader result;
- whether the branch is causally admissible.

## Causal admissibility rule

An intervention branch is used for causal estimation only when a no-intervention replay from the same checkpoint reproduces the source final state under the declared equality/hash policy. If replay fidelity fails, the checkpoint is reported as non-admissible rather than silently attributed to the intervention.

Real GUI environments may be partly stochastic. For those adapters, the strict equality rule can be replaced only by a preregistered equivalence relation over task-relevant state. The relation must be defined before looking at intervention outcomes.

## Statistical unit

Branches from the same source task/trajectory are correlated. Paper-level confidence intervals and comparisons must cluster or resample at the task level. Branch count must never be reported as if it were the number of independent samples.
