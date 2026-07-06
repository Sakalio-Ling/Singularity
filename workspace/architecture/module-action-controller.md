# Module: Action Controller

> Status: Design (M0)
> Owner: Core Agent

## Purpose

Translate structured action plans into validated Minecraft bot commands, with pre-checks, execution monitoring, post-verification, and failure handling.

## Action Lifecycle

```
Plan Action
    |
    v
Pre-Check: Are preconditions met? -> No -> Fail with reason
    |
    v
Execute: Send command to Mineflayer bot
    |
    v
Monitor: Watch for completion, timeout, interruption
    |
    v
Post-Verify: Did expected outcome happen?
    |
    v
Record: Log action, result, duration, state change
```

## Supported Actions (Primitive)

| Action | Mineflayer API | Notes |
|--------|---------------|-------|
| move_to(x,z) | bot.pathfinder.goto() | Uses mineflayer-pathfinder |
| look_at(x,y,z) | bot.lookAt() | |
| dig(x,y,z) | bot.dig(block) | Check block type, tool |
| place(x,y,z,face) | bot.placeBlock(reference, face) | Need reference block |
| craft(item, count) | bot.craft(recipe, count, craftingTable?) | Need recipe + materials |
| smelt(item, count, fuel) | Custom furnace interaction | |
| attack(entity) | bot.attack(entity) | |
| use_item(slot) | bot.activateItem() | |
| open_container(x,y,z) | bot.openContainer(block) | |
| equip(slot, destination) | bot.equip(item, destination) | |
| drop(slot, count) | bot.toss(item) | |
| chat(message) | bot.chat(msg) | |
| wait(ticks) | bot.waitForTicks() | |

## Safety Constraints

1. Never execute actions that would destroy the bot (e.g., walk into lava)
2. Never break blocks that would cause structural collapse without assessment
3. Always check inventory before crafting (prevent wasting materials)
4. Timeout on any single action (default: 30s)
5. Interrupt on health critical (< 4 hearts)
6. All actions logged with before/after state

## Interface

```
execute_action(action: Action, context: WorldState) -> ActionResult {
  action: Action,
  success: bool,
  duration_ms: int,
  state_before: WorldState,
  state_after: WorldState,
  error: str | null,
  retriable: bool
}
```
