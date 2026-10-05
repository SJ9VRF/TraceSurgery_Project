# Task Design Standard

A paper-quality task must be stateful, reproducibly initialized, externally gradable, and not solvable by merely emitting a plausible text answer. Each task declares horizon, statefulness and recovery-complexity axes independently.

## Categories
- browser
- documents
- spreadsheets
- email-like sandbox
- filesystem
- multi-app

## Paper target distribution
Browser 90; Documents 70; Spreadsheet 80; Email 60; Files 50; Multi-app 150 = 500 tasks.

## Leakage control
Split by task template family, layout family and data generator seed, not by randomly shuffling near-duplicate task instances. Keep a hidden held-out set for leaderboard evaluation.
