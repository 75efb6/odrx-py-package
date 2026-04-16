#!/usr/bin/env bash
set -e  # Stop on first error

echo "🧹 Cleaning old artifacts..."
rm -rf ./build ./dist ./src/*.egg-info

# Run tests before building to ensure everything is working
echo "🔍 Running tests before build..."
./tests.sh

echo "⬆️ Installing build dependencies..."
python -m pip install --upgrade pip setuptools wheel build

echo "📦 Building package..."
python -m build .

echo "📥 Installing package locally..."
python -m pip install dist/*.whl --force-reinstall

cd ..
echo "✅ Build and install complete on local .venv!"
