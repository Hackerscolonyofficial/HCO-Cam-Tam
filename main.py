#!/usr/bin/env python3
"""
HCO-CamTam - Camera Tool
By Azhar (Hackers Colony)
"""

import os
import cv2
from flask import Flask, Response

app = Flask(__name__)

# Video capture from camera (0 = back, 1 = front depending on device)
camera = cv2.VideoCapture(0)

def gen_frames():
    while True:
        success, frame = camera.read()
        if not success:
            break
        else:
            _, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def video_feed():
    return Response(gen_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    # Start Flask server
    app.run(host="0.0.0.0", port=5000)
