#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

echo "Setting up the Gridlock Challenge environment..."

# Check if the virtual environment directory already exists
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Activate the virtual environment
source venv/bin/activate

# Install requirements
echo "Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

# Run the Streamlit application
echo "Launching the Gridlock tool..."
streamlit run app.py