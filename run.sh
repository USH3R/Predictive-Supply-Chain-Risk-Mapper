#!/bin/bash

# ----------------------------------------
# US Predictive Supply Chain Risk Mapper
# Run Script
#
# This script:
# 1. Creates a Python virtual environment
# 2. Installs required libraries
# 3. Starts the Dash dashboard
#
# Hackathon goal: one-command startup
# ----------------------------------------

echo "Setting up Python environment..."

# Check if virtual environment exists, create if not
if [ ! -d "venv" ]; then
    python3 -m venv venv
    echo "Virtual environment created."
fi

# Activate virtual environment
source venv/bin/activate

echo "Installing required Python packages..."
pip install --upgrade pip
pip install -r requirements.txt

echo "Starting the Dashboard..."
python app.py
