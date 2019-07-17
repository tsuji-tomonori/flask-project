# server.py
from flask import Flask, render_template, request

app = Flask(__name__)

model_name = "model1"
heads = ['odai', 'pre', 'axe', 'airplane', 'apple', 'banana',
         'bicycle', 'car', 'donut', 'fish', 'hat', 'house']
value_list = [["banana", "banana", 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]]


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/log", methods=["POST", "GET"])
def log_model():
    if request.method == "POST":
        value = []
        for key in heads:
            res = request.form[key]
            value.append(res)
        global value_list
        value_list.append(value)
        return render_template("model.html", model_name=model_name, heads=heads, value_list=value_list)
    else:
        return render_template("model.html", model_name=model_name, heads=heads, value_list=value_list)


if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port=8888)
