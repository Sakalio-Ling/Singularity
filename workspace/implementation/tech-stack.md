# Tech Stack — Implementation Notes

> Last updated: 2026-07-07

## Core Stack

| Component | Choice | Version | Notes |
|-----------|--------|---------|-------|
| Agent Language | Python | 3.11+ | Main agent logic, LLM integration |
| Minecraft Bot | Mineflayer (Node.js) | 4.x | Primary action interface |
| Pathfinding | mineflayer-pathfinder | 2.x | Navigation plugin for Mineflayer |
| Minecraft Server | Paper | 1.20.4 | Local private server |
| LLM Backend | OpenAI / Anthropic / DeepSeek | Various | Swappable via abstract interface |
| Local LLM | Ollama | Latest | For cost-sensitive operations |
| Memory Storage | Markdown + JSON | N/A | Phase 1; evaluate SQLite/vector DB later |
| Logging | Python logging + JSON | N/A | Structured logs for all operations |

## Python Dependencies (Planned)

```
openai>=1.0
anthropic>=0.20
httpx
pydantic>=2.0
rich
jsonlines
```

## Node.js Dependencies (Planned)

```
mineflayer@^4.0.0
mineflayer-pathfinder@^2.0.0
prismarine-viewer (optional, debugging)
```

## Communication Architecture

```
Python Agent  <--(stdio/socket)-->  Node.js Mineflayer Bot
     |
     +-->(HTTP)--> LLM API (OpenAI/Anthropic/DeepSeek)
     |
     +-->(filesystem)--> Memory (markdown/JSON)
     |
     +-->(filesystem)--> Logs (JSON lines)
```

## Development Environment

- OS: Windows (primary), Linux (server)
- IDE: Any (VSCode recommended)
- Git: Version control for all code and research docs
- Docker: Optional for Minecraft server containerization
