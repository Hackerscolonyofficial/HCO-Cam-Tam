#!/usr/bin/env python3
"""
HCO-Cam-Tam - Educational Camera Tool
By Azhar (Hackers Colony)
"""

import os
import sys
import time
import subprocess
import webbrowser
from flask import Flask, Response
import cv2

# --------- Auto Install Dependencies ---------
required = ["flask", "opencv-python", "cloudflared"]
for pkg in required:
    try:
        __import__(pkg if pkg != "opencv-python" else "cv2")
    except ImportError:
        os.system(f"pip install {pkg}")

# --------- Unlock System ---------
def unlock_tool():
    print("\nThis tool is not free. To unlock, please subscribe to our YouTube channel.\n")
    for i in range(8, 0, -1):
        sys.stdout.write(f"\rRedirecting in {i}...")
        sys.stdout.flush()
        time.sleep(1)

    # Open YouTube
    youtube_url = "https://youtube.com/@hackers_colony_tech?sub_confirmation=1"
    webbrowser.open(youtube_url)

    input("\n\nAfter subscribing and clicking the bell icon, press ENTER to continue...")

    # Neon styled unlock banner
    print("\n" + "="*60)
    print("\033[1;92m\033[1;41m  HCO-Cam-Tam by Azhar  \033[0m".center(60))
    print("="*60 + "\n")

# --------- Flask Camera App ---------
app = Flask(__name__)
camera = cv2.VideoCapture(0)  # Use webcam

def gen_frames():
    while True:
        success, frame = camera.read()
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

# --------- Run with Cloudflare ---------
def run_server():
    print("[*] Starting local Flask server...")
    subprocess.Popen(["python3", "-m", "flask", "run", "--host=0.0.0.0", "--port=5000"])
    time.sleep(3)
    print("[*] Starting Cloudflare tunnel...")
    os.system("cloudflared tunnel --url http://localhost:5000")

if __name__ == "__main__":
    unlock_tool()
    run_server()
