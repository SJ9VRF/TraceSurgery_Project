# Baseline Contract for the External Study

A paper-scale result is not valid if TraceSurgery is compared only to weak handcrafted baselines.

## Baseline families

### Trace-only diagnosis
Input: exactly the same trajectory view available to the debugger being tested.
Output: ranked causal step(s), failure label, confidence, optional repair proposal.
Evaluation: localization metrics **and** TraceSurgery intervention faithfulness.

### Retry / reflection / replan recovery
Input: current agent-visible state and history only.
No evaluator checkpoint, oracle action, hidden state, or reference suffix may be exposed.
Report: task success, added actions, latency, cost, unsafe side effects.

### Verifier-guided recovery
Verifier may observe only fields declared in the baseline protocol. If it receives privileged state, that baseline must be labeled evaluator-assisted.

### Diagnosis-driven re-execution
Reproduce the strongest available computer-use debugging/recovery pipeline with matched model access and task budget where feasible.

### Oracle upper bounds
- oracle critical action patch;
- oracle state restoration;
- oracle suffix continuation;
- bounded multi-action repair set.
These are causal probes, not deployable-agent baselines.

## Matching rules
- same task initial state;
- same model/version and decoding settings where applicable;
- same maximum action budget unless method inherently consumes recovery budget, which must be reported;
- same final-state grader;
- repeated trials with task-level pairing;
- failures, timeouts, safety events, and invalid branches retained.

## Forbidden comparison
Do not compare an evaluator-privileged surgery to an agent-realizable recovery method and call the difference “performance improvement.” They answer different questions.
