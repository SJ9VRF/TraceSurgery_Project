# Metrics

## Outcome
- Task Success Rate
- Success@k
- Cost per Successful Task
- Latency per Successful Task

## Failure dynamics
- First-Failure Position = first failure step / trajectory length
- Failure Count
- Root Failure Count
- Error Propagation Depth
- Failure Cascade Size
- State Divergence Duration
- Failure Detection Latency

## Recovery
- Recoverable Failure Rate
- Recovery Rate
- Recovery Efficiency
- Recovery Cost (steps, tokens, wall time, dollars)
- Recovery Window Length
- Recoverability Half-Life (estimated from recovery probability vs delay)
- Point-of-No-Return Position

## Safety
- Catastrophic Action Rate
- Irreversible Action Rate
- Unintended Side-Effect Rate
- Constraint Violation Rate
- Unsafe Recovery Rate

Every aggregate result should report uncertainty (bootstrap confidence intervals by task, with task as the resampling unit where appropriate).
