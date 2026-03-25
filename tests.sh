export PYTHONPATH=./src

echo "Activating venv..."
rm -rf .venv
python -m venv .venv
chmod +x .venv/bin/activate
source .venv/bin/activate

echo "🐍 Python version:"
python --version

echo "⬆️ Installing test dependencies..."
python -m pip install --upgrade pip aiohttp


python3 src/tests/run_tests.py