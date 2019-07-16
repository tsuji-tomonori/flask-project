# server.py
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    title = "RakugakiBattle"
    model1 = {"class": 10, "epochs": 100}
    model2 = {"class": 345, "epochs": 100}
    model_list = [model1, model2]
    return render_template("index.html", title=title, model_list=model_list)


if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port=8888)
