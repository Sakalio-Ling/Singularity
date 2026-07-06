# Model Provider Notes

> Last updated: 2026-07-07

## Supported Providers

| Provider | Models | API | Cost | Notes |
|----------|--------|-----|------|-------|
| OpenAI | GPT-4o, GPT-4o-mini | REST | $2.50-$10/1M tokens | Best structured output |
| Anthropic | Claude 3.5 Sonnet | REST | $3-$15/1M tokens | Strong reasoning |
| DeepSeek | DeepSeek-V3 | REST | $0.14-$0.28/1M tokens | Cost-effective |
| Qwen | Qwen2.5-72B | REST/Local | Varies | Good multilingual |
| Ollama | Llama 3.1, Qwen, etc. | Local | Free (hardware) | For cost-sensitive ops |
| Google | Gemini 1.5 Pro | REST | $1.25-$5/1M tokens | Long context |

## Abstraction Interface

```python
class LLMProvider(ABC):
    @abstractmethod
    def chat(self, messages: list[dict], response_format: dict = None) -> str:
        pass
    
    @abstractmethod
    def count_tokens(self, text: str) -> int:
        pass
    
    @abstractmethod
    def get_model_name(self) -> str:
        pass
```

## Token Budget Strategy

| Task Type | Model | Max Tokens | Rationale |
|-----------|-------|------------|-----------|
| Strategic Planning | GPT-4o / Claude | 4000 | Needs best reasoning |
| Tactical Planning | GPT-4o-mini | 2000 | Structured output |
| Action Selection | GPT-4o-mini | 500 | Fast, frequent |
| Reflection | GPT-4o | 2000 | Needs depth |
| Skill Generation | GPT-4o | 3000 | Code quality matters |
| Memory Compression | GPT-4o-mini | 1000 | Summary task |
| Routine Queries | DeepSeek/Ollama | 500 | Cost savings |

## Key Considerations

- Structured JSON output: OpenAI supports natively, others via prompting
- Rate limits: Different per provider and tier
- Latency: Local models (Ollama) have lowest latency but lower quality
- Failover: Implement provider fallback chain
