#!/usr/bin/env bash
set -e  # Stop on first error

echo "🧹 Cleaning old artifacts..."
rm -rf src/build src/dist src/*.egg-info

echo "Activating venv..."
rm -rf .venv
python -m venv .venv
chmod +x .venv/bin/activate
source .venv/bin/activate

echo "🐍 Python version:"
python --version

echo "⬆️ Installing build dependencies..."
python -m pip install --upgrade pip setuptools wheel

echo "📦 Building package..."
cd src/
python setup.py sdist bdist_wheel

echo "📥 Installing package locally..."
python -m pip install dist/*.whl --force-reinstall

cd ..
echo "✅ Build and install complete on local .venv!"
