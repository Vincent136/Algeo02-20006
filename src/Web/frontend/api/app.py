import time
from flask import Flask

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route("/add_todo", methods=["POST"])
def add_todo():
    todo_data = request.get_json()


# def getCurrentTime():
#     return {"time": time.time()}


if __name__ == "__main__":
    app.run()
