# Provider / Real-Environment Adapter Contract

Real model integrations should implement `Agent.act(observation, step) -> Action`. Real desktop/browser integrations should implement `Environment.reset`, `step`, `snapshot`, and `is_terminal`.

Do not leak benchmark ground-truth state into the agent observation. `snapshot()` is for graders/logging only. Keep observation and privileged state physically separated in adapter code.

Recommended adapters:
- browser automation / BrowserGym-style environment
- OSWorld-compatible desktop adapter
- isolated document/spreadsheet/email/file sandboxes

Store exact model version, environment version, agent commit, seed, grader version and perturbation seed with each trial.
