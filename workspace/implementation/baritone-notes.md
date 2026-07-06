# Baritone Implementation Notes

> Last updated: 2026-07-07

## Overview

Baritone is a Minecraft pathfinding mod written in Java. It provides A* pathfinding and automated gameplay features.

## Key Features

- A* pathfinding with sophisticated heuristics
- Automatic block breaking/placing during pathfinding
- Goal types: GoalBlock, GoalNear, GoalXZ, GoalY, GoalAxis
- Mine and build automation
- Sprint and parkour movement

## Integration Options

### Option A: Mineflayer Plugin
Use mineflayer-pathfinder which implements similar A* pathfinding in JavaScript. This is the primary approach.

### Option B: Server Plugin
Run Baritone as a Fabric/Forge mod on the server. Bot controls Baritone via chat commands or custom API.

### Option C: Standalone
Use Baritone's Java API directly from a Java-based bot.

## Decision

Primary: Use mineflayer-pathfinder (Option A) for M1-M5. Evaluate Baritone (Option B) only if pathfinding quality is insufficient.

## License Concern

Baritone is LGPL-3.0. This means:
- Can use as-is (linking OK)
- Modifications to Baritone itself must be shared
- Our agent code does NOT need to be LGPL
- Be careful about static linking

## Version Compatibility

- Baritone 1.20.4: Available via Fabric
- API changes between versions are common
- Pin exact version for experiments
