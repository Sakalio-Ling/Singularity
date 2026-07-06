"""Singularity — Minecraft LLM Agent entry point."""
import sys
import json
import logging
import argparse

from singularity.core.config import Config, BotConfig, LLMConfig
from singularity.core.agent import Agent


def main():
    parser = argparse.ArgumentParser(description="Singularity Minecraft LLM Agent")
    parser.add_argument("--goal", type=str, default="Gather 3 oak logs", help="Goal in natural language")
    parser.add_argument("--host", type=str, default="localhost", help="MC server host")
    parser.add_argument("--port", type=int, default=25565, help="MC server port")
    parser.add_argument("--username", type=str, default="Singularity", help="Bot username")
    parser.add_argument("--llm-provider", type=str, default="openai", help="LLM provider")
    parser.add_argument("--llm-model", type=str, default="gpt-4o-mini", help="LLM model")
    parser.add_argument("--api-key", type=str, default="", help="LLM API key (or set OPENAI_API_KEY env)")
    parser.add_argument("--log-level", type=str, default="INFO", help="Log level")
    args = parser.parse_args()

    logging.basicConfig(
        level=getattr(logging, args.log_level.upper()),
        format="%(asctime)s [%(name)s] %(levelname)s: %(message)s",
    )

    config = Config(
        bot=BotConfig(host=args.host, port=args.port, username=args.username),
        llm=LLMConfig(provider=args.llm_provider, model=args.llm_model, api_key=args.api_key),
    )

    agent = Agent(config)

    if not agent.connect():
        print("Failed to connect to Minecraft server")
        sys.exit(1)

    try:
        result = agent.run_goal(args.goal)
        print(json.dumps(result, indent=2, default=str))
    finally:
        agent.disconnect()


if __name__ == "__main__":
    main()
