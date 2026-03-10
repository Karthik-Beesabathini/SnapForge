from flask import Flask, render_template, send_file, request
from camera import capture_photos
from collage import create_collage,create_collage1,create_collage2,create_collage3

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/capture")
def capture():
    num_photos = request.args.get('num_photos',  type=int)
    
    photos = capture_photos(num_photos)

    if(num_photos == 6):
        path = create_collage(photos)
    elif(num_photos == 4):
        path = create_collage1(photos)
    elif(num_photos == 3):
        path = create_collage2(photos)
    elif (num_photos == 2):
        path = create_collage3(photos)        





    

    return send_file(path, mimetype='image/jpeg')


if __name__ == "__main__":
    app.run(debug=True)