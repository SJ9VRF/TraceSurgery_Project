# Paper Experiment Matrix

## Conditions
A. Natural run
B. Controlled perturbation
C. Controlled perturbation + explicit recovery hint
D. Oracle checkpoint / failure-location upper bound

## Agent baselines
- Reactive / ReAct-style baseline
- Retry-only
- Reflection
- Episodic memory
- Explicit post-action verification
- Oracle failure detection
- Oracle recovery point

## Required ablations
- no structured state logging
- no post-action verification
- no recovery opportunity signal
- no perturbation diversity
- deterministic-only grader vs composite grader calibration

## Statistical rules
- Never pool multiple trials as if independent tasks when reporting CIs.
- Pre-register the primary metrics before paper-scale model runs.
- Report per-category results, not only macro averages.
- Include negative results and failure examples.
- Do not tune prompts on the held-out test split.
