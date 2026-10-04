# Decision log

Each entry follows **Decision -> Alternatives -> Evidence -> Trade-off -> Outcome**. These decisions are tied to implemented artifacts rather than retrospective storytelling.

## D-001 - Rename and narrow the project to TraceSurgery

**Decision.** Move from a generic recovery benchmark to replay-controlled causal intervention analysis.  
**Alternatives.** Keep RecoveryBench; focus mainly on failure taxonomy; focus mainly on repair success rate.  
**Evidence.** Novelty review showed adjacent work already covers GUI recovery, root-cause localization, counterfactual repair, and minimal repair families.  
**Trade-off.** Narrower claim, but more falsifiable and less likely to be dismissed as incremental.  
**Outcome.** TraceSurgery centers checkpoint-indexed intervention surfaces and intervention-faithfulness.  
**Evidence path.** `docs/NOVELTY_AUDIT_2026-09.md`, `CHANGELOG.md`.

## D-002 - Require no-intervention replay before causal interpretation

**Decision.** A checkpoint is causally usable only when an unchanged replay reproduces the source trajectory sufficiently for the declared control.  
**Alternatives.** Compare each repair branch directly with the original logged failure; tolerate replay divergence and average over it.  
**Evidence.** Replay drift is a direct confound for counterfactual attribution; the deterministic demo verifies two admissible controls.  
**Trade-off.** Some real-world checkpoints may become unusable, reducing sample size.  
**Outcome.** Causal claims become more conservative and auditable.  
**Evidence path.** `runs/demo_5min.json`, `docs/COUNTERFACTUAL_PROTOCOL.md`.

## D-003 - Separate action, state, and suffix interventions

**Decision.** Do not collapse repair into one generic "recovered" flag.  
**Alternatives.** Use only action correction; use only oracle replay; report final success without mechanism.  
**Evidence.** In the local case, action/suffix repair work before corruption while state repair works after corruption.  
**Trade-off.** More branches and privileged upper-bound probes; requires careful labeling of agent-realizable vs oracle interventions.  
**Outcome.** The framework exposes how the locus of recoverability changes over time.  
**Evidence path.** `artifacts/plots/demo_intervention_matrix.svg`, `artifacts/qualitative_cases/CASE-001.md`.

## D-004 - Treat the 500-task suite as software validation, not a scientific benchmark

**Decision.** Keep local generated tasks for regression/oracle validation only.  
**Alternatives.** Put 500/500 in the hero section as benchmark performance.  
**Evidence.** The suite tests harness breadth and deterministic oracle paths but does not represent frontier-model behavior in realistic environments.  
**Trade-off.** Less impressive headline number; much stronger claim discipline.  
**Outcome.** Scientific result generation rejects local validation/demo evidence.  
**Evidence path.** `PROJECT_STATUS.md`, `docs/PUBLIC_CLAIMS.md`, `tracesurgery/evidence.py`.

## D-005 - Make evidence reporting fail closed

**Decision.** Scientific tables are generated only after provenance and evidence audits pass.  
**Alternatives.** Generate tables first and rely on manual review; accept partially specified model/environment revisions.  
**Evidence.** Provenance mistakes are easy to make and hard to detect once results reach a paper.  
**Trade-off.** More metadata and friction for external runs.  
**Outcome.** Missing external provenance, benchmark revision, grader revision, or verified manifest blocks claim eligibility.  
**Evidence path.** `docs/SCIENTIFIC_RESULT_PIPELINE.md`, `tracesurgery/scientific_report.py`.

## D-006 - Preserve privileged interventions as upper bounds, not agent capabilities

**Decision.** Oracle state patches and oracle suffixes must be explicitly labeled as diagnostic upper bounds.  
**Alternatives.** Present all repair branches as if an agent could execute them online.  
**Evidence.** State surgery uses evaluator-side access that a normal policy may not possess.  
**Trade-off.** Results become less headline-friendly but scientifically interpretable.  
**Outcome.** Agent-realizable recovery and oracle recoverability remain conceptually separate.  
**Evidence path.** `docs/BASELINE_CONTRACT.md`, `docs/VALIDITY_THREATS.md`.

## D-007 - Use task-clustered statistics for repeated trials

**Decision.** Cluster uncertainty at the task level and use paired task-level comparisons when appropriate.  
**Alternatives.** Treat every repeated run as an independent sample.  
**Evidence.** Repeats on the same task are correlated and otherwise understate uncertainty.  
**Trade-off.** Wider, more honest confidence intervals.  
**Outcome.** Statistics utilities and scientific reporting preserve the task as the primary independence unit.  
**Evidence path.** `tracesurgery/statistics.py`, `docs/STATISTICS.md`.

## D-008 - Do not reconstruct or backdate Git history

**Decision.** Start a real incremental history from the imported verified release and explicitly document the boundary.  
**Alternatives.** Create a visually attractive sequence of fake historical commits.  
**Evidence.** Backfilled history would be misleading and undermine the purpose of the Evidence Layer.  
**Trade-off.** Earlier development remains represented by release artifacts/changelog rather than commit-by-commit history.  
**Outcome.** New evidence-layer work is committed incrementally from this point forward; a Git bundle preserves it.  
**Evidence path.** `artifacts/git_history/HISTORY_POLICY.md`.
