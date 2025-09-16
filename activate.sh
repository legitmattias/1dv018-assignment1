#!/bin/bash
# Script to activate the project environment

echo "Activating assignment1 environment..."

# Source conda configuration first
if [ -f "/home/mattias/miniconda3/etc/profile.d/conda.sh" ]; then
    . "/home/mattias/miniconda3/etc/profile.d/conda.sh"
else
    export PATH="/home/mattias/miniconda3/bin:$PATH"
fi

# Check if conda is available after sourcing
if ! command -v conda &> /dev/null; then
    echo "Error: Conda is not installed or not in PATH"
    echo "Please make sure conda is properly installed and try again"
    return 2>/dev/null || exit 1
fi

# Check if environment exists
if ! conda env list | grep -q "assignment1"; then
    echo "Creating assignment1 environment from environment.yml..."
    conda env create -f environment.yml
fi

# Activate the environment
conda activate assignment1

if [ $? -eq 0 ]; then
    echo "Environment activated! Python: $(python --version)"
    echo "Python path: $(which python)"
    echo ""
    echo "To use this environment in your current shell, run:"
    echo "  source activate.sh"
    echo ""
    echo "Or to start a new shell with this environment:"
    echo "  conda activate assignment1"
else
    echo "Failed to activate assignment1 environment"
    return 2>/dev/null || exit 1
fi
