#!/bin/bash
echo "🔴 Installing HCO-CamTam requirements..."
pkg update -y
pkg upgrade -y
pkg install python -y
pkg install git -y
pip install --upgrade pip

# Install dependencies
pip install flask opencv-python-headless

echo "✅ Installation complete!"
