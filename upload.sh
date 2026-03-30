#!/usr/bin/env bash

set -e  # Stop on first error

source .venv/bin/activate
echo "🚀 Uploading package to PyPI..."
pip install twine
python -m twine upload dist/*
echo "✅ Upload complete!"