# Experiment Index

> Last updated: 2026-07-07
> Format: EXP-NNNN-title.md per experiment

## Experiment Registry

| ID | Title | Status | Phase | Date |
|----|-------|--------|-------|------|
| EXP-0001 | Mineflayer Connectivity Test | Planned | M1 | - |
| EXP-0002 | Observation Module Latency | Planned | M1 | - |
| EXP-0003 | Primitive Action Reliability | Planned | M1 | - |
| EXP-0004 | LLM Planning Quality | Planned | M2 | - |
| EXP-0005 | Python-Node.js Bridge Benchmark | Planned | M1 | - |

## Experiment Template

Each experiment file follows this structure:

```
# EXP-NNNN: Title

## Metadata
- Date:
- Phase:
- Hypothesis:

## Setup
- Minecraft version:
- Server type:
- Bot version:
- LLM model:
- World seed:

## Procedure
1. ...
2. ...

## Results
- Metric 1:
- Metric 2:

## Analysis
- ...

## Conclusion
- Hypothesis supported/refuted
- Next steps
```

## Notes

- All experiments must be reproducible (fixed seeds, pinned versions)
- Minimum 3 repetitions before claiming stability
- Record both successes and failures
