#!/usr/bin/env python3
"""
HCO-Cam-Tam - Educational Live Camera Tool (Termux-Friendly)
By Azhar (Hackers Colony)
"""

import os
import time
import webbrowser
import subprocess
import requests
from flask import Flask, Response
import cv2  # opencv-python-headless works here
from colorama import Fore, Style, init
from threading import Thread

init(autoreset=True)

# Flask app
app = Flask(__name__)
camera = cv2.VideoCapture(0)

# ==============================
# Unlock Tool Function
# ==============================
def unlock_tool():
    print(Fore.YELLOW + Style.BRIGHT + "\n⚠️  This tool is PAID!")
    print(Fore.CYAN + "👉 Subscribe & Click the Bell Icon to Unlock!\n")

    # Countdown 9..1
    for i in range(9, 0, -1):
        print(Fore.MAGENTA + f"Redirecting in {i}...")
        time.sleep(1)

    youtube_link = "https://youtube.com/@hackers_colony_tech?si=pvdCWZggTIuGb0ya"
    webbrowser.open(youtube_link)

    input(Fore.GREEN + "\n✅ After subscribing, press ENTER to unlock...\n")

    # Neon banner
    print(Fore.RED + Style.BRIGHT + "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(Fore.RED + Style.BRIGHT + "      HCO CAM TAM by Azhar     ")
    print(Fore.RED + Style.BRIGHT + "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n")

# ==============================
# Camera Stream
# ==============================
def generate_frames():
    while True:
        success, frame = camera.read()
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def index():
    return "📷 HCO-Cam-Tam Running... Visit /cam for live feed."

@app.route('/cam')
def cam():
    return Response(generate_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

# ==============================
# Cloudflare Tunnel
# ==============================
def start_cloudflared():
    print(Fore.YELLOW + "\n🚀 Starting Cloudflare Tunnel...")

    # Kill any existing tunnels
    os.system("pkill cloudflared > /dev/null 2>&1")

    # Start new tunnel
    subprocess.Popen(["cloudflared", "tunnel", "--url", "http://127.0.0.1:5000", "--logfile", ".cloudflared.log"],
                     stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    time.sleep(5)  # wait for tunnel to initialize

    try:
        r = requests.get("http://127.0.0.1:4040/api/tunnels")
        tunnels = r.json()["tunnels"]
        public_url = tunnels[0]["public_url"]
        print(Fore.GREEN + Style.BRIGHT + f"\n🌍 Public Link: {public_url}/cam\n")
    except Exception as e:
        print(Fore.RED + f"[-] Could not get public URL automatically. Check .cloudflared.log\n{e}")

# ==============================
# Main
# ==============================
if __name__ == "__main__":
    unlock_tool()

    # Start Flask server in a separate thread
    Thread(target=lambda: app.run(host="0.0.0.0", port=5000, debug=False, use_reloader=False)).start()
    start_cloudflared()
