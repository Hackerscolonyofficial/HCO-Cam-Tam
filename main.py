import os
import time
import sys

from colorama import Fore, Style, init
init(autoreset=True)

YOUTUBE_URL = "https://youtube.com/@hackers_colony_tech?si=pvdCWZggTIuGb0ya"

def clear():
    os.system("clear")

def countdown(seconds):
    for i in range(seconds, 0, -1):
        sys.stdout.write(f"\r{Fore.CYAN}[*] Redirecting in {i} seconds... ")
        sys.stdout.flush()
        time.sleep(1)
    print()

def open_youtube():
    print(Fore.YELLOW + "\n[!] This tool is locked. Subscribe to our YouTube channel to unlock.")
    countdown(8)
    os.system(f"xdg-open {YOUTUBE_URL}")
    input(Fore.GREEN + "\nPress ENTER after subscribing to continue...")

def banner():
    clear()
    print(Fore.RED + Style.BRIGHT + "\n HCO CAM TAM")
    print(Fore.GREEN + " by Azhar - A Camera Tool\n")

if __name__ == "__main__":
    open_youtube()
    banner()
    print(Fore.MAGENTA + "[*] Cloudflare link will appear here once started...\n")
