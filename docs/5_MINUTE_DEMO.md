# Five-minute reproducible demo

This demo verifies the semantics of TraceSurgery; it is **not** a frontier-model performance result.

## 1. Install

```bash
python -m pip install -e ".[dev]"
tracesurgery --version
tracesurgery doctor
```

## 2. Run the known-failure counterfactual demo

```bash
python scripts/demo_5min.py --output runs/demo_5min.json
```

The demo uses the bundled spreadsheet task with a deliberately corrupted recorded action. It then:

1. executes the failed source trajectory;
2. checks same-checkpoint no-intervention replay fidelity;
3. patches actions one checkpoint at a time;
4. reports which intervention changes task success;
5. writes the complete auditable branch record to JSON.

A valid run must show at least one replay-faithful control branch and at least one causally effective intervention. Those conditions verify the framework's branch-and-replay mechanics only.

## 3. Verify the release

```bash
python scripts/verify_release.py
```

This runs compilation, regression tests, the >=90% package coverage gate, `doctor`, release audit, 500-task lint/oracle validation, and wheel build.

## 4. What this demo does not prove

It does not establish that TraceSurgery improves a frontier model, outperforms another benchmark, or measures causal failures correctly in a nondeterministic desktop environment. Those claims require the external study described in `docs/EXTERNAL_EXECUTION_HANDOFF.md`.
