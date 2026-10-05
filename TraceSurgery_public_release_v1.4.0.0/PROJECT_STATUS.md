# Project status - TraceSurgery v1.0.3

**Author: Aura Yavary**

## Current honest label

**Stable, executable causal-evaluation research artifact; realistic frontier-agent study pending.**

TraceSurgery 1.0 is stable in the engineering/research-artifact sense: public CLI behavior, serialized study/evidence interfaces, release gates, and local causal semantics are reproducibly validated. It is **not** a claim that the external frontier-model experiment is complete.

## Implemented and tested

- Counterfactual checkpoint/restore/replay engine.
- Mandatory no-intervention replay control before causal interpretation.
- Replay-fidelity gating and stable checkpoint/continuation/final-state provenance hashes.
- Executed action-patch, state-patch, and oracle-suffix intervention families.
- Executable diagnosis-faithfulness evaluation.
- Bounded minimum-cardinality oracle action-repair-set search as a causal upper-bound probe.
- Recovery-surface summaries over causally admissible checkpoints.
- Strict agent-visible observation vs privileged evaluator-state separation.
- Intervention events separated from agent failure events.
- 20 seeded perturbation primitives.
- Deterministic state and safety graders.
- 500-task deterministic local software-validation suite.
- Task-clustered and paired-task bootstrap analysis.
- Human annotation schema/tooling and adjudication protocol.
- Concurrency-safe resumable external-study ledger with deterministic run IDs.
- Scientific evidence gate with on-disk manifest SHA-256 verification.
- Fail-closed JSON/CSV/Markdown/LaTeX scientific report generation.
- Versioned experiment/study/evidence schemas and compatibility policy.
- One-command release verifier, CI, technical report, website, reviewer/hiring packets, reproducibility and preregistration artifacts.

## Important novelty boundary

Recent work already covers GUI recovery, root-cause localization, counterfactual repair, and minimal repair-family recovery. TraceSurgery therefore does **not** claim those primitives as individually novel. The intended contribution is replay-controlled, checkpoint-indexed decomposition of recoverability across intervention families for stateful computer-use agents, together with an intervention-faithfulness test for diagnosis claims.

## Verified v1.0.3 release checks - 2026-09-27

- **48/48 automated tests passed.**
- **92.75% package statement coverage**, with a hard release gate at 90%.
- Public CLI itself is directly regression-tested rather than excluded from coverage.
- **500/500** validation-suite tasks passed oracle validation; **0 duplicate IDs**.
- **9/9 Claim Ledger claims** recompute from raw evidence; published local eval table matches the raw branch records.
- Task lint: **0 errors / 0 warnings**.
- `tracesurgery doctor` returned `ok: true`.
- `tracesurgery release-audit` found no claim/link/version errors in the working tree; cache warnings are removed in the clean release archive.
- `compileall` passed.
- A `tracesurgery-1.0.3-py3-none-any.whl` wheel built successfully with `--no-build-isolation --no-deps` in the offline container.
- The external-study smoke path creates deterministic study cells, atomically claims work, records completion, verifies a real manifest SHA-256 from disk, and produces guarded scientific summaries. That smoke path is infrastructure validation, not a model result.
- No external frontier-model performance or comparative superiority claim is introduced by v1.0.3.

## Not yet empirical frontier evidence

The following still require external model/environment/human resources and are intentionally not fabricated:

- frontier or open-model calls in a realistic browser/desktop environment;
- OSWorld 2.0 / BrowserGym-style execution;
- matched reproduction of strong adjacent debugging/recovery baselines;
- human double annotation and inter-annotator agreement where preregistered;
- paper-scale recovery surfaces and repeated trials;
- statistically supported model comparisons;
- any comparative superiority claim.

## External-study readiness

A frozen `StudySpec` expands to deterministic run IDs and a resumable, concurrency-safe ledger. Provider/environment implementations must satisfy explicit adapter contracts. Evidence records are performance-claim eligible only if they pass the scientific evidence gate with model revision, benchmark version, grader revision, external provenance, and optional on-disk manifest hash verification. Local validation and synthetic demos are machine-rejected for that purpose.

## Public-release hardening - v1.0.3

- Added a deterministic five-minute demo and direct regression test.
- Added GitHub bug/validity issue forms and a validity-focused pull-request template.
- Removed generated `build/` source duplicates from the public release tree.
- Release audit now flags build/dist/egg-info artifacts as release hygiene issues.
- `verify_release.py` now audits the untouched tree first, cleans only artifacts it generates, and performs a final zero-warning audit.
- Scientific claims are unchanged; no external model-performance result was added.


## Claim traceability - v1.0.3

Every released local-evidence claim is mapped to raw files and an executable verification rule in `docs/evidence/CLAIM_LEDGER.md` and `artifacts/claim_ledger.json`. `python scripts/verify_evidence_layer.py` recomputes the released counts and step-specific mechanistic statements directly from `runs/demo_5min.json`, the experiment journal, and evidence logs. A mismatch exits non-zero.

## Evidence Layer - v1.0.3

The Evidence Layer is now a release-gated artifact, not an optional narrative appendix. It contains:

- 9 documented executed investigations (8 local causal branches/analyses + 1 software-validation investigation);
- 3 failed repair attempts preserved as negative evidence;
- 8 major design decisions with alternatives, evidence, trade-offs, and outcomes;
- 4 unexpected findings grounded in raw traces;
- 8 raw counterfactual branch JSON records, structured failure examples, machine-readable eval tables, and a qualitative case;
- an explicit Git-history boundary: no earlier commits are reconstructed or backdated.

These artifacts remain local/mechanistic evidence. They do not become frontier-model performance claims.

## Clean-room Evidence Layer archive verification

The v1.0.3 ZIP was extracted into a fresh directory. Before running tests it contained zero cache/build/bytecode junk; release audit reported 0 errors / 0 warnings; **658 tracked checksums** verified; **48/48 tests** passed; and the Evidence Layer verifier passed **10/10 checks** (9 claim rules plus published-table consistency). The Git bundle verifies as complete history from the honest imported baseline.
