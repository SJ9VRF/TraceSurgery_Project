# Realistic Environment Integration Contract

TraceSurgery should sit *above* a realistic computer-use environment rather than duplicate one.

An adapter must implement:

```python
class Environment(ABC):
    def reset(self, task, seed=0) -> Observation: ...
    def step(self, action) -> Observation: ...
    def snapshot(self) -> dict: ...   # privileged grader state
    def is_terminal(self) -> bool: ...
```

## Non-negotiable properties

1. **Observation/ground-truth separation.** The agent never receives private grader state.
2. **Deterministic reset when supported.** Store environment image/version and seed.
3. **Outcome verification.** Grade final external state, not the agent's completion claim.
4. **Trace preservation.** Store screenshots/UI trees/tool calls and state transitions when allowed.
5. **Action normalization.** Map environment-native actions to TraceSurgery `Action` records without discarding native payloads.
6. **Safety boundary.** Destructive/financial/publication actions require sandboxing or explicit confirmation policies.
7. **Perturbation hooks.** Controlled interventions must be logged as benchmark interventions, never silently labeled as agent failures.
8. **Version pinning.** Save environment version, task version, grader version, adapter commit, model identifier, and seed.

## OSWorld/desktop-style mapping

- `reset`: restore VM/container snapshot and task-specific initial resources.
- `step`: execute click/type/hotkey/shell or environment-native action.
- `snapshot`: collect task-specific verifier state (files, app state, DB values, document contents).
- `Observation`: screenshot plus optionally accessibility/UI tree, never verifier-only fields.

## BrowserGym/WebArena-style mapping

- `reset`: initialize benchmark site/database state.
- `step`: browser action through the environment action space.
- `snapshot`: direct site/database checks or benchmark-provided evaluator state.
- Preserve tab/session identifiers because cross-tab state and session expiration are recovery-relevant.

## Integration acceptance tests

An adapter is release-ready only when:

- the same task can be reset at least 20 times without state leakage;
- an oracle/scripted policy reaches the expected state on deterministic tasks;
- intentionally wrong actions fail the state grader;
- private verifier state is absent from agent observations;
- interrupted/perturbed trials contain explicit intervention records;
- replay artifacts contain enough information for a human to reconstruct the failure sequence.
