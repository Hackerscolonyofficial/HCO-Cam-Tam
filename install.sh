#!/usr/bin/env python3
"""
HCO-CamTam - Camera Tool
By Azhar (Hackers Colony)
"""

import os
import cv2
from flask import Flask, Response
from datetime import datetime

app = Flask(__name__)
CAPTURE_DIR = "captures"
TOTAL_IMAGES = 10

# Make sure captures/ exists
os.makedirs(CAPTURE_DIR, exist_ok=True)

def gen_frames():
    cam = cv2.VideoCapture(0)  # 0 = front camera (usually works for mobiles/laptops)
    count = 0
    while count < TOTAL_IMAGES:
        success, frame = cam.read()
        if not success:
            break
        else:
            filename = os.path.join(CAPTURE_DIR, f"img_{count+1}.jpg")
            cv2.imwrite(filename, frame)
            count += 1
    cam.release()
    print(f"[✔] {TOTAL_IMAGES} images received and saved in {CAPTURE_DIR}/")

@app.route('/')
def index():
    gen_frames()
    return "<h2>Camera access complete. You may close this page.</h2>"

if __name__ == "__main__":
    print("[*] Flask server started on http://127.0.0.1:5000")
    app.run(host="0.0.0.0", port=5000)
