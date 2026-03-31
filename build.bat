@echo off
setlocal enabledelayedexpansion

REM Stop on error helper
set ERR=0

echo 🧹 Cleaning old artifacts...
if exist build rmdir /s /q build || set ERR=1
if exist dist rmdir /s /q dist || set ERR=1
del /q src\*.egg-info 2>nul

if %ERR% neq 0 exit /b %ERR%

REM Run tests before building
echo 🔍 Running tests before build...
call tests.bat || exit /b %errorlevel%

echo ⬆️ Installing build dependencies...
python -m pip install --upgrade pip setuptools wheel build || exit /b %errorlevel%

echo 📦 Building package...
python -m build . || exit /b %errorlevel%

echo 📥 Installing package locally...
for %%f in (dist\*.whl) do (
    python -m pip install "%%f" --force-reinstall || exit /b %errorlevel%
)

cd ..
echo ✅ Build and install complete on local .venv!

endlocal