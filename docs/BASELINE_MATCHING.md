# Baseline matching protocol

Comparisons must hold constant: base model/version, observation modality, tool schema, task set, seed schedule, max environment steps, context/token budget, temperature/sampling settings, and access to external memory. Report any unavoidable mismatch.

Required interventions on the same base model:
- reactive baseline
- retry-only
- reflection-only
- structured memory
- explicit verifier
- oracle failure-detection upper bound
- oracle recovery-point upper bound

For recovery methods, report both end-to-end task success and conditional recovery success on the *same injected failures*. This prevents gains from easier failure distributions being misread as better recovery.
