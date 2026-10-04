# Share copy

## 1-line
TraceSurgery tests whether a proposed cause of a computer-use agent failure is actually causal by checkpointing, intervening, replaying, and re-grading the trajectory.

## Recruiter / hiring manager
I built TraceSurgery, a replay-controlled framework for causal failure analysis in long-horizon computer-use agents. Instead of asking a model to guess which step caused a failure, it restores a checkpoint, runs a no-intervention replay control, applies a surgical action/state/policy intervention, and tests whether the final outcome changes. The public artifact includes an executable demo, causal controls, evidence gating, reproducible study infrastructure, and a paper; external frontier-model benchmarking is intentionally left unclaimed until it is run.

## Short social post
TraceSurgery: don’t guess which step caused an agent failure—intervene, replay, and test it. A causal-evaluation framework for long-horizon computer-use agents, with replay controls, surgical counterfactuals, reproducible study infrastructure, and explicit evidence gating. — Aura Yavary
