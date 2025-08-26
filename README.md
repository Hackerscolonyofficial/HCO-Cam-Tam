# HCO-Cam-Tam
Educational Live Camera Tool by Hackers Colony  
**Author:** Azhar  

---

## Features

- Paid unlock system with **YouTube redirect**  
- Countdown 9..8..7..6..5..4..3..2..1  
- Shows **HCO CAM TAM by Azhar** in **Neon Red** after unlock  
- Live camera feed via Flask at `/cam`  
- Auto Cloudflare tunnel generates public URL  
- Public URL displayed in **bold green letters** in Termux  
- Beautiful colorful outputs in Termux  

---

## ⚡ Setup in Termux

```bash
# 1️⃣ Update Termux
pkg update -y && pkg upgrade -y

# 2️⃣ Install dependencies
pkg install -y python git cloudflared

# 3️⃣ Clone the repo
git clone https://github.com/YourUsername/HCO-Cam-Tam.git
cd HCO-Cam-Tam

# 4️⃣ Install Python modules
pip install -r requirements.txt --no-cache-dir

# 5️⃣ Run the tool
python main.py
```

> Make sure to allow Termux access to your camera.

---

## 🔗 Usage

1. Run the tool: `python main.py`  
2. Countdown + redirect to YouTube appears  
3. After subscribing & pressing ENTER → Neon banner appears  
4. Flask server runs on port 5000  
5. Auto Cloudflare tunnel gives public link  
6. Visit `http://<public_url>/cam` to view **live camera feed**  

---

## 🌐 Social Links

[![YouTube](https://img.shields.io/badge/YouTube-Hackers_Colony_Tech-red)](https://youtube.com/@hackers_colony_tech?si=pvdCWZggTIuGb0ya)  
[![Telegram](https://img.shields.io/badge/Telegram-Hackers_Colony-blue)](https://t.me/hackersColony)  
[![Instagram](https://img.shields.io/badge/Instagram-Hackers_Colony_Official-purple)](https://www.instagram.com/hackers_colony_official)  

---

## ⚠ Disclaimer

This tool is for **educational purposes only**.  
Do not use it to spy on anyone without consent.  

---

**Code by Azhar (Hackers Colony)**
