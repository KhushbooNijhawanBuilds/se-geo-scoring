#!/bin/bash
# Double-click to start the Content GEO Score app on a Mac.
cd "$(dirname "$0")" || exit 1

if ! command -v python3 >/dev/null 2>&1; then
  echo "Python 3 is not installed. Install it from https://www.python.org/downloads/ and run this again."
  read -r -p "Press Enter to close."
  exit 1
fi

if [ ! -f ".streamlit/secrets.toml" ]; then
  echo "No API key file yet. Copy .streamlit/secrets.toml.example to .streamlit/secrets.toml and put your key in it,"
  echo "or paste the key in the app's sidebar each time."
fi

if [ ! -d ".venv" ]; then
  echo "First run: setting up (takes a minute)..."
  python3 -m venv .venv || exit 1
  ./.venv/bin/pip install --quiet --upgrade pip
  ./.venv/bin/pip install --quiet -r requirements.txt || exit 1
fi

echo "Starting the app at http://localhost:8501 (close this window to stop it)."
./.venv/bin/streamlit run app.py
