from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import os
from process import *

app = Flask(__name__)

UPLOAD_PATH = "static/uploads/"
DOWNLOAD_PATH = "static/downloads/"
FILE_TYPE = ["jpg", "jpeg", "png"]
app.config["UPLOAD_PATH"] = UPLOAD_PATH
app.config["DOWNLOAD_PATH"] = DOWNLOAD_PATH
app.config["FILE_TYPE"] = FILE_TYPE

image_in = ""
image_out = ""
exe_time = ""


def allowedFile(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in FILE_TYPE


@app.route("/", methods=["POST", "GET"])
def handleImage():
    global image_in
    global image_out
    global exe_time
    output = ""

    if request.method == "POST":
        if "submit" in request.form:
            file = request.files["file"]
            if file and allowedFile(file.filename):
                image_in = secure_filename(file.filename)
                # image_out = "compressed_" + image_in
                file.save(os.path.join(app.config["UPLOAD_PATH"], image_in))
                output = "Image Uploaded Successfully"
            else:
                output = "Invalid file type!"
            return render_template("index.html", image_in=image_in, output1=output)
        elif "compress" in request.form:  # compress
            compression_rate = float(request.form["compression_rate"])
            if image_in != "":
                image_out = "compressed_" + image_in
                input_path = os.path.join(app.config["UPLOAD_PATH"], image_in)
                output_path = os.path.join(app.config["DOWNLOAD_PATH"], image_out)
                exe_time = Process(input_path, output_path, compression_rate)
                output = "Image Compressed Successfully"
            else:
                output = "Upload image first!"
            return render_template(
                "index.html",
                image_in=image_in,
                image_out=image_out,
                output2=output,
                exe_time=exe_time,
            )
    else:
        return render_template("index.html")


@app.route("/uploads_display/<filename>")
def displayUploads(filename):
    return redirect(url_for("static", filename="uploads/" + filename), code=302)


@app.route("/downloads_display/<filename>")
def displayDownloads(filename):
    return redirect(url_for("static", filename="downloads/" + filename), code=302)


if __name__ == "__main__":
    app.run()
