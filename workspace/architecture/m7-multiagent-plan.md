# M7: Multi-Agent Collaboration
## Goal
Multiple bots cooperate on shared tasks with role assignment and communication.
## Key Tasks
1. Multi-agent communication protocol (shared memory + message passing)
2. Task decomposition with role assignment
3. Shared world state and memory
4. Conflict resolution (resource contention, path blocking)
5. Collaboration benchmarks (resource gathering, building together)
## Acceptance Criteria
- Two agents complete a resource gathering or building task together
- Communication protocol documented
- Sync failures and conflict resolution logged
- Efficiency improvement over single-agent measured
## Key Challenges
- Communication overhead can negate multi-agent benefits
- Resource contention requires careful scheduling
- Shared memory corruption risk
- Coordination deadlocks
## Research References
- MineCollab, TeamCraft, TickingCollabBench (limited work exists)
- Multi-agent RL literature (more mature but not Minecraft-specific)
## Recommendation
Start with simple leader-follower pattern. Leader plans, follower executes subtasks. Use shared memory for coordination. Avoid complex negotiation protocols initially.
