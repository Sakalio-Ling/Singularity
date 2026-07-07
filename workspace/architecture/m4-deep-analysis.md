# M4 Deep Analysis: Autonomous Survival

## Key Challenges
1. Goal generation without human input
2. Resource chain awareness (wood->stone->iron->diamond)
3. Night cycle awareness and shelter timing
4. Combat decision-making (fight vs flee)
5. Multi-step failure recovery

## Implementation Strategy
1. Strategic goal generator: LLM evaluates current inventory and proposes next milestone
2. Resource chain tracker: Maintain dependency graph of items
3. Time monitor: Track day/night cycle, trigger shelter at dusk
4. Combat evaluator: Assess threat level, decide fight/flee/hide
5. State machine: Bootstrap->Resource->Defense->Progression->Exploration

## Open Questions
- How to handle unexpected mob spawns during resource gathering?
- Should agent sleep in bed or wait out the night?
- How to balance exploration vs safety?
- When to abandon current goal for survival?
