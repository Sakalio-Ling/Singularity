# Skill: Build Shelter
> SK-006 | Status: Template | Version: 0.1
## Description
Build a simple shelter to survive the night.
## Parameters
| Name | Type | Default |
|------|------|---------|
| size | str | "5x5" |
| material | str | "any" |
## Preconditions: Building blocks in inventory (dirt, wood, cobblestone)
## Postconditions: Enclosed structure with door
## Implementation
1. Select flat area near current position
2. Clear area if needed
3. Build walls (5x5, 3 blocks high)
4. Place door
5. Place torch inside for light
6. Verify enclosure (no gaps for mobs)
## Notes: Dirt and wood are fastest to gather. Cobblestone is more durable. Add roof to prevent spider climbing.
