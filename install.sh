#!/bin/bash
# HCO CamTam one-click install by Azhar

echo -e "\033[1;32m[+] Updating Termux packages...\033[0m"
pkg update -y && pkg upgrade -y

echo -e "\033[1;32m[+] Installing required packages...\033[0m"
pkg install python git clang libjpeg-turbo fftw wget tar -y

echo -e "\033[1;32m[+] Upgrading pip...\033[0m"
pip install --upgrade pip

echo -e "\033[1;32m[+] Installing Python packages (Flask + OpenCV)...\033[0m"
# Using pre-built OpenCV wheel to avoid compilation
pip install flask==3.1.1 opencv-python-headless==4.5.5.64 --no-cache-dir --prefer-binary

echo -e "\033[1;32m[+] Installing Cloudflared...\033[0m"
wget -O cloudflared.tgz https://bin.equinox.io/c/VdrWdbjqyF/cloudflared-stable-linux-arm64.tgz
tar -xvzf cloudflared.tgz
chmod +x cloudflared
mv cloudflared /data/data/com.termux/files/usr/bin/

echo -e "\033[1;33m[!] Setup complete!\033[0m"
echo -e "\033[1;34mRun the tool with:\033[0m python main.py"
