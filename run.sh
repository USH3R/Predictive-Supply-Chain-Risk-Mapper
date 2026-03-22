#!/bin/bash
# run.sh - US Predictive Supply Chain Risk Mapper
# One-command setup and run

echo "Initializing Python environment..."

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    python3 -m venv venv
    echo "Virtual environment created."
fi

# Activate virtual environment
source venv/bin/activate

# Upgrade pip
pip install --upgrade pip

echo "Installing required Python packages..."
pip install -r requirements.txt

echo "Launching the US Predictive Supply Chain Risk Mapper dashboard..."
# Run the Dash app
python app.py
