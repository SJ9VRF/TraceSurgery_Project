# Git history provenance

The distributed v1.0.1 source release did not contain `.git` history. This Evidence Layer does **not** invent or backdate earlier commits.

A new repository was initialized from the verified v1.0.1 archive on 2026-09-26 with the baseline commit:

- `Import verified TraceSurgery v1.0.1 baseline`

Subsequent Evidence Layer changes are committed incrementally as they are actually made. The accompanying `TraceSurgery_evidence_history.bundle` preserves that genuine history and can be inspected with standard Git tooling.

Earlier project evolution is documented by `CHANGELOG.md`, release-validation artifacts, and versioned files rather than reconstructed fake commits.

As of v1.0.3, the final Evidence Layer bundle contains the imported baseline plus **17 real incremental commits** made after that boundary, including claim-traceability hardening. No earlier history is reconstructed or backdated.
