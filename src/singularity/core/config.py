"""Configuration for Singularity agent."""
from dataclasses import dataclass, field


@dataclass
class BotConfig:
    host: str = "localhost"
    port: int = 25565
    username: str = "Singularity"
    version: str = "1.20.4"
    auth: str = "offline"


@dataclass
class LLMConfig:
    provider: str = "openai"  # openai, anthropic, deepseek, ollama
    model: str = "gpt-4o-mini"
    api_key: str = ""
    base_url: str = ""
    max_tokens: int = 4096
    temperature: float = 0.7


@dataclass
class Config:
    bot: BotConfig = field(default_factory=BotConfig)
    llm: LLMConfig = field(default_factory=LLMConfig)
    log_dir: str = "logs"
    memory_dir: str = "workspace/memory"
    max_action_timeout: int = 30000  # ms
    health_critical_threshold: float = 4.0  # hearts
