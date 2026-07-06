# Skill: Smelt Iron
> SK-005 | Status: Template | Version: 0.1
## Description
Smelt raw iron into iron ingots using a furnace.
## Parameters
| Name | Type | Default |
|------|------|---------|
| quantity | int | 8 |
| fuel | str | "coal" |
## Preconditions: raw_iron in inventory, fuel available, furnace accessible
## Postconditions: iron_ingot in inventory
## Implementation
1. Ensure furnace available (craft from 8 cobblestone if needed)
2. Place furnace
3. Open furnace GUI
4. Place raw iron in input slot
5. Place fuel in fuel slot
6. Wait for smelting (10s per item)
7. Collect iron ingots
## Notes: Each iron ore yields 1 iron ingot. Coal smelts 8 items per piece.
