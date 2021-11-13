from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

UPLOAD_PATH = "uploads"
FILE_TYPE = ["jpg", "jpeg", "png"]
app.config["DEBUG"] = True
app.config["UPLOAD_PATH"] = UPLOAD_PATH

image = ""


def allowedFile(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in FILE_TYPE


# @app.route("/")
# def home():
#     return render_template("index.html")


@app.route("/", methods=["POST", "GET"])
def handleImage():
    global image
    output = ""

    if request.method == "POST":
        if "submit" in request.form:
            file = request.files["file"]
            if file and allowedFile(file.filename):
                image = secure_filename(file.filename)
                file.save(os.path.join(app.config["UPLOAD_PATH"], image))
                output = "Image Uploaded Successfully"
            else:
                output = "Invalid file type!"
            return render_template("index.html", filename=image, output1=output)
        else:  # compress
            compressionRate = float(request.form["compression_rate"])
            print(image)
            if image != "":
                # lakukan compression
                # imageCompressionRate = 'Image pixel difference percentage' $compressionRate
                output = "Image Compressed Successfully"
            else:
                output = "Upload image first!"
            return render_template("index.html", filename=image, output2=output)
    else:
        return render_template("index.html")


# @app.route("/display/<filename>")
# def displayImage(filename):
#     return redirect(url_for("uploads", filename="" + filename), code=301)


if __name__ == "__main__":
    app.run()
