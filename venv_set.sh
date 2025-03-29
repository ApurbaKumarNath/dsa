#!/bin/bash

# Update package list
echo "Updating package list..."
sudo apt update

# Ensure PyPy is installed
if ! command -v pypy3 >/dev/null 2>&1; then
    echo "PyPy is not installed. Installing PyPy..."
    sudo apt install -y pypy3
fi

# Ensure pypy3-venv is installed
if ! dpkg -s pypy3-venv >/dev/null 2>&1; then
    echo "Installing pypy3-venv..."
    sudo apt install -y pypy3-venv
fi

# Ensure pypy3-dev is installed (for development headers)
if ! dpkg -s pypy3-dev >/dev/null 2>&1; then
    echo "Installing pypy3-dev..."
    sudo apt install -y pypy3-dev
fi

# Create virtual environment using PyPy
if [ ! -d "venv" ]; then
    echo "Creating virtual environment with PyPy..."
    pypy3 -m venv venv
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Install and upgrade pip, then install required packages
echo "Installing Python packages..."
pip install --upgrade pip
pip install numpy wheel ipykernel psutil

echo "Setup complete!"

# Run these in terminal (use the actual path to your script):
# chmod +x path/venv_set.sh
# bash path/venv_set.sh