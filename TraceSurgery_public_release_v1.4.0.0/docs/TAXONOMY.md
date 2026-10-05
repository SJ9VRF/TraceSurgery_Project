# Failure Ontology

The ontology is hierarchical and should be refined empirically on pilot trajectories before the paper split is frozen.

1. **Perception / grounding** — element misidentification, text misunderstanding, spatial confusion, missed occluded state.
2. **State estimation** — stale state, hidden state error, incorrect state assumption, lost intermediate state, missed transition.
3. **Planning** — bad decomposition/order, missing prerequisite, premature commitment, infeasible plan.
4. **Memory** — forgotten fact, incorrect retrieval, source confusion, context pollution.
5. **Execution** — wrong target/text, malformed tool call, duplicate action.
6. **Verification** — false-positive completion, failure not detected, partial completion misclassified, state not verified.
7. **Recovery** — repeated failed action, incorrect repair, unnecessary restart, failed replan, repair causes new failure.
8. **Safety** — unintended side effect, irreversible action, privilege/constraint violation.

The benchmark distinguishes **event type** from **causal role**. A verification failure may be a downstream symptom of an earlier grounding error rather than the root cause.
