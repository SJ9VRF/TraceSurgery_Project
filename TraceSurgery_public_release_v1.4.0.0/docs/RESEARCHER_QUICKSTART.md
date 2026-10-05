# Researcher Quickstart

This path is intentionally short. A reviewer should be able to tell whether the repository is real in minutes.

```bash
python -m pip install -e '.[dev]'
tracesurgery doctor
pytest
tracesurgery lint-suite --suite tasks/suites/validation_500.yaml
tracesurgery validate-suite --suite tasks/suites/validation_500.yaml --oracle-run
tracesurgery surgery --task tasks/samples/multiapp_research.yaml --output runs/surgery_demo.json
```

For a normal run:

```bash
tracesurgery run --suite tasks/suites/mvp.yaml --agent faulty --trials 3 --output runs/example
```

Every `run` now writes `manifest.json` next to `results.jsonl`. The manifest records the package version, command, Python/platform fingerprint, suite hash, task count, agent, trial count, output path, git commit when available, and only the *presence* of API-key environment variables—never their values.

## What to inspect first

1. `tracesurgery/counterfactual.py` — replay controls and interventions.
2. `tests/test_counterfactual.py` — executable causal semantics.
3. `docs/NOVELTY_AUDIT_2026-09.md` — novelty boundary and overlapping work.
4. `docs/REVIEWER_RED_TEAM.md` — reject reasons and kill criteria.
5. `docs/PUBLIC_CLAIMS.md` — what may and may not be claimed publicly.
