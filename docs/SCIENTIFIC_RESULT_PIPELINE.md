# Scientific result pipeline

TraceSurgery intentionally separates **running experiments** from **making scientific claims**.

1. Freeze a `StudySpec` and initialize the run ledger.
2. Workers atomically claim cells with `tracesurgery study-claim`.
3. Provider/environment adapters execute the exact cell and persist raw traces plus a manifest.
4. Workers mark the cell complete or failed; reruns preserve the deterministic run ID and increment `attempt`.
5. Convert completed runs into `EvidenceRecord` rows. Every external row must identify model revision, benchmark version, grader version, manifest path and manifest SHA-256.
6. Run `tracesurgery evidence-audit --verify-files`. The audit recomputes manifest hashes from bytes, rejects local/synthetic runs, duplicate IDs, missing revisions and provenance failures.
7. Only after the gate passes, run `tracesurgery evidence-report`. It emits JSON, CSV, Markdown and LaTeX summaries using task-clustered uncertainty and paired task-level deltas.

`evidence-report` fails closed: it will not produce paper-ready tables from an invalid evidence file. This is deliberate protection against accidentally promoting infrastructure smoke tests into benchmark claims.

## Multi-worker execution

The JSONL ledger uses an atomic directory lock plus atomic file replacement. `study-claim` therefore assigns a study cell to one worker at a time on a shared POSIX-like filesystem. For distributed object stores or cluster schedulers, replace the ledger backend with a transactional store rather than assuming this local lock is globally distributed.

## What this release still does not do

This release does not bundle credentials, invoke proprietary frontier APIs, provision OSWorld/BrowserGym machines, or pretend that a schema-valid smoke record is a model result. Those remain external execution responsibilities.
