#!/usr/bin/env python3
"""
HCO-CAM-TAM - Educational Camera Tool
By Azhar (Hackers Colony)
"""

import os
import time
import webbrowser
from flask import Flask, Response
import cv2
from colorama import Fore, Style, init

init(autoreset=True)

# Flask app
app = Flask(__name__)
camera = cv2.VideoCapture(0)

# ==============================
# Unlock Tool Function
# ==============================
def unlock_tool():
    print(Fore.YELLOW + Style.BRIGHT + "\nThis tool is PAID!")
    print(Fore.CYAN + "👉 Subscribe & Click the Bell Icon to Unlock!\n")

    for i in range(9, 0, -1):
        print(Fore.MAGENTA + f"Redirecting in {i}...")
        time.sleep(1)

    # Open YouTube link
    youtube_link = "https://youtube.com/@hackers_colony_tech"
    webbrowser.open(youtube_link)

    input(Fore.GREEN + "\n✅ After subscribing, press ENTER to continue...")

    print(Fore.RED + Style.BRIGHT + "\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
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


@app.route('/cam')
def cam():
    return Response(generate_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


# ==============================
# Main Run
# ==============================
if __name__ == "__main__":
    unlock_tool()

    print(Fore.YELLOW + "🚀 Starting Flask server on http://127.0.0.1:5000/cam")
    print(Fore.CYAN + "🌍 Starting Cloudflare Tunnel...")

    # Start Cloudflared tunnel
    os.system("pkill cloudflared > /dev/null 2>&1")  # Kill if already running
    os.system("cloudflared tunnel --url http://127.0.0.1:5000 --logfile tunnel.log > /dev/null 2>&1 &")

    time.sleep(5)
    print(Fore.GREEN + "✅ Cloudflare Tunnel Started! Check the logs for public URL.")

    app.run(host="0.0.0.0", port=5000)
