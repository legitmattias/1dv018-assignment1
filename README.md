# Assignment 1 - Algorithms and Data Structures

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

### Running the Project

```bash
# Start Jupyter Lab
jupyter lab

# Run linting
ruff check eploration/

# Format code
black eploration/
```

### Troubleshooting

If you get "command not found" errors:
1. Make sure conda is installed
2. Run `conda init` and restart your terminal
3. Use `./activate.sh` to activate the environment
