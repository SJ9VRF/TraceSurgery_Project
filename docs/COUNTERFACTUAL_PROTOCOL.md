# Counterfactual surgery protocol

## Experimental unit

A source failed trajectory and all branches derived from it form one correlated branch family. Statistical resampling must preserve this grouping.

## Required checkpoints

For every meaningful action store:

- exact pre-action agent observation;
- evaluator-only pre-action environment snapshot or deterministic replay token;
- action;
- post-action observation;
- evaluator-only post-action state;
- task grader version;
- agent/model/config version;
- environment version and seed.

## Intervention families

### A0 - no intervention
Replay/control for environment determinism.

### A1 - action patch
Replace one action at step `t`; leave pre-state and all later recorded actions unchanged.

Interpretation: tests whether a specific decision is sufficient to flip the outcome under the fixed continuation.

### S1 - state patch
Restore the matched successful/reference pre-state at `t`; leave the failed continuation unchanged.

Interpretation: tests whether accumulated environment-state corruption is sufficient to explain downstream failure.

### O1 - observation refresh
Keep ground-truth state fixed, regenerate/reveal the normal observation at `t`, then continue with the same policy.

Interpretation: separates stale/noisy observation from environment corruption.

### B1 - belief/memory patch
Keep environment state fixed, repair the structured memory/belief state supplied to the policy.

Interpretation: isolates internal state tracking from external world state.

### P1 - local replan
Keep environment and memory state fixed; resample/replan only the next subgoal window.

### P2 - suffix replan
Keep state at `t`, replace all future policy decisions with a validated reference continuation.

Interpretation: upper bound on whether the world is still salvageable without rollback.

### R1 - rollback + replan
Restore an earlier checkpoint and generate a new policy continuation.

Interpretation: measures the value and cost of explicit rollback.

## Primary metrics

For intervention `I` at step `t`:

`OutcomeGain(t,I) = Y(t,I) - Y(no intervention)`

where `Y` is task success or a preregistered deterministic task score.

Additional task-level summaries:

- Last Recoverable Checkpoint per intervention family.
- Recovery AUC across normalized trajectory time.
- Minimum sufficient intervention family.
- Minimum sufficient action-edit set where tractable.
- Recovery cost: extra actions, latency, tokens, dollar cost.
- Safety delta: change in irreversible/high-risk effects.
- Diagnosis faithfulness: whether a predicted root-cause step has positive executed intervention effect.

## Validity controls

- Replay the no-intervention branch to quantify nondeterminism.
- Require paired task seeds/configurations across compared models.
- Separate evaluator privileges from agent-visible tools.
- Never call a patched branch "recovery by the agent"; it is evaluator intervention evidence.
- Log unsuccessful surgeries as first-class negative results.
- Predeclare which interventions are allowed for each environment/task.
- Use task-clustered intervals; do not treat branch count as independent sample size.
