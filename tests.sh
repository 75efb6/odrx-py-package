#!/bin/bash
set -e  # Stop on first error

export PYTHONPATH=./src
export PYO3_USE_ABI3_FORWARD_COMPATIBILITY=1

echo "Activating venv..."
rm -rf .venv
python -m venv .venv
chmod +x .venv/bin/activate
source .venv/bin/activate

echo "🐍 Python version:"
python --version

echo "⬆️ Installing test dependencies..."
python -m pip install --upgrade pip httpx git+https://github.com/unclem2/rosu-pp-py.git


python3 tests/run_tests.py