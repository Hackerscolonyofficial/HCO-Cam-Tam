#!/data/data/com.termux/files/usr/bin/bash
# =====================================================
# HCO-CamTam Installer Script
# By Azhar (Hackers Colony)
# =====================================================

clear
echo -e "\e[91m"
echo "============================================"
echo "        Installing HCO-CamTam Tool          "
echo "============================================"
echo -e "\e[0m"

# Update Termux
pkg update -y && pkg upgrade -y

# Install required packages
pkg install -y python git wget curl

# Upgrade pip
pip install --upgrade pip

# Install Python requirements
if [ -f requirements.txt ]; then
    pip install -r requirements.txt --no-cache-dir
fi

# Install cloudflared if missing
if ! command -v cloudflared &> /dev/null
then
    pkg install -y cloudflared
fi

# Make scripts executable
chmod +x main.py server.py

echo -e "\n\e[92m[✔] Installation complete!"
echo -e "\e[96mLaunching HCO-CamTam...\e[0m\n"

# Start main.py
python main.py
