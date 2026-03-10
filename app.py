from flask import Flask, render_template, send_file
from camera import capture_photos
from collage import create_collage

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/capture")
def capture():

    photos = capture_photos()

    path = create_collage(photos)

    return send_file(path, mimetype='image/jpeg')


if __name__ == "__main__":
    app.run(debug=True)