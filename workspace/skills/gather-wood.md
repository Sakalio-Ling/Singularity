# Skill: Gather Wood

> SK-001 | Status: Template | Version: 0.1

## Description

Find and chop a tree to collect logs. This is a fundamental survival skill.

## Parameters

| Name | Type | Default | Description |
|------|------|---------|-------------|
| wood_type | str | "any" | Type of wood (oak, birch, spruce, jungle, acacia, dark_oak) |
| quantity | int | 10 | Number of logs to collect |

## Preconditions

- Agent is in a world with trees within reasonable distance
- Agent has empty inventory slots (at least 1)
- No immediate hostile mob threat

## Postconditions

- At least `quantity` logs of `wood_type` in inventory
- Some tool durability may be consumed (if using axe)

## Required Items

- None (hand gathering works, but slow)
- Optional: any axe (increases speed significantly)

## Failure Modes

| Failure | Cause | Recovery |
|---------|-------|----------|
| no_trees_nearby | No trees in scan radius | Explore in expanding spiral |
| inventory_full | No empty slots | Drop or store non-essential items |
| hostile_mobs | Mob interference | Defend first, then resume |
| tool_broken | Axe breaks mid-task | Continue with hand or craft new axe |

## Implementation (Action Sequence)

```
1. Scan for nearest tree block (log) within 50-block radius
2. If not found, explore in expanding spiral (10, 20, 30... blocks)
3. Navigate to tree using pathfinder
4. Face the log block
5. Dig the log block
6. Wait for block break + item pickup
7. Repeat steps 4-6 for remaining logs (navigate up trunk or find more trees)
8. Verify inventory count >= quantity
```

## Examples

- "Gather 10 oak logs"
- "Collect some wood for crafting"
- "Get 5 birch logs for building"

## Tests

| Test | Input | Expected | Status |
|------|-------|----------|--------|
| basic_gather | {wood_type:"oak", quantity:1} | 1 oak_log in inventory | Template |
| gather_10 | {wood_type:"any", quantity:10} | 10 logs in inventory | Template |

## Notes

- Trees are the most common wood source in Minecraft
- Punching trees (hand) takes ~4 seconds per log vs ~0.5s with iron axe
- In forest biomes, trees are abundant; in plains/desert, may need to explore
