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
│   ├── reports/                 # Exported notebook runs
│   └── exploration/             # Personal testing (not part of assignment)
│       └── big_o_complexity.ipynb
├── screenshots/                  # Performance analysis visualizations
│   ├── output-graphs01.png      # Initial analysis results
│   ├── output-graphs02.png      # Updated analysis (workshop methodology)
│   ├── output-graphs03.png      # Extended analysis results
│   ├── output-graphs04_curve-fit.png # Curve-fit analysis visualization
│   ├── 3sum.png                 # 3Sum algorithm performance
│   └── unionfind.png            # UnionFind algorithm performance
├── assignment1_report.md         # Assignment report
├── code_implementation_guide.md  # Implementation documentation
├── activate.sh                   # Environment activation script
├── lint.sh                      # Code quality script
├── environment.yml              # Conda environment configuration
├── pyproject.toml               # Project configuration
├── requirements.txt             # Python package requirements
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
python3 src/unionfind.py

# Test 3Sum implementations
python3 src/threesum.py
```

### Running Analysis Notebooks

```bash
# Start Jupyter Lab
jupyter lab

# Navigate to notebooks/algorithm_analysis.ipynb for comprehensive analysis
```

### Code Quality

```bash
# Run linting and formatting (recommended)
./lint.sh

# Manual linting and formatting
ruff check . --fix
ruff format .

# Type checking
mypy src/
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

### Comprehensive Analysis

The `notebooks/algorithm_analysis.ipynb` contains comprehensive performance analysis including:
- **%timeit precision measurements** for accurate timing
- **Slope verification** to confirm theoretical complexity
- **Scaled testing**: UnionFind (N=1K-100K), 3Sum (separate ranges for different algorithms)
- **Visual comparisons** with both linear and log-log plots

### Key Findings

**UnionFind Results:**
- Quick Find: Perfect O(N) scaling (slope = 1.00)
- Quick Union: Catastrophic O(N²) degradation (slope = 2.07, 25+ seconds at N=100K)
- Weighted algorithms: Excellent O(log N) performance maintaining sub-second execution

**3Sum Results:**
- Brute Force: Perfect O(N³) validation (slope = 3.13)
- Two Pointers: Near-linear optimization (slope = 0.99)
- Hash Set: Solid O(N²) behavior (slope = 2.35)

### Documentation

- **`assignment1_report.md`**: Complete assignment report with analysis and findings
- **`code_implementation_guide.md`**: Detailed implementation documentation and notebook structure
- **`notebooks/reports/`**: Exported HTML reports from notebook runs
- **`screenshots/`**: Performance visualization graphs showing scaling behavior and curve-fit analysis

## Quick Test

```bash
# Test that everything works
./activate.sh
python3 -c "import sys; sys.path.append('src'); from unionfind import QuickFind; from threesum import three_sum_brute_force; print('All algorithms work!')"

# Run full performance analysis (takes several minutes due to large datasets)
jupyter lab notebooks/algorithm_analysis.ipynb
```

## Troubleshooting

If you get "command not found" errors:
1. Make sure conda is installed
2. Run `conda init` and restart your terminal
3. Use `./activate.sh` to activate the environment
