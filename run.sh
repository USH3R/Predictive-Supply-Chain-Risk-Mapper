#!/bin/bash
# run.sh - US Predictive Supply Chain Risk Mapper
# Sets up environment, installs packages, and runs the app

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

# Install all required Python packages
echo "Installing required Python packages..."
pip install -r requirements.txt

# Launch the Dash app
echo "Launching the US Predictive Supply Chain Risk Mapper dashboard..."
# Using host=0.0.0.0 so Codespaces can forward the port
python app.py
