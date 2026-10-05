# Reviewer red-team: what could still make TraceSurgery look weak?

Author: **Aura Yavary**

This file is intentionally adversarial. A strong research artifact should make its rejection risks explicit before a reviewer does.

## 1. "This is just CausalFlow/MRFR applied to GUI agents."

**Why the criticism is plausible:** generic counterfactual repair and minimal repair-family replay already exist.

**Required defense:** the paper must empirically justify the CUA-specific decomposition. The strongest evidence would show that action-only causal attribution is insufficient because persistent world-state corruption, hidden-state/belief divergence, or continuation-policy failures require different interventions, and that checkpoint-indexed recovery geometry predicts behavior not visible in final success.

**Failure condition:** if action patches alone explain nearly all recoverable failures and recovery surfaces add little beyond a critical-step label, the contribution should be reframed or stopped.

## 2. "Oracle patches make the benchmark unrealistic."

**Correct response:** oracle action/state/suffix patches are evaluator instruments and upper bounds, not deployable recovery policies.

**Required experiment:** separate two questions:
1. causal diagnosis using oracle/minimal interventions;
2. implementable recovery using model-generated interventions.

Never report oracle branch success as agent self-recovery.

## 3. "Counterfactual replay is not causal if the environment is nondeterministic."

**Mitigation now implemented:** every tested checkpoint has a no-intervention replay control. Intervention branches are excluded from causal summaries if the control cannot reproduce the source under the preregistered equivalence policy.

**Paper requirement:** report replay-fidelity coverage. A method that obtains attractive causal effects only on low-fidelity checkpoints is invalid.

## 4. "State patches leak privileged information."

They do, by design, to the evaluator. The agent must never receive evaluator-only state. State-patch results answer a mechanism question (was world-state corruption sufficient?), not a deployment claim.

## 5. "The 500 tasks are toy data."

Correct. They are software-validation fixtures. Do not put their completion rate in the abstract, leaderboard, or resume. The scientific study needs established realistic computer-use environments and real model trajectories.

## 6. "The benchmark has no independent human ground truth."

The main causal outcome is execution-based, which reduces reliance on subjective labels, but human calibration remains necessary for task feasibility, taxonomy analysis, and debugger-label evaluation. Paper release requires double annotation on a preregistered subset and agreement reporting.

## 7. "Recovery AUC hides non-monotonic behavior."

Always publish the underlying checkpoint curve/surface. AUC is a summary, not the primary visual evidence. Non-monotonic recovery is scientifically interesting and must not be forced into a monotonic frontier.

## 8. "You selected only failures that are easy to repair."

Use all failed source trajectories passing task/environment validity checks, including zero-recovery surfaces. Preregister exclusions independently of branch success.

## 9. "The paper compares models using correlated branches as N."

Do not. The primary unit is the source task/trajectory. Use paired task-level analysis or hierarchical models and report the number of independent tasks separately from branch count.

## 10. "The name/claim is more polished than the evidence."

The public release must visibly separate:
- implemented mechanism;
- local software validation;
- real model evidence;
- hypotheses.

If the real study is not yet run, say so on the homepage, in the README, and in the technical report.

## Kill criteria

TraceSurgery should not be pushed as a flagship paper if the real experiment finds any of the following:

- poor checkpoint replay fidelity on realistic environments;
- recovery surfaces collapse to the same information as one-step critical localization;
- intervention-family decomposition is unstable across equivalent task states;
- grader state is too weak to distinguish genuine completion from benchmark gaming;
- effects disappear under task-level uncertainty;
- the final novelty sweep finds a directly equivalent CUA recovery-surface benchmark.

A negative result can still produce a useful technical report, but it should not be marketed as a frontier research breakthrough.
