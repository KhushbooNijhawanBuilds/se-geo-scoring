@echo off
REM Double-click to start the Content GEO Score app on Windows.
cd /d "%~dp0"

where python >nul 2>nul
if errorlevel 1 (
  echo Python is not installed. Install it from https://www.python.org/downloads/ ^(tick "Add python.exe to PATH"^) and run this again.
  pause
  exit /b 1
)

if not exist ".streamlit\secrets.toml" (
  echo No API key file yet. Copy .streamlit\secrets.toml.example to .streamlit\secrets.toml and put your key in it,
  echo or paste the key in the app's sidebar each time.
)

if not exist ".venv" (
  echo First run: setting up ^(takes a minute^)...
  python -m venv .venv || exit /b 1
  .venv\Scripts\python -m pip install --quiet --upgrade pip
  .venv\Scripts\pip install --quiet -r requirements.txt || exit /b 1
)

echo Starting the app at http://localhost:8501 (close this window to stop it).
.venv\Scripts\streamlit run app.py
