# Adapter conformance

External model and environment integrations are intentionally behind narrow contracts.

A provider adapter must expose a stable `name`, immutable `model_revision`, deterministic seed reset where the provider permits it, `act(observation, task)`, and `close()`.

A stateful environment adapter must expose a stable `name` and `version`, plus `reset`, `step`, `snapshot`, `restore`, and `is_terminal`. Snapshot/restore is not an implementation detail: causal replay is invalid when the environment cannot restore the intervention checkpoint with sufficient fidelity.

Before scientific use, an adapter implementation should pass these checks:

- reset produces the declared task start state;
- snapshot -> mutate -> restore round-trips relevant benchmark state;
- no-intervention replay reproduces the source branch within the preregistered fidelity criterion;
- task/grader hidden state is not exposed to the provider observation;
- model revision and environment version are persisted in evidence;
- raw trace, run manifest, grader revision and intervention specification are retained;
- retry behavior does not silently change seed, task, model revision or prompt policy.

The core ships the protocol and conformance surface, not fake OSWorld/provider implementations.
