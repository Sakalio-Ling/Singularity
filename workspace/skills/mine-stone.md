# Skill: Mine Stone

> SK-003 | Status: Template | Version: 0.1

## Description

Mine cobblestone from stone blocks underground or exposed. Requires a pickaxe.

## Parameters

| Name | Type | Default | Description |
|------|------|---------|-------------|
| quantity | int | 20 | Number of cobblestone blocks |

## Preconditions

- Has at least a wooden pickaxe equipped or in inventory
- Stone blocks accessible (underground or exposed cliff)

## Postconditions

- At least `quantity` cobblestone in inventory

## Failure Modes

| Failure | Cause | Recovery |
|---------|-------|----------|
| no_pickaxe | Need pickaxe to mine stone | Craft wooden pickaxe first |
| pickaxe_breaks | Tool durability exhausted | Bring backup pickaxe |
| fall_danger | Mining creates gaps | Place torches, watch footing |
| cave_in | Unsupported blocks | Mine carefully, pillar up |

## Implementation

```
1. Ensure pickaxe is equipped
2. Find stone blocks (y-level 64 and below, or exposed stone)
3. Navigate to stone layer
4. Dig stone blocks -> yields cobblestone
5. Monitor tool durability
6. Return when quantity reached
```

## Notes

- Stone requires wooden pickaxe or better (hand mining yields nothing)
- Best y-level for exposed stone: y=5 to y=63
- Strip mining is more efficient than cave exploration for bulk cobblestone
