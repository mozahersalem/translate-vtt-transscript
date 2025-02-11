#!/bin/bash

# Ensure the script runs only inside a virtual environment
if [[ -z "$VIRTUAL_ENV" ]]; then
    echo "❌ Error: Virtual environment is not activated!"
    echo "➡️ Run 'source venv/bin/activate' first."
    exit 1
else
    echo "✅ Virtual environment detected. Installing dependencies..."
    pip install -r requirements.txt
fi