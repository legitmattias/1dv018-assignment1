# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is an academic assignment implementing and analyzing algorithms and data structures:
- **UnionFind algorithms**: 4 implementations with different performance characteristics
- **3Sum algorithms**: 3 implementations with varying time/space complexity trade-offs

## Environment Setup

The project uses conda for dependency management with Python 3.12.11.

### Environment Activation
```bash
# Quick activation
./activate.sh

# Manual activation
conda activate assignment1
```

## Common Commands

### Running Code
```bash
# Test UnionFind implementations
python src/unionfind.py

# Test 3Sum implementations  
python src/threesum.py

# Start Jupyter Lab for analysis notebooks
jupyter lab
```

### Code Quality
```bash
# Lint and format code
./lint.sh

# Or manually:
ruff check . --fix
ruff format .

# Type checking
mypy src/
```

## Code Architecture

### Core Implementations (`src/`)

**UnionFind (`src/unionfind.py`)**:
- `QuickFind`: O(N) union, O(1) find
- `QuickUnion`: O(N) union/find worst case
- `WeightedQuickUnion`: O(log N) union/find
- `WeightedQuickUnionPathCompression`: O(α(N)) union/find

All classes implement: `union(p, q)`, `find(p)`, `connected(p, q)`, `count_components()`

**3Sum (`src/threesum.py`)**:
- `three_sum_brute_force()`: O(N^3) time, O(1) space
- `three_sum_optimized()`: O(N^2) time using two pointers
- `three_sum_optimized_with_hash()`: O(N^2) time, O(N) space

### Performance Analysis (`notebooks/`)

**Primary notebook**: `algorithm_analysis.ipynb` - comprehensive performance analysis using `%timeit` for precise measurements
- UnionFind timing across different N values (100-5000 elements)
- 3Sum timing across different array sizes (50-1000 elements)
- Performance visualizations (linear and log-log plots)
- Both best and average timing results

**Analysis notes**: `algorithm_analysis_notes.md` - detailed function documentation and theoretical vs. empirical analysis

**Exploration**: `notebooks/exploration/big_o_complexity.ipynb` - quick testing and experimentation

## Development Workflow

1. Activate environment: `./activate.sh`
2. Run individual algorithms to test: `python src/{module}.py`
3. Use Jupyter notebooks for analysis: `jupyter lab`
4. Lint/format before committing: `./lint.sh`

## Key Design Patterns

- All algorithm classes follow consistent interfaces
- Built-in test functions demonstrate usage
- Performance measurement using `%timeit` for precision
- Setup functions for clean timing measurements
- Comprehensive docstrings with complexity analysis
- Type hints throughout codebase
- Separate analysis documentation for insights

## Configuration

- **Ruff**: Configured in `pyproject.toml` with Python 3.12 target
- **Environment**: Full dependency specification in `environment.yml`
- **Code style**: Line length 88, automatic import sorting