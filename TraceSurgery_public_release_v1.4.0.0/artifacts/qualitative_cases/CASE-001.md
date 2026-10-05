# CASE-001 - Wrong spreadsheet summary becomes persistent state

**Task.** Produce a summary value of 42 from raw values `[10, 12, 20]`.

**Observed failure.** The recorded trajectory writes `spreadsheet.summary = 41` and then finishes.

## Before corruption - checkpoint 0

- No-intervention replay reproduces the failure.
- `action_patch` to write 42 recovers.
- `suffix_replan` recovers.
- `state_patch` alone does **not** recover because the next recorded action writes 41 again.

## After corruption - checkpoint 1

- No-intervention replay reproduces the failure.
- `state_patch` recovers.
- `action_patch` on the remaining `finish` action does not repair the already-corrupted state.
- `suffix_replan` also fails because the oracle suffix at this point does not include a state repair.

## Research implication

A single label such as "wrong action" hides the temporal structure of recoverability. Before the bad write, policy/action repair is sufficient. After the write, recovery requires changing state. This is the concrete motivation for checkpoint-indexed intervention surfaces.

**Raw evidence:** `runs/demo_5min.json`
