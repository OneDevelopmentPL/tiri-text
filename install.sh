#!/bin/bash

echo "Welcome to Tiri (text) installer! This will install libraries on your computer."
echo "Let's start. Do NOT run this script with sudo. Make sure Python and pip are installed."
echo "Tiri version: 3.1 | Installer version: 1.0"
echo

PYTHON_CMD=python3

# 👉 Tu możesz zmienić nazwę venv
VENV_NAME=venv

echo "[1/4] Checking Python..."
if ! command -v $PYTHON_CMD &> /dev/null; then
    echo "❌ Python 3 is not installed! Install Python and pip first."
    exit 1
fi

echo "[2/4] Cloning repository..."
cd ~ || exit 1
git clone https://github.com/OneDevelopmentPL/tiri-text.git
cd tiri-text || exit 1

echo "[3/4] Creating virtual environment..."
$PYTHON_CMD -m venv $VENV_NAME

echo "[3/4] Activating virtual environment..."
source $VENV_NAME/bin/activate

echo "[4/4] Installing required packages..."
pip install --upgrade pip
pip install PyQt6 PyQt6-WebEngine

echo
echo "🎉 Installation finished successfully!"
echo
echo "To run TIRI:"
echo "  source venv/bin/activate"
echo "  python tiri.py"
echo
echo "Tip: You can add a shortcut to make Tiri act like real Siri 😎"
