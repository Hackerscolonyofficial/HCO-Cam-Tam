#!/usr/bin/env python3
"""
HCO-Cam-Tam - Educational Camera Tool
By Azhar (Hackers Colony)
"""

import os
import time
import webbrowser
import subprocess
from colorama import Fore, Style
from flask import Flask, Response, render_template_string

# Try importing OpenCV
try:
    import cv2
    OPENCV_AVAILABLE = True
except ImportError:
    OPENCV_AVAILABLE = False

app = Flask(__name__)

# ---------- Unlock System with Countdown ----------
def unlock_tool():
    print(Fore.RED + Style.BRIGHT + "\nThis tool is not free!\n" + Style.RESET_ALL)
    print("🔒 To unlock, you must subscribe to our YouTube channel!\n")

    # Countdown
    for i in range(9, 0, -1):
        print(Fore.YELLOW + f"Redirecting in {i}..." + Style.RESET_ALL)
        time.sleep(1)

    # Redirect to YouTube
    youtube = "https://youtube.com/@hackers_colony_tech"
    print(Fore.GREEN + "\nOpening YouTube... Please subscribe and then return here." + Style.RESET_ALL)
    webbrowser.open(youtube)
    input(Fore.CYAN + "\n✅ Press ENTER after subscribing to continue..." + Style.RESET_ALL)

    # Flashing Banner
    for _ in range(5):
        print(Fore.RED + Style.BRIGHT + "\n==============================")
        print("     HCO-Cam-Tam Tool")
        print("        By Azhar 🔥")
        print("==============================\n" + Style.RESET_ALL)
        time.sleep(0.5)
        os.system("clear")  # flashing effect
        time.sleep(0.3)


# ---------- Camera Stream ----------
def generate_frames():
    if not OPENCV_AVAILABLE:
        return
    camera = cv2.VideoCapture(0)
    if not camera.isOpened():
        return
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
    if OPENCV_AVAILABLE:
        return "📷 HCO-Cam-Tam Running... Visit <a href='/cam'>/cam</a> to see the live camera feed."
    else:
        return render_template_string("""
            <html><body style="background:black; color:red; text-align:center; font-family:monospace;">
            <h1>⚠️ HCO-Cam-Tam</h1>
            <h2>No Camera Found!</h2>
            <p>Install OpenCV to enable live streaming.</p>
            </body></html>
        """)

@app.route('/cam')
def cam():
    if not OPENCV_AVAILABLE:
        return render_template_string("""
            <html><body style="background:black; color:lime; text-align:center; font-family:monospace;">
            <h1>HCO-Cam-Tam</h1>
            <h2>📵 Camera Not Available</h2>
            <p>Showing fake feed instead.</p>
            </body></html>
        """)
    return Response(generate_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


# ---------- Cloudflare Tunnel ----------
def start_cloudflared():
    print(Fore.YELLOW + "\n🚀 Starting Cloudflare Tunnel..." + Style.RESET_ALL)
    try:
        proc = subprocess.Popen(["cloudflared", "tunnel", "--url", "http://localhost:5000"],
                                stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        for line in proc.stdout:
            if "trycloudflare.com" in line:
                url = line.split(" ")[-1].strip()
                print(Fore.CYAN + f"\n🌍 Public Link: {url}/cam\n" + Style.RESET_ALL)
                break
    except Exception as e:
        print(Fore.RED + f"[!] Cloudflared error: {e}" + Style.RESET_ALL)


if __name__ == "__main__":
    unlock_tool()
    from threading import Thread
    Thread(target=lambda: app.run(host="0.0.0.0", port=5000, debug=False)).start()
    start_cloudflared()
