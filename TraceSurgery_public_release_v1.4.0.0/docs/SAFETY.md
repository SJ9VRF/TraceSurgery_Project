# Safety Evaluation

Actions should be risk-labelled as reversible/safe, moderate, or high-risk. High-risk tasks require explicit benchmark constraints and deterministic post-state checks.

Never evaluate real destructive behavior against production accounts. Use isolated sandboxes, disposable accounts, fixtures, mocked payment/delete flows and checkpointable state.

A task can be outcome-successful and still fail the benchmark if a safety constraint is violated.
