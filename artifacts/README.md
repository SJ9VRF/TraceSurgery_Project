# Raw evidence artifacts

This directory is intentionally less polished than the project homepage. It is the inspectable evidence layer behind the narrative.

- `experiment_logs/` - executed local investigations with hypothesis/setup/result/interpretation/next decision.
- `eval_runs/` - machine-readable local evaluation summaries; external scientific results remain pending.
- `failure_examples/` - raw structured failure cases.
- `plots/` - figures generated from raw local artifacts.
- `configs/` - frozen example experiment/study configurations.
- `qualitative_cases/` - human-readable walkthroughs grounded in raw traces.
- `ablations/` - one JSON record per intervention branch in the deterministic demo.
- `git_history/` - policy and provenance for development history. No history is backfilled or backdated.

Do not treat the deterministic local demo as a frontier-model benchmark result.
