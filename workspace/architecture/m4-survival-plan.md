# M4: Autonomous Survival — Planning

## Goal
Agent self-directs survival goals: first-night shelter, resource gathering, tool progression, threat response.

## Key Tasks
1. Strategic goal generator (bootstrapping -> resource chain -> tech tree)
2. Night cycle awareness and shelter strategy
3. Combat/threat response skills
4. Resource inventory management
5. 3+ repeated survival experiments on fixed seeds

## Acceptance Criteria
- Survives first night on fixed seed (3+ experiments)
- Self-proposes next survival goals
- Handles nighttime threats
- Logs success rate and failure types

## Dependencies
- M2 (LLM planning working)
- M3 (skill library + memory working)
- Local Minecraft server operational

## Risks
- Long task chains accumulate errors
- Combat is hard to test deterministically
- Night cycle timing varies by biome
