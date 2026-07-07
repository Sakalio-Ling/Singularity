"""Benchmark runner for Singularity M1-M2 validation."""
import json
import time
import logging
from dataclasses import dataclass, field
from typing import Optional

from singularity.core.config import Config, BotConfig, LLMConfig
from singularity.core.agent import Agent

logger = logging.getLogger("singularity.benchmark")


@dataclass
class BenchmarkTask:
    id: str
    name: str
    goal: str
    phase: str
    timeout_cycles: int = 100
    success_criteria: dict = field(default_factory=dict)
    min_inventory: dict = field(default_factory=dict)


M1_BENCHMARKS = [
    BenchmarkTask("BM-001", "Chop 3 oak logs", "Gather 3 oak logs", "M1",
                  timeout_cycles=50, success_criteria={"oak_log": 3}, min_inventory={"oak_log": 3}),
    BenchmarkTask("BM-002", "Craft workbench", "Craft a crafting table", "M1",
                  timeout_cycles=30, success_criteria={"crafting_table": 1}, min_inventory={"oak_planks": 4}),
    BenchmarkTask("BM-003", "Craft wooden pickaxe", "Craft a wooden pickaxe", "M1",
                  timeout_cycles=60, success_criteria={"wooden_pickaxe": 1}, min_inventory={"oak_planks": 3, "stick": 2}),
    BenchmarkTask("BM-004", "Mine cobblestone", "Mine 3 cobblestone blocks", "M1",
                  timeout_cycles=40, success_criteria={"cobblestone": 3}),
    BenchmarkTask("BM-005", "Craft stone tools", "Craft a stone pickaxe", "M1",
                  timeout_cycles=80, success_criteria={"stone_pickaxe": 1}),
]

M2_BENCHMARKS = [
    BenchmarkTask("BM-006", "Gather wood and craft workbench", "Gather oak wood and craft a crafting table", "M2",
                  timeout_cycles=80, success_criteria={"crafting_table": 1}),
    BenchmarkTask("BM-007", "Wooden pickaxe + cobblestone", "Craft a wooden pickaxe and mine 3 cobblestone", "M2",
                  timeout_cycles=120, success_criteria={"cobblestone": 3}),
    BenchmarkTask("BM-008", "Stone tool progression", "Craft stone pickaxe and stone axe", "M2",
                  timeout_cycles=150, success_criteria={"stone_pickaxe": 1, "stone_axe": 1}),
    BenchmarkTask("BM-009", "Gather and store", "Gather 16 oak logs and store in a chest", "M2",
                  timeout_cycles=200, success_criteria={"oak_log": 16}),
    BenchmarkTask("BM-010", "Night survival prep", "Build a shelter and craft a bed before nightfall", "M2",
                  timeout_cycles=300, success_criteria={"bed": 1}),
]


@dataclass
class BenchmarkResult:
    task_id: str
    task_name: str
    status: str  # pass, fail, timeout, error
    cycles_used: int = 0
    duration_s: float = 0.0
    inventory_snapshot: dict = field(default_factory=dict)
    error: str = ""
    session_log_path: str = ""


class BenchmarkRunner:
    """Runs benchmark tasks against the agent and records results."""

    def __init__(self, config: Config, output_dir: str = "logs/benchmarks"):
        self.config = config
        self.output_dir = output_dir
        self.results: list[BenchmarkResult] = []

    def run_task(self, task: BenchmarkTask) -> BenchmarkResult:
        """Run a single benchmark task."""
        logger.info(f"Running benchmark {task.id}: {task.name}")
        agent = Agent(self.config)
        start = time.time()

        if not agent.connect():
            return BenchmarkResult(task.id, task.name, "error", error="Connection failed")

        try:
            result = agent.run_goal(task.goal)
            duration = time.time() - start
            inventory = agent.bot.get_inventory()
            inv_summary = {}
            for item in inventory:
                name = item.get("name", "unknown")
                inv_summary[name] = inv_summary.get(name, 0) + item.get("count", 1)

            passed = self._check_success(inv_summary, task.success_criteria)
            status = "pass" if passed else "fail"

            bench_result = BenchmarkResult(
                task_id=task.id, task_name=task.name, status=status,
                cycles_used=result.get("cycles", 0), duration_s=round(duration, 2),
                inventory_snapshot=inv_summary,
                session_log_path=result.get("summary", {}).get("log_path", ""),
            )
        except Exception as e:
            bench_result = BenchmarkResult(task.id, task.name, "error", error=str(e))
        finally:
            agent.disconnect()

        self.results.append(bench_result)
        logger.info(f"  {task.id}: {bench_result.status} ({bench_result.duration_s}s, {bench_result.cycles_used} cycles)")
        return bench_result

    def run_suite(self, tasks: list[BenchmarkTask]) -> list[BenchmarkResult]:
        """Run a suite of benchmark tasks."""
        results = []
        for task in tasks:
            result = self.run_task(task)
            results.append(result)
        return results

    def run_m1_suite(self) -> list[BenchmarkResult]:
        return self.run_suite(M1_BENCHMARKS)

    def run_m2_suite(self) -> list[BenchmarkResult]:
        return self.run_suite(M2_BENCHMARKS)

    def _check_success(self, inventory: dict, criteria: dict) -> bool:
        for item, count in criteria.items():
            if inventory.get(item, 0) < count:
                return False
        return True

    def save_results(self, filename: str = "benchmark_results.json"):
        import os
        os.makedirs(self.output_dir, exist_ok=True)
        path = os.path.join(self.output_dir, filename)
        data = []
        for r in self.results:
            data.append({
                "task_id": r.task_id, "task_name": r.task_name, "status": r.status,
                "cycles": r.cycles_used, "duration_s": r.duration_s,
                "inventory": r.inventory_snapshot, "error": r.error,
                "log": r.session_log_path,
            })
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        logger.info(f"Results saved to {path}")

    def print_summary(self):
        total = len(self.results)
        passed = sum(1 for r in self.results if r.status == "pass")
        failed = sum(1 for r in self.results if r.status == "fail")
        errors = sum(1 for r in self.results if r.status == "error")
        print(f"\nBenchmark Summary: {passed}/{total} passed, {failed} failed, {errors} errors")
        for r in self.results:
            icon = "+" if r.status == "pass" else "x" if r.status == "fail" else "!"
            print(f"  [{icon}] {r.task_id} {r.task_name}: {r.status} ({r.duration_s}s)")
