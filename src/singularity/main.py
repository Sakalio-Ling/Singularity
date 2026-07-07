"""Singularity - Minecraft LLM Agent entry point."""
import sys
import json
import logging
import argparse

from singularity.core.config import Config, BotConfig, LLMConfig


def main():
    parser = argparse.ArgumentParser(description="Singularity Minecraft LLM Agent")
    subparsers = parser.add_subparsers(dest="command", help="Command to run")

    # Run goal command
    run_parser = subparsers.add_parser("run", help="Run a single goal")
    run_parser.add_argument("--goal", type=str, default="Gather 3 oak logs", help="Goal in natural language")
    run_parser.add_argument("--host", type=str, default="localhost")
    run_parser.add_argument("--port", type=int, default=25565)
    run_parser.add_argument("--username", type=str, default="Singularity")
    run_parser.add_argument("--llm-provider", type=str, default="openai")
    run_parser.add_argument("--llm-model", type=str, default="gpt-4o-mini")
    run_parser.add_argument("--api-key", type=str, default="")
    run_parser.add_argument("--log-level", type=str, default="INFO")

    # Benchmark command
    bench_parser = subparsers.add_parser("benchmark", help="Run benchmarks")
    bench_parser.add_argument("--suite", type=str, default="m1", choices=["m1", "m2", "all"])
    bench_parser.add_argument("--host", type=str, default="localhost")
    bench_parser.add_argument("--port", type=int, default=25565)
    bench_parser.add_argument("--username", type=str, default="Singularity")
    bench_parser.add_argument("--llm-provider", type=str, default="openai")
    bench_parser.add_argument("--llm-model", type=str, default="gpt-4o-mini")
    bench_parser.add_argument("--api-key", type=str, default="")
    bench_parser.add_argument("--log-level", type=str, default="INFO")
    bench_parser.add_argument("--output", type=str, default="benchmark_results.json")

    # Legacy: direct goal without subcommand
    parser.add_argument("--goal", type=str, default=None)

    args = parser.parse_args()

    logging.basicConfig(
        level=getattr(logging, (args.log_level if hasattr(args, "log_level") else "INFO").upper()),
        format="%(asctime)s [%(name)s] %(levelname)s: %(message)s",
    )

    host = getattr(args, "host", "localhost")
    port = getattr(args, "port", 25565)
    username = getattr(args, "username", "Singularity")
    provider = getattr(args, "llm_provider", "openai")
    model = getattr(args, "llm_model", "gpt-4o-mini")
    api_key = getattr(args, "api_key", "")

    config = Config(
        bot=BotConfig(host=host, port=port, username=username),
        llm=LLMConfig(provider=provider, model=model, api_key=api_key),
    )

    if args.command == "benchmark":
        from singularity.evaluation.benchmark_runner import BenchmarkRunner
        runner = BenchmarkRunner(config)
        if args.suite == "m1":
            runner.run_m1_suite()
        elif args.suite == "m2":
            runner.run_m2_suite()
        else:
            runner.run_m1_suite()
            runner.run_m2_suite()
        runner.print_summary()
        runner.save_results(args.output)
    else:
        from singularity.core.agent import Agent
        goal = args.goal if args.goal else "Gather 3 oak logs"
        agent = Agent(config)
        if not agent.connect():
            print("Failed to connect to Minecraft server")
            sys.exit(1)
        try:
            result = agent.run_goal(goal)
            print(json.dumps(result, indent=2, default=str))
        finally:
            agent.disconnect()


if __name__ == "__main__":
    main()
