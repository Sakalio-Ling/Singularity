# Testing Framework

## Test Types
1. **Unit Tests**: Individual module functions (Python pytest)
2. **Integration Tests**: Module interactions (bot + observer + action controller)
3. **Benchmark Tests**: Full agent against fixed-seed tasks
4. **Regression Tests**: Previously passed benchmarks must still pass

## Running Tests
```bash
# Unit tests
python -m pytest tests/unit/ -v

# Integration tests (requires running MC server)
python -m pytest tests/integration/ -v

# Benchmark tests
python -m pytest tests/benchmarks/ -v --benchmark
```

## Test Fixtures
- Mock bot for unit tests (no server needed)
- Fixed seed world for reproducible benchmarks
- Snapshot-based state comparison

## Coverage Goals
- M1: 60% unit test coverage on core modules
- M2: 70% coverage including planner and task system
- M3: 80% coverage including skill library and memory

## CI Pipeline (Future)
1. Lint (ruff/flake8)
2. Type check (mypy)
3. Unit tests
4. Integration tests (if MC server available)
5. Benchmark regression
