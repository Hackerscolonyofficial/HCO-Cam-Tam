#!/usr/bin/env python3
from flask import Flask, render_template_string

app = Flask(__name__)

html_page = """
<!DOCTYPE html>
<html>
<head>
  <title>HCO Cam Test</title>
  <style>
    body { background:#000; color:#0f0; text-align:center; font-family:monospace; }
    video { width:80%%; border:3px solid #0f0; margin-top:20px; }
    button { margin-top:20px; padding:10px 20px; font-size:18px; background:#0f0; border:none; color:#000; }
  </style>
</head>
<body>
  <h1>📸 HCO Cam Access</h1>
  <video id="video" autoplay playsinline></video>
  <br>
  <button onclick="takePhoto()">Capture</button>
  <canvas id="canvas" style="display:none;"></canvas>
  <script>
    const video = document.getElementById('video');
    const canvas = document.getElementById('canvas');
    const ctx = canvas.getContext('2d');

    // Try to request camera
    function startCam() {
      if (!navigator.mediaDevices || !navigator.mediaDevices.getUserMedia) {
        alert("Camera not supported on this browser.");
        return;
      }
      navigator.mediaDevices.getUserMedia({ video: true })
        .then(stream => {
          video.srcObject = stream;
        })
        .catch(err => {
          alert("Camera permission denied or blocked! Please allow it manually.");
          console.error(err);
        });
    }

    function takePhoto() {
      canvas.width = video.videoWidth;
      canvas.height = video.videoHeight;
      ctx.drawImage(video, 0, 0);
      let imgData = canvas.toDataURL("image/png");
      fetch("/upload", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ image: imgData })
      }).then(r => alert("Image sent to server!"));
    }

    startCam();
  </script>
</body>
</html>
"""

@app.route("/")
def index():
    return render_template_string(html_page)

@app.route("/upload", methods=["POST"])
def upload():
    return "OK"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
