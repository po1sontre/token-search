#!/bin/bash

echo "Installing dependencies for Discord Token Finder..."

# Check for Python3 installation
if ! command -v python3 &>/dev/null; then
    echo "Python3 is not installed. Please install it first."
    exit 1
fi

# Check for pip installation
if ! command -v pip &>/dev/null; then
    echo "pip is not installed. Installing pip..."
    
    if command -v apt &>/dev/null; then
        sudo apt-get install python3-pip -y
    elif command -v pacman &>/dev/null; then
        sudo pacman -S --noconfirm python-pip
    elif command -v dnf &>/dev/null; then
        sudo dnf install python3-pip -y
    elif command -v zypper &>/dev/null; then
        sudo zypper install python3-pip -y
    else
        echo "Unsupported package manager. Please install pip manually."
        exit 1
    fi
fi

# Check for tkinter installation
echo "Checking for tkinter..."
python3 -c "import tkinter" 2>/dev/null
if [ $? -ne 0 ]; then
    echo "tkinter is not installed. Installing tkinter..."
    
    if command -v apt &>/dev/null; then
        sudo apt-get install python3-tk -y
    elif command -v pacman &>/dev/null; then
        sudo pacman -S --noconfirm tk
    elif command -v dnf &>/dev/null; then
        sudo dnf install python3-tkinter -y
    elif command -v zypper &>/dev/null; then
        sudo zypper install python3-tk -y
    else
        echo "Unsupported package manager. Please install tkinter manually."
        exit 1
    fi
fi

# Install required Python modules
echo "Installing required Python packages..."
pip install colorama

echo "Installation complete. Run the program with: python3 discord_token_finder.py"
