# server.py
from flask import Flask, render_template, request

app = Flask(__name__)

name_list = ["taro", "jiro"]


@app.route("/")
def index():
    return render_template("index.html", name_list=name_list)


@app.route("/", methods=["POST"])
def test():
    res = request.form["post_value"]
    global name_list
    name_list.append(res)
    return render_template("index.html", name_list=name_list)


if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port=8888)
