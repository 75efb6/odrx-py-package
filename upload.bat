@echo off
setlocal enabledelayedexpansion

REM Activate virtual environment
call .venv\Scripts\activate.bat || exit /b %errorlevel%

echo 🚀 Uploading package to PyPI...

REM Install twine
python -m pip install twine || exit /b %errorlevel%

REM Upload package
python -m twine upload dist\* || exit /b %errorlevel%

echo ✅ Upload complete!

endlocal