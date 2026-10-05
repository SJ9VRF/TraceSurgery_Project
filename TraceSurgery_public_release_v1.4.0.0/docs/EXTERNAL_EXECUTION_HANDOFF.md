# External execution handoff

TraceSurgery's local release validates software semantics; it does not contain frontier-model performance evidence. This handoff is the boundary between the released framework and a real external study.

## Required before the first scientific run

1. Freeze exact benchmark/environment revision and task IDs.
2. Freeze exact model/provider revision or dated endpoint configuration.
3. Implement the `ProviderAdapter` and `StatefulEnvironmentAdapter` contracts in `tracesurgery.external`.
4. Run adapter conformance tests against a non-scientific smoke task.
5. Create a study matrix from `configs/external_study.example.yaml` using `tracesurgery study-init`.
6. Record one result and one provenance manifest per ledger run. Do not overwrite failed attempts; preserve attempt history outside the core ledger if the external executor retries.
7. Run no-intervention replay controls before interpreting any intervention branch as causal.
8. Export only external records into the evidence JSONL, then run `tracesurgery evidence-audit --verify-files`.
9. Generate paper-ready summaries only with `tracesurgery evidence-report`; it refuses invalid evidence.

## Evidence record gate

A performance record is ineligible if it comes from local validation/synthetic demo, lacks model revision, benchmark version, manifest provenance, a frozen grader revision, or identifies the local sandbox as its environment. With file verification enabled, the manifest must exist and its SHA-256 must match the recorded digest. A causal metric can additionally be excluded if replay fidelity fails.

## Resume semantics

The study ledger uses deterministic run IDs from study/task/model/environment/seed/repetition. `study-claim` atomically moves one pending (or retryable failed) row to running, records the worker ID, and increments its attempt counter. `study-mark` explicitly records completion/failure. The local JSONL backend uses an atomic directory lock and atomic file replacement; do not assume that lock provides global transactions across object stores or unrelated cluster filesystems.

## What the framework intentionally does not do

The core package does not impersonate or bundle proprietary frontier-model clients, OSWorld, BrowserGym, or credentials. Concrete adapters belong in optional/private integration packages so that the public core remains auditable and does not imply external execution that did not occur.
