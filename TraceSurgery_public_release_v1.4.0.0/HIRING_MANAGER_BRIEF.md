# TraceSurgery — Hiring Manager Brief

**Aura Yavary**

## One sentence
TraceSurgery turns a failed computer-use trajectory into a controlled family of checkpointed counterfactual experiments, so a claimed root cause must survive an executed intervention rather than merely sound plausible from the trace.

## Why this is technically interesting
Computer-use agents fail in long, stateful workflows where a bad action, hidden state drift, memory corruption, or a poor continuation policy can produce similar terminal symptoms. Trace-only diagnosis cannot reliably separate these mechanisms. TraceSurgery branches from privileged evaluator checkpoints, first verifies replay fidelity, then applies typed interventions and re-grades the resulting state.

## What Aura built
- provider-neutral task, agent, environment, grader, and trajectory contracts;
- exact pre/post observations separated from privileged evaluator state;
- checkpoint/restore/replay counterfactual engine;
- no-intervention controls and replay-fidelity causal gate;
- action, state, and suffix interventions;
- diagnosis-faithfulness evaluation;
- recovery surfaces and bounded repair-set search;
- deterministic state/safety graders and seeded perturbations;
- task-level paired statistics and provenance manifests;
- concurrency-safe resumable external-study ledger with deterministic run IDs;
- fail-closed evidence audit with on-disk SHA-256 verification and guarded paper-table generation;
- 500-task deterministic software-validation suite;
- tests, CI, preregistration, release audit, dataset/release metadata, paper and website.

## Research taste signal
The project was deliberately renamed and narrowed after a 2026 related-work audit showed that the original RecoveryBench framing overlapped with existing recovery, fault-injection, root-cause localization, and counterfactual-repair work. The current project explicitly does **not** claim that recovery, counterfactual repair, or minimal repair are individually novel. The falsifiable gap is replay-controlled decomposition of recoverability over intervention time/type for stateful computer-use agents.

## Evidence already earned
Local evidence establishes software semantics, research controls, and study infrastructure only: deterministic checkpoint replay, branch execution, intervention attribution, 500-task oracle validation, safety/state grading, and automated tests. It does not establish frontier-model superiority or SOTA.

## What would make the paper decisive
Run matched frontier-model agents on OSWorld/BrowserGym-like stateful tasks, reproduce strong debugging/recovery baselines, and test whether:
1. trace-only diagnoses often fail intervention faithfulness;
2. models with similar success rates have different recovery surfaces;
3. action/state/suffix interventions separate distinct failure mechanisms;
4. recoverability collapses at measurable irreversibility frontiers.

## Roles this artifact directly demonstrates readiness for
Computer Use, Agent Evals/Environments, Model Evaluations, Agent Safety, post-training feedback loops, RL environments/data infrastructure, and research engineering for long-horizon agents.

## Release engineering signal
TraceSurgery 1.0 is intentionally auditable: 48 regression tests, 92.75% package statement coverage with a hard 90% gate, direct CLI tests, cross-artifact version/link/claim auditing, deterministic 500-task oracle validation, and a clean wheel build. `python scripts/verify_release.py` runs the complete local verification path. These numbers are software-quality evidence, not agent-performance evidence.
