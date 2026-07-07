# Error Handling Guide

## Error Categories
| Category | Examples | Recovery |
|----------|----------|----------|
| Connection | Bot disconnected, server restart | Auto-reconnect with backoff |
| Action | Dig failed, craft failed | Log + reflect + retry or alternative |
| Pathfinding | No path found, stuck | Retry with different goal or manual movement |
| LLM | JSON parse error, hallucination | Retry with stricter prompt |
| Inventory | Full inventory, missing item | Drop/store items, gather missing |
| Combat | Taking damage, mob swarm | Flee + heal + retry |
| Environment | Lava, void, suffocation | Emergency teleport or respawn |

## Retry Strategy
- Max 3 retries per action
- Exponential backoff: 1s, 2s, 4s
- After 3 failures: trigger reflection, try alternative approach
- After 5 consecutive failures: pause and request human help

## Error Logging Format
```json
{
  "timestamp": "ISO-8601",
  "level": "ERROR",
  "category": "action",
  "action": {"type": "dig", "parameters": {}},
  "error": "Block not found",
  "world_state_snapshot": {},
  "retry_count": 1,
  "resolution": "retried with updated coordinates"
}
```
