# Skill: Craft Tools

> SK-002 | Status: Template | Version: 0.1

## Description

Craft basic tools from available materials (wooden, stone, iron tiers).

## Parameters

| Name | Type | Default | Description |
|------|------|---------|-------------|
| tool_type | str | required | pickaxe, axe, shovel, sword, hoe |
| material | str | "best_available" | wood, stone, iron, gold, diamond |
| quantity | int | 1 | Number of tools to craft |

## Preconditions

- Sufficient raw materials (planks, cobblestone, iron_ingot, etc.)
- Crafting table available (for pickaxe, axe, shovel)
- Knows recipe for target tool

## Postconditions

- Tool in inventory
- Materials consumed

## Failure Modes

| Failure | Cause | Recovery |
|---------|-------|----------|
| missing_materials | Not enough resources | Gather more resources first |
| no_crafting_table | Need 3x3 grid | Place or find crafting table |
| wrong_recipe | Unknown recipe | Look up recipe in knowledge base |

## Implementation (Action Sequence)

```
1. Check inventory for required materials
2. If materials missing, request gather/craft subtask
3. If crafting table needed and not available, craft one (4 planks)
4. Open crafting table (or use 2x2 grid for basic items)
5. Select correct recipe
6. Craft tool
7. Verify tool in inventory
```

## Recipe Reference

| Tool | Recipe | Materials |
|------|--------|-----------|
| Wooden Pickaxe | S/S/ | 3 planks + 2 sticks |
| Stone Pickaxe | C/C/ | 3 cobblestone + 2 sticks |
| Iron Pickaxe | I/I/ | 3 iron_ingot + 2 sticks |
| Wooden Axe | SS/S./ | 3 planks + 2 sticks |
| Stone Axe | CC/C./ | 3 cobblestone + 2 sticks |
| Iron Axe | II/I./ | 3 iron_ingot + 2 sticks |

## Notes

- Always craft best available material tier
- Axe is priority 1 (faster wood gathering), pickaxe is priority 2 (mine stone/ore)
