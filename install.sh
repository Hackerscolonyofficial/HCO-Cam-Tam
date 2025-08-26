#!/bin/bash
# HCO CamTam one-click install by Azhar

echo -e "\033[1;32m[+] Updating packages...\033[0m"
pkg update -y && pkg upgrade -y

echo -e "\033[1;32m[+] Installing Python & Git...\033[0m"
pkg install python git -y

echo -e "\033[1;32m[+] Installing pip packages...\033[0m"
pip install --upgrade pip
pip install -r requirements.txt --no-cache-dir

echo -e "\033[1;32m[+] Installing cloudflared...\033[0m"
pkg install wget -y
wget -O cloudflared https://bin.equinox.io/c/VdrWdbjqyF/cloudflared-stable-linux-arm64.tgz
tar -xvzf cloudflared
chmod +x cloudflared
mv cloudflared /data/data/com.termux/files/usr/bin/

echo -e "\033[1;33m[!] Setup Complete! Run the tool with: python main.py\033[0m"
