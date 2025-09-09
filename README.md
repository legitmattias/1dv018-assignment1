# Assignment 1 - Algorithms and Data Structures

## Project Overview

This assignment implements and analyzes various algorithms and data structures:

1. **UnionFind algorithms**: Quick Find, Quick Union, Weighted Quick Union, and Weighted Quick Union with Path Compression
2. **3Sum algorithms**: Brute Force (O(N^3)), Optimized Two Pointers (O(N^2)), and Hash Set approach (O(N^2))

## Project Structure

```
assignment_1/
├── src/                          # Source code
│   ├── unionfind.py             # UnionFind implementations
│   └── threesum.py              # 3Sum implementations
├── notebooks/                    # Jupyter notebooks
│   ├── algorithm_analysis.ipynb # Comprehensive performance analysis
│   └── eploration/              # Testing and exploration
│       └── big_o_complexity.ipynb
├── activate.sh                   # Environment activation script
├── environment.yml              # Conda environment configuration
├── pyproject.toml               # Project configuration
└── README.md                    # This file
```

## Environment Setup

This project uses a conda environment for dependency management.

### Quick Start

```bash
# Option 1: Use the activation script
./activate.sh

# Option 2: Manual activation
conda env create -f environment.yml  # First time only
conda activate assignment1

# Option 3: Use direnv (if installed)
direnv allow
```

### Environment Details

- **Environment Name**: `assignment1`
- **Python Version**: 3.12.11
- **Configuration**: `environment.yml`

### Required Packages

- **Data Analysis**: numpy, pandas, matplotlib, seaborn
- **Jupyter**: jupyter, ipykernel
- **Code Quality**: ruff, black, mypy

## Running the Project

### Running Individual Algorithms

```bash
# Test UnionFind implementations
python src/unionfind.py

# Test 3Sum implementations
python src/threesum.py
```

### Running Analysis Notebooks

```bash
# Start Jupyter Lab
jupyter lab

# Navigate to notebooks/algorithm_analysis.ipynb for comprehensive analysis
# Use notebooks/eploration/big_o_complexity.ipynb for quick testing
```

### Code Quality

```bash
# Run linting
ruff check src/

# Format code
black src/
```

## Algorithm Implementations

### UnionFind Algorithms

- **QuickFind**: O(N) union, O(1) find
- **QuickUnion**: O(N) union, O(N) find (worst case)
- **WeightedQuickUnion**: O(log N) union, O(log N) find
- **WeightedQuickUnionPathCompression**: O(α(N)) union, O(α(N)) find

### 3Sum Algorithms

- **Brute Force**: O(N^3) time, O(1) space
- **Two Pointers**: O(N^2) time, O(1) space
- **Hash Set**: O(N^2) time, O(N) space

## Performance Analysis

The `notebooks/algorithm_analysis.ipynb` contains comprehensive performance analysis including:
- Empirical timing measurements
- Complexity analysis
- Performance comparisons
- Theoretical vs empirical results

## Quick Test

```bash
# Test that everything works
conda activate assignment1
python -c "import sys; sys.path.append('src'); from unionfind import QuickFind; from threesum import three_sum_brute_force; print('All algorithms work!')"
```

## Troubleshooting

If you get "command not found" errors:
1. Make sure conda is installed
2. Run `conda init` and restart your terminal
3. Use `./activate.sh` to activate the environment
