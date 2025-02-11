#!/bin/bash

# Ensure the script runs only inside a virtual environment
if [[ -z "$VIRTUAL_ENV" ]]; then
    echo "❌ Error: Virtual environment is not activated!"
    echo "➡️ Run 'source venv/bin/activate' first."
    exit 1
else
    echo "✅ Virtual environment detected."
fi

# Install dependencies
echo "📦 Installing dependencies from requirements.txt..."
pip install --no-cache-dir -r requirements.txt

# Run the application
echo "🚀 Running the application..."
python3 src/main.py