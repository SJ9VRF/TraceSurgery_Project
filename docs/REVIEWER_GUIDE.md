# Reviewer Guide

This document makes the strongest objections easy to inspect rather than hiding them.

## What is the claim?
Not: “we invented agent recovery.”

Not: “we invented counterfactual repair.”

Not: “we have a new error taxonomy.”

The proposed contribution is **replay-controlled causal evaluation of recoverability in stateful computer-use trajectories**: each intervention branch is admitted as causal evidence only when an unmodified replay from the same checkpoint reproduces the source continuation under a preregistered state-equivalence rule.

## What is evaluator-privileged?
Checkpoint state, oracle actions, reference suffixes, and state patches are evaluator-only probes. They are never exposed to the evaluated agent. They estimate causal upper bounds and mechanism attribution; they are not presented as deployable recovery policies.

## Main threats to validity
1. **Replay nondeterminism** — addressed with no-intervention checkpoint controls; failed controls exclude the checkpoint from causal summaries.
2. **Oracle intervention realism** — interventions are mechanism probes/upper bounds; agent-realizable recovery must be reported separately.
3. **Grader leakage/gaming** — final outcomes are state-based where possible and the same grader scores source/control/intervention branches.
4. **Correlated branches** — statistical resampling is at task/source-family level, not branch level.
5. **Task contamination** — public development tasks and hidden evaluation tasks must be separated in the external study.
6. **Intervention-family incompleteness** — a failed repair does not prove irrecoverability outside the tested family.
7. **Privileged checkpoint equivalence** — the external protocol must define which state components determine replay equivalence.

## Fast audit path
```bash
pip install -e '.[dev]'
tracesurgery doctor
tracesurgery release-audit
pytest
tracesurgery validate-suite --suite tasks/suites/validation_500.yaml --oracle-run
tracesurgery surgery --task tasks/samples/spreadsheet_formula.yaml --output runs/reviewer_demo.json
```

## Evidence boundary
The 500-task suite is a deterministic software-validation suite. It is not a claim about frontier computer-use performance. See `docs/PUBLIC_CLAIMS.md`.
