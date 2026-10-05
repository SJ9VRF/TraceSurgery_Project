# TraceSurgery 1.0 Release Notes

**Author: Aura Yavary**

TraceSurgery 1.0 is the first release designated as a stable research artifact. The designation means the local framework, release gates, public CLI surface, and serialized research records are internally consistent and reproducibly validated. It does **not** mean the external frontier-model study has been completed.

## What is stable
- checkpoint / restore / replay semantics;
- replay-fidelity gate before causal interpretation;
- action, state, and suffix surgeries;
- diagnosis-faithfulness and recovery-surface machinery;
- task-level statistical unit and scientific evidence gate;
- resumable concurrency-safe study ledger;
- provenance-bearing experiment manifests;
- fail-closed scientific report generation;
- versioned serialized study/evidence interfaces;
- public CLI commands documented in the README and quickstart.

## Quality bar for 1.0
- test coverage is release-gated at 90% or higher for the `tracesurgery` package;
- the 500-task deterministic suite must lint cleanly and pass oracle execution;
- public artifacts must pass the release claim audit;
- broken local documentation links and version drift are release errors;
- a wheel must build from the clean release tree;
- no frontier-model performance result is included without external provenance.

## What remains external empirical work
Realistic browser/desktop execution, frontier/open-model rollouts, matched adjacent baselines, independent human calibration, repeated trials, and paper-scale statistical results still require external compute, credentials, and/or human annotators.
