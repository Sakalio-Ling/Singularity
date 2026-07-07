# M7: Multi-Agent Collaboration - Implementation Plan

## Overview
Enable multiple Minecraft bots to cooperate on shared tasks with role assignment, communication, and conflict resolution.

## Architecture

### Communication Protocol
Two approaches to evaluate:

**Approach A: Shared Memory (Simple)**
- All agents read/write a shared JSON file or in-memory store
- Agents poll shared state at regular intervals
- Pros: Simple, no networking complexity
- Cons: Race conditions, no direct messaging

**Approach B: Message Passing (Scalable)**
- Agents send structured messages via TCP/IPC
- Message types: task_request, task_complete, resource_need, status_update
- Pros: Real-time, decoupled
- Cons: More complex, message ordering issues

**Recommendation**: Start with Approach A for M7 prototype, evaluate B later.

### Role Assignment
```
Leader Agent:
  - Observes world state
  - Decomposes tasks into subtasks
  - Assigns roles (gatherer, builder, miner, defender)
  - Monitors progress and reassigns as needed

Worker Agent(s):
  - Execute assigned subtasks
  - Report status back to leader
  - Request help when stuck
```

### Conflict Resolution
- **Resource contention**: Leader assigns exclusive resource zones
- **Path blocking**: Agents yield to higher-priority traffic
- **Task overlap**: Leader prevents duplicate task assignment
- **Deadlock detection**: Timeout-based with role reassignment

### Shared World State
- Each agent broadcasts position, inventory, health every 5s
- Leader maintains aggregate state for planning
- Workers query shared state for nearby teammate locations

## Implementation Steps

### Step 1: Multi-Agent Bridge
Modify bot_server.js to support multiple named bot instances on different bridge ports (3001, 3002, etc.)

### Step 2: Shared State Protocol
Create `src/singularity/multi_agent/shared_state.py`:
- File-based shared state with locking
- Position/inventory/health broadcasting
- Role assignment storage

### Step 3: Leader Agent
Extend Agent class with leader capabilities:
- Task decomposition with role assignment
- Worker status monitoring
- Resource zone allocation

### Step 4: Worker Agent
Extend Agent class with worker capabilities:
- Accept and execute assigned subtasks
- Status reporting to leader
- Help requests when blocked

### Step 5: Conflict Resolution
Implement timeout-based deadlock detection and role reassignment.

## Acceptance Criteria
- [ ] Two agents connected simultaneously to same MC server
- [ ] Leader assigns gatherer and builder roles
- [ ] Both agents complete assigned subtasks
- [ ] Resource contention handled without deadlock
- [ ] Efficiency improvement over single-agent measured
