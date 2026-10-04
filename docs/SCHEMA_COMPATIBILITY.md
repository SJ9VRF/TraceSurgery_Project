# Schema Compatibility Policy

TraceSurgery 1.0 treats experiment manifests, external-study specs/ledgers, and scientific evidence records as research interfaces rather than incidental JSON.

## Versioned records
- `ExperimentManifest.schema_version = 1.0`
- `StudySpec.schema_version = 1.0`
- `RunEntry.schema_version = 1.0`
- `EvidenceRecord.schema_version = 1.1`

Schema versions are independent of the Python package version. A package patch release may fix implementation bugs without changing a record schema.

## Compatibility promise for the 1.x line
1. Existing required fields will not silently change meaning.
2. New optional fields may be added in backward-compatible releases.
3. Removing or renaming a required field requires a schema-version change and an explicit migration note.
4. Scientific result tooling must reject records it cannot validate rather than coercing them silently.
5. Raw external evidence should remain immutable; migrations create a new derived artifact and preserve the source record.

## Reproducibility rule
Every scientific result must retain the exact study snapshot, run ledger entry, manifest provenance, grader revision, benchmark version, model revision, and evidence schema version used to produce it.

## Non-goal
This policy does not claim long-term API stability for internal Python classes. The stable research interfaces are the documented CLI commands and versioned serialized schemas.
