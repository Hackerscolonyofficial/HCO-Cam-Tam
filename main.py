#!/usr/bin/env python3
"""
HCO-CamTam - Single File Edition
By Azhar (Hackers Colony)
"""

import os
import time
import subprocess
from flask import Flask, render_template_string

# =============================
# Auto-install dependencies
# =============================
def install(package):
    try:
        __import__(package)
    except ImportError:
        os.system(f"pip install {package}")

install("flask")
install("pyngrok")

from pyngrok import ngrok

# =============================
# Flask App
# =============================
app = Flask(__name__)

@app.route("/")
def index():
    return render_template_string("""
        <html>
        <head><title>HCO CamTam</title></head>
        <body style="background:black;color:lime;font-family:monospace;">
            <h1>📸 HCO CamTam</h1>
            <p>Camera tool running... By Azhar</p>
        </body>
        </html>
    """)

# =============================
# Run with Ngrok Tunnel
# =============================
if __name__ == "__main__":
    print("\n\033[91mHCO CamTam - Hackers Colony\033[0m")
    print("Starting server...\n")

    # Start Flask on port 5000
    public_url = ngrok.connect(5000)
    print(f"\nYour Public Link:\n\033[92m{public_url}\033[0m\n")

    app.run(port=5000)
