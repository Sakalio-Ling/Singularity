# Mineflayer Implementation Notes

> Last updated: 2026-07-07

## Overview

Mineflayer is the primary bot interface. It provides a high-level JavaScript API for controlling a Minecraft player on a server.

## Key APIs

```javascript
// Connection
const bot = mineflayer.createBot({ host, port, username })

// Player state
bot.entity.position      // Vec3 {x, y, z}
bot.health               // 0-20
bot.food                 // 0-20
bot.experience.level     // int
bot.inventory.items()    // array of Item objects

// Block interaction
bot.blockAt(Vec3)        // get block at position
bot.canDigBlock(block)   // check if diggable
bot.dig(block)           // dig a block
bot.placeBlock(reference, face) // place block

// Movement
bot.pathfinder.goto(goal) // navigate to goal
bot.lookAt(Vec3)          // look at position
bot.setControlState(name, state) // movement keys

// Crafting
bot.recipesFor(itemType, metadata, minCount, craftingTable) // find recipes
bot.craft(recipe, count, craftingTable) // craft item

// Entity interaction
bot.attack(entity)       // attack entity
bot.mount(entity)        // mount entity
bot.activateEntity(entity) // interact

// Chat
bot.chat(message)        // send chat message
bot.on('chat', handler)  // listen for chat
```

## Python Bridge Options

### Option A: Subprocess (Simple)
- Launch Node.js script as subprocess
- Communicate via stdin/stdout JSON messages
- Simple but has per-action startup overhead

### Option B: Persistent Socket (Recommended)
- Node.js bot runs as persistent process
- Python connects via TCP/Unix socket or WebSocket
- JSON-RPC style request/response
- Low latency, persistent connection

### Option C: HTTP API
- Node.js bot exposes REST API via Express
- Python calls HTTP endpoints
- Easy to debug but higher latency than socket

**Decision**: Option B (persistent socket) for M1 implementation.

## Known Issues

- prismarine-world chunk loading can be slow in new areas
- pathfinder gets stuck on complex terrain (1-block gaps, water)
- Crafting requires exact recipe knowledge (bot needs recipe DB)
- Entity tracking is limited range (~40 blocks)
