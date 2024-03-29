# server.py
from flask import Flask, render_template, request, url_for
import glob
import os
import csv

app = Flask(__name__)

model_info = {}
labels = {}


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/What is RakugakiBattle")
def what_is_rakugakibattle():
    return render_template("rakugakibattle.html")

@app.route("/What is AI")
def what_is_ai():
    return render_template("ml.html")

<<<<<<< HEAD
@app.route("/Program information")
def Program_information():
    return render_template("prog.html")

=======
>>>>>>> b2212a272232be8dbbc0f5687c996c9800346560

@app.route("/log/<model_name>", methods=["POST", "GET"])
def log_model(model_name):
    global model_info
    if request.method == "POST":
        value = []
        for key in model_info[model_name]["heads"]:
            res = request.form[key]
            value.append(res)
        model_info[model_name]["value_list"].append(value)
        with open('model/' + model_name + "/log.csv", 'a') as f:
            writer = csv.writer(f)
            writer.writerow(value)
    (acc, ave) = cal(model_name)
    return render_template("log.html",
                           heads=model_info[model_name]["heads"],
                           value_list=model_info[model_name]["value_list"],
                           acc=acc,
                           ave=ave)
@app.route("/model_info/<model_name>")
def model(model_name):
    global model_info
    return render_template("model.html", model_name=model_name, info=model_info[model_name]["info"])


def init():
    """ 初期化する関数.

    model フォルダーを読み込み, model_info の設定をする
    """
    path = "./model"
    files = os.listdir(path)
    # モデル名を フォルダー名から取得
    files_dir = [f for f in files if os.path.isdir(os.path.join(path, f))]
    global model_info, labels
    for model in files_dir:
        model_info[model] = {}
        # label.csv を開き ラベルを取得する
        with open(path + "/" + model + "/label.csv", "r") as f:
            reader = csv.DictReader(f)
            l = [row for row in reader]
        # ラベルを labels にセットする
        labels[model] = {key: int(value) + 2 for key, value in l[0].items()}
        # model_info の設定
        head = ["odai", "pre"]
        model_info[model]["heads"] = head + [key for key in l[0]]
        model_info[model]["value_list"] = []
        # info.csv を開き 情報を取得する
        with open(path + "/" + model + "/info.csv", "r") as f:
            reader = csv.DictReader(f)
            l = [row for row in reader]
        model_info[model]["info"] = {key: value for key, value in l[0].items()}


def cal(model):
    """ 正答率, 平均スコアを算出する関数.

    Args:
        model (str): モデル名

    Return:
        int: 正答率
        int: 平均スコア

    """
    global model_info, labels
    acc_ave = 0
    acc_count = 0
    for score in model_info[model]["value_list"]:
        if score[0] == score[1]:
            acc_ave += float(score[labels[model][score[0]]])
            acc_count += 1
    if acc_count == 0:
        return (0, 0)
    return (acc_count/len(model_info[model]["value_list"]), acc_ave/acc_count)


if __name__ == "__main__":
    init()
    app.debug = True
    app.run(host="0.0.0.0", port=8888)
