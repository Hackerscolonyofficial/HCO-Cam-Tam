#!/usr/bin/env python3
"""
HCO-Cam-Tam - Camera Capture Tool (Educational)
By Azhar (Hackers Colony)
"""

import os
import time
import cv2
from flask import Flask, send_from_directory
from colorama import Fore, Style, init

# Initialize Colorama
init(autoreset=True)

# === Banner Unlock System ===
def unlock_tool():
    print(Fore.YELLOW + "\n🔒 This tool is locked!")
    print(Fore.CYAN + "👉 To unlock, you must subscribe & press the bell icon on our YouTube channel.\n")
    for i in range(8, 0, -1):
        print(Fore.MAGENTA + f"Redirecting in {i} seconds...", end="\r")
        time.sleep(1)
    os.system("xdg-open https://youtube.com/@hackers_colony_tech")
    input(Fore.GREEN + "\nAfter subscribing, press ENTER to continue...")

    # Neon effect after unlock
    print(Fore.GREEN + Style.BRIGHT + "\n" + "="*50)
    print(Fore.RED + Style.BRIGHT + "      HCO-Cam-Tam by Azhar (Hackers Colony)     ")
    print(Fore.GREEN + Style.BRIGHT + "="*50 + "\n")

# === Camera Capture Function ===
def capture_images():
    save_path = os.path.expanduser("~/Downloads")
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    cap = cv2.VideoCapture(0)
    count = 0
    print(Fore.YELLOW + "\n📸 Capturing 10 pictures from camera...")

    while count < 10:
        ret, frame = cap.read()
        if not ret:
            print(Fore.RED + "❌ Failed to access camera!")
            break
        filename = os.path.join(save_path, f"hco_cam_{count+1}.jpg")
        cv2.imwrite(filename, frame)
        print(Fore.GREEN + f"✅ Saved: {filename}")
        count += 1
        time.sleep(1)

    cap.release()
    print(Fore.CYAN + "\n🎉 Capture complete! Images saved in Downloads folder.")

# === Flask Server for File Sharing ===
app = Flask(__name__)
DOWNLOADS = os.path.expanduser("~/Downloads")

@app.route('/files/<path:filename>')
def serve_file(filename):
    return send_from_directory(DOWNLOADS, filename)

# === Auto Start Cloudflare Tunnel ===
def start_cloudflare():
    print(Fore.YELLOW + "\n☁️ Starting Cloudflare Tunnel...")
    os.system("pkill cloudflared >/dev/null 2>&1")
    os.system("cloudflared tunnel --url http://127.0.0.1:5000 --logfile cloudflared.log --loglevel info &")
    time.sleep(5)
    try:
        import requests
        r = requests.get("http://127.0.0.1:5000")
    except:
        pass
    print(Fore.GREEN + "🌍 Cloudflare Tunnel started successfully!")
    print(Fore.CYAN + "👉 Your public link will be shown by cloudflared in Termux console.\n")

# === Main Execution ===
if __name__ == "__main__":
    unlock_tool()
    capture_images()
    start_cloudflare()
    print(Fore.MAGENTA + "🚀 Hosting Flask server at http://127.0.0.1:5000")
    print(Fore.CYAN + "👉 Access your images at /files/hco_cam_X.jpg")
    app.run(host="0.0.0.0", port=5000)
