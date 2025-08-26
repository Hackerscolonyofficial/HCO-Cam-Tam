#!/bin/bash
# HCO-Cam-Tam Installer
# By Azhar (Hackers Colony)

clear
echo -e "\e[91m[+] Installing requirements for HCO Cam Tam...\e[0m"
sleep 2

# Update Termux
pkg update -y && pkg upgrade -y

# Install Python & essentials
pkg install -y python git wget curl

# Install pip packages cleanly
pip install --upgrade pip
pip install flask==3.1.1 colorama requests

# Install OpenCV (headless, avoids stuck build)
pip install opencv-python==4.9.0.80

# Install cloudflared
pkg install -y cloudflared

clear
echo -e "\e[92m[+] Installation Complete!\e[0m"
echo -e "\e[93m[*] To run the tool, type:\e[0m"
echo -e "\e[96m   python main.py\e[0m"
