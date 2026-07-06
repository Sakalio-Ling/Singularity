"""LLM provider abstraction — supports OpenAI, Anthropic, DeepSeek, and local models via Ollama."""
import json
import logging
from typing import Optional

from singularity.core.config import LLMConfig

logger = logging.getLogger("singularity.llm")


class LLMProvider:
    """Swappable LLM backend that supports multiple providers."""

    def __init__(self, config: LLMConfig):
        self.config = config
        self._client = None
        self._init_client()

    def _init_client(self):
        provider = self.config.provider.lower()
        if provider == "openai":
            import openai
            kwargs = {"api_key": self.config.api_key}
            if self.config.base_url:
                kwargs["base_url"] = self.config.base_url
            self._client = openai.OpenAI(**kwargs)
        elif provider == "anthropic":
            import anthropic
            self._client = anthropic.Anthropic(api_key=self.config.api_key)
        elif provider == "ollama":
            import openai
            self._client = openai.OpenAI(
                base_url=self.config.base_url or "http://localhost:11434/v1",
                api_key="ollama",
            )
        else:
            raise ValueError(f"Unknown LLM provider: {provider}")

    def chat(self, messages: list[dict], response_format: Optional[dict] = None) -> str:
        """Send a chat completion request and return the response text."""
        provider = self.config.provider.lower()
        logger.debug(f"LLM call ({provider}): {len(messages)} messages")

        if provider in ("openai", "ollama"):
            kwargs = {
                "model": self.config.model,
                "messages": messages,
                "max_tokens": self.config.max_tokens,
                "temperature": self.config.temperature,
            }
            if response_format and provider == "openai":
                kwargs["response_format"] = response_format
            response = self._client.chat.completions.create(**kwargs)
            text = response.choices[0].message.content or ""
        elif provider == "anthropic":
            # Anthropic uses a different message format
            system_msg = ""
            user_messages = []
            for msg in messages:
                if msg["role"] == "system":
                    system_msg = msg["content"]
                else:
                    user_messages.append(msg)
            response = self._client.messages.create(
                model=self.config.model,
                max_tokens=self.config.max_tokens,
                system=system_msg,
                messages=user_messages,
            )
            text = response.content[0].text if response.content else ""
        else:
            raise ValueError(f"Unsupported provider: {provider}")

        logger.debug(f"LLM response: {text[:200]}")
        return text
