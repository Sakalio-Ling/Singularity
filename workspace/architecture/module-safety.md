# Module: Safety System

> Status: Design (M0)
> Owner: Core Agent

## Purpose

Enforce safety boundaries for all agent actions, prevent dangerous operations, and maintain audit trails.

## Safety Layers

### Layer 1: Action Schema Validation
- All LLM outputs validated against JSON schema before execution
- Unknown action types are rejected
- Parameter types and ranges are checked

### Layer 2: Pre-Condition Guards
- Check game state before each action
- Prevent: self-damage, resource waste, structural destruction, infinite loops
- Block: actions on protected areas, actions requiring unavailable items

### Layer 3: Execution Monitoring
- Timeout on all actions (30s default)
- Health monitoring (abort if health < 4 hearts)
- Interrupt on external signal (human override)

### Layer 4: Post-Condition Verification
- Verify expected outcome happened
- If mismatch: log, reflect, re-plan or abort

### Layer 5: Audit Trail
- Every action logged with: timestamp, action, parameters, pre-state, post-state, result
- Every LLM interaction logged with: prompt, response, token count
- Logs are immutable and append-only

## Forbidden Operations

| Operation | Reason | Exception |
|-----------|--------|-----------|
| Execute arbitrary system commands | Security | Never allowed |
| Connect to public Minecraft servers | Safety/ethics | Never allowed |
| Break bedrock or server structures | Game integrity | Never allowed |
| Infinite loops without exit condition | Resource waste | Must have timeout |
| Actions that delete MEMORY.md | Data protection | Never allowed |
| Bypass server rules or anti-cheat | Ethics | Never allowed |

## Human Override Protocol

At any point, a human can:
- `pause` — Agent stops all actions, maintains state
- `resume` — Agent continues from paused state
- `stop` — Agent stops current task, returns to idle
- `abort` — Agent stops everything, saves state, shuts down
- `override <action>` — Agent executes specific human-specified action

## Interface

```
validate_action(action: Action, world_state: WorldState) -> (bool, str | None)
check_preconditions(action: Action, state: WorldState) -> (bool, str | None)
check_postconditions(action: Action, before: WorldState, after: WorldState) -> (bool, str | None)
log_audit(entry: AuditEntry) -> None
request_human_override(reason: str) -> HumanDecision
```
