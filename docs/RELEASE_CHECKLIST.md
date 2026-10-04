# Definition of Done

- [ ] 500+ verified tasks
- [ ] paper-scale multiple-trial trajectories
- [ ] empirically refined ontology
- [ ] causal failure graph annotations
- [ ] recovery-window and point-of-no-return annotations
- [ ] controlled perturbation suite
- [ ] deterministic/state graders
- [ ] safety constraints/graders
- [ ] strong agent/model baselines
- [ ] confidence intervals and per-category breakdowns
- [ ] human gold subset + inter-annotator agreement
- [ ] contamination/leakage analysis
- [ ] cost/latency analysis
- [ ] public task/data subset + dataset card
- [ ] hidden test split / leaderboard protocol
- [ ] reproducible code and locked environment versions
- [ ] trajectory explorer + demo video
- [ ] project homepage
- [ ] technical report / paper
- [ ] limitations and negative results
- [ ] no fabricated or placeholder performance claims in public artifacts

## 1.0 engineering gates
- [ ] `pytest --cov=tracesurgery --cov-fail-under=90` passes
- [ ] `python scripts/verify_release.py` passes
- [ ] wheel builds with `pip wheel --no-build-isolation --no-deps`
- [ ] local documentation links resolve
- [ ] public version strings match package version
