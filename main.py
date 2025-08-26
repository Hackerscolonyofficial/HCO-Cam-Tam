#!/usr/bin/env python3
"""
HCO-Cam-Tam - Camera Capture Tool (Educational Demo)
By Azhar (Hackers Colony)
"""

import os
import time
import subprocess
from colorama import Fore, Style
import cv2

# ========= Banner =========
def banner():
    os.system("clear")
    print(Fore.RED + Style.BRIGHT + "\n\n     HCO CAM TAM\n" + Style.RESET_ALL)
    print(Fore.GREEN + "         by Azhar - A Camera Tool\n" + Style.RESET_ALL)

# ========= Countdown =========
def countdown():
    for i in range(5, 0, -1):
        print(Fore.CYAN + f"Starting in {i}..." + Style.RESET_ALL)
        time.sleep(1)

# ========= Camera Capture =========
def capture_images():
    cam = cv2.VideoCapture(0)  # open camera
    if not cam.isOpened():
        print(Fore.RED + "Camera not found!" + Style.RESET_ALL)
        return
    
    print(Fore.YELLOW + "\n[+] Capturing 5 FRONT images..." + Style.RESET_ALL)
    for i in range(1, 6):
        ret, frame = cam.read()
        if ret:
            filename = f"front_{i}.jpg"
            cv2.imwrite(filename, frame)
            print(Fore.GREEN + f"[✔] Saved {filename}" + Style.RESET_ALL)
        time.sleep(1)

    print(Fore.YELLOW + "\n[+] Capturing 5 BACK images..." + Style.RESET_ALL)
    for i in range(1, 6):
        ret, frame = cam.read()
        if ret:
            filename = f"back_{i}.jpg"
            cv2.imwrite(filename, frame)
            print(Fore.GREEN + f"[✔] Saved {filename}" + Style.RESET_ALL)
        time.sleep(1)

    cam.release()
    print(Fore.CYAN + "\n[+] Images received successfully!" + Style.RESET_ALL)

# ========= Start Cloudflare Tunnel =========
def start_cloudflare():
    print(Fore.YELLOW + "\n[+] Starting Cloudflare tunnel..." + Style.RESET_ALL)
    try:
        # Start Flask server
        subprocess.Popen(["python", "-m", "http.server", "5000"])
        time.sleep(2)

        # Start Cloudflare tunnel
        tunnel = subprocess.Popen(["cloudflared", "tunnel", "--url", "http://localhost:5000"],
                                  stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)

        # Print the first line with https link
        for line in tunnel.stdout:
            if "https://" in line:
                print(Fore.MAGENTA + f"\n[+] Cloudflare Link: {line.strip()}" + Style.RESET_ALL)
                break

    except Exception as e:
        print(Fore.RED + f"[!] Cloudflare Error: {e}" + Style.RESET_ALL)

# ========= Main =========
if __name__ == "__main__":
    banner()
    print(Fore.LIGHTBLUE_EX + "Redirecting to YouTube... please subscribe!" + Style.RESET_ALL)
    time.sleep(2)
    os.system("xdg-open https://youtube.com/@hackers_colony_tech")

    input(Fore.LIGHTGREEN_EX + "\nPress Enter after subscribing to continue..." + Style.RESET_ALL)

    banner()
    countdown()
    capture_images()
    start_cloudflare()
