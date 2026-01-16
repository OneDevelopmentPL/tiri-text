#!/bin/bash

echo "Welcome to Tiri (text) installer! This will install librares and bla bla bla on you computer.
echo "Let's start, make sure to NOT run it with sudo, make sure you have python with pip installed."
echo "Tiri version - 3.1 installer version - 1."

PYTHON_CMD=python3

# Virtual environment name
VENV_NAME=venv

echo "[1/4] Checking Python..."
if ! command -v $PYTHON_CMD &> /dev/null; then
    echo "Python 3 is not installed! Also download pip"
    exit 1
fi

echo "[2/4] Cloning repo...
cd ~
git clone https://github.com/OneDevelopmentPL/tiri-text.git
cd tiri-text

echo "[3/] Creating virtual environment..."
$PYTHON_CMD -m venv $VENV_NAME

echo "[3/4] Activating virtual environment..."
source $VENV_NAME/bin/activate

echo "[4/4] Installing required packages..."
pip install --upgrade pip
pip install PyQt6 PyQt6-WebEngine

echo "Installation finished successfully🎉"
echo
echo "To run TIRI:"
echo "  source venv/bin/activate"
echo "  python tiri.py"
echo

echo "Tip: You can add a shortcut on your taskbar to make Tiri act like real Siri"
