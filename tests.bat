@echo off
REM Stop on first error
setlocal enabledelayedexpansion

REM Set PYTHONPATH
set PYTHONPATH=.\src
set PYO3_USE_ABI3_FORWARD_COMPATIBILITY=1

echo Activating venv...

REM Remove existing venv
REM if exist .venv rmdir /s /q .venv

REM Create virtual environment
REM python -m venv .venv

REM Activate venv
call .venv\Scripts\activate.bat

echo 🐍 Python version:
python --version

echo ⬆️ Installing test dependencies...
REM python -m pip install --upgrade pip httpx git+https://github.com/unclem2/rosu-pp-py.git@main

REM Run tests
python tests\run_tests.py

endlocal