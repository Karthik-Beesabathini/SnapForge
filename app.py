from flask import Flask, render_template, Response, request, send_file
from camera import VideoCamera
from collage import create_collage, create_collage1, create_collage2, create_collage3

app = Flask(__name__)
camera = VideoCamera()

def gen(camera):
    while True:
        frame = camera.get_frame()
        if frame:

            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/video_feed")
def video_feed():

    return Response(gen(camera),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route("/capture")
def capture():
    num_photos = request.args.get('num_photos', type=int)
    photos = camera.capture_multiple(num_photos)
    

    if num_photos == 6: path = create_collage(photos)
    elif num_photos == 4: path = create_collage1(photos)
    elif num_photos == 3: path = create_collage2(photos)
    elif num_photos == 2: path = create_collage3(photos)
    
    return send_file(path, mimetype='image/jpeg')

if __name__ == "__main__":
    app.run(debug=True)