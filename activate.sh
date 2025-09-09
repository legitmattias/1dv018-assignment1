#!/bin/bash
# Script to activate the project environment

echo "Activating assignment1 environment..."

# Check if conda is available
if ! command -v conda &> /dev/null; then
    echo "Error: Conda is not installed or not in PATH"
    exit 1
fi

# Check if environment exists
if ! conda env list | grep -q "assignment1"; then
    echo "Creating assignment1 environment from environment.yml..."
    conda env create -f environment.yml
fi

# Activate the environment
source ~/miniconda3/etc/profile.d/conda.sh
conda activate assignment1

echo "Environment activated! Python: $(python --version)"
echo "Python path: $(which python)"
