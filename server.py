#!/usr/bin/env python3
"""
HCO-CamTam - Camera Tool
By Azhar (Hackers Colony)
"""

import os
import cv2
from flask import Flask
from colorama import Fore, Style, init

init(autoreset=True)

app = Flask(__name__)
CAPTURE_DIR = "captures"
TOTAL_IMAGES = 10

# Ensure captures/ directory exists
os.makedirs(CAPTURE_DIR, exist_ok=True)

def gen_frames():
    cam = cv2.VideoCapture(0)  # 0 = front camera
    count = 0

    print(Fore.CYAN + "[*] Capturing images from front camera...")

    while count < TOTAL_IMAGES:
        success, frame = cam.read()
        if not success:
            print(Fore.RED + "[!] Camera not accessible!")
            break
        else:
            filename = os.path.join(CAPTURE_DIR, f"img_{count+1}.jpg")
            cv2.imwrite(filename, frame)
            print(Fore.GREEN + f"[+] Saved {filename}")
            count += 1

    cam.release()
    if count == TOTAL_IMAGES:
        print(Fore.MAGENTA + Style.BRIGHT + f"\n[✔] {TOTAL_IMAGES} images received successfully!")
        print(Fore.YELLOW + f"[📂] Saved inside: {CAPTURE_DIR}/\n")

@app.route('/')
def index():
    gen_frames()
    return "<h2 style='color:green;'>Camera access complete. You may close this page.</h2>"

if __name__ == "__main__":
    print(Fore.BLUE + "[*] Flask server started on http://127.0.0.1:5000")
    app.run(host="0.0.0.0", port=5000)
