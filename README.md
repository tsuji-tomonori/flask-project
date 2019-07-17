# flask-project

[参考URL](<http://python.zombie-hunting-club.com/entry/2017/11/03/223503>)

## 1 はじめに

各モデルごとのスコア値をリアルタイム(の予定) で表示させるために, web アプリケーションを作成する.  

今回はサーバーサイドと機械学習にて Python を使用しているため, Python を使用したweb アプリケーションフレームワークであること. 簡単で学習コストが少ないものであること. の2点を満たす Flask を使用する.

はじめに, Flask の使い方を一通り実験してみた上で本題に入る.

## 2 pip で Flask をインストール

```
Microsoft Windows [Version 6.1.7601]
Copyright (c) 2009 Microsoft Corporation.  All rights reserved.

C:\Users\Owner>pip install flask
C:\Users\Owner>python
Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import flask
>>> flask.__version__
'1.1.1'
```

## 3 最小構成で実行してみる

### 3.1 ディレクトリ構成

server.py を追加

```
$ pwd
/c/Users/Owner/Desktop/flask-project
$ ls
README.md  server.py
```

### 3.2 コードの追加

```python
# server.py
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello"

if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port=8888)
```

### 3.3 プログラムの実行

> linux (xubuntu) の場合, 実行した際に表示される url をクリックするだけで表示された

事前に ipconfig 等で使用している PC の IPアドレスを確認しておく.

```
C:\Users\Owner\Desktop\flask-project>python server.py
 * Serving Flask app "server" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 332-831-366
 * Running on http://0.0.0.0:8888/ (Press CTRL+C to quit)
```

server.py をコマンドプロンプト上で実行すると上記のようになる. (はず)  

その後, [IPアドレス:ポート番号] に接続すると "Hello" と表示される.

## 4 html ファイルを表示する

3章では 文字列を表示した.

今回は, html ファイルを表示する. (というかこれがやりたいはず)

html ファイルを表示する場合は, index の戻り値を文字列ではなく, render_template 関数にすればOK.

この関数を使用するため, render_template をインポートする必要がある.

html ファイルは, templatesディレクトリに配置する必要がある (templates以外の名前だと動作しない)

【やること】

1. templates フォルダーを作成
2. templates の中に html ファイルを作成
3. index の戻り値を render_template にする

### 4.1 ディレクトリ構成

```
$ pwd
/c/Users/Owner/Desktop/flask-project
$ ls
README.md  server.py  templates/
$ ls templates/
index.html
```

### 4.2 コードの追加/変更

```python
# server.py
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port=8888)
```

```html
<!-- index.html -->
<!DOCTYPE html>
<html lang="ja">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Flask-Project</title>
</head>

<body>
    <h1>Hello from index.html</h1>
</body>

</html>
```

## 5 CSS と JavaScript を読み込む

4章 では html ファイルを表示した.

次は, CSS, JavaScript を読み込めるようにする. (これで普通のサイトっぽいものが作れるはず)

### 5.1 ディレクトリ構造

1. static フォルダーを作成 (static という名前でないと動作しない)
2. static フォルダーの中に index.css, index.js を作成

```
$ pwd
/c/Users/Owner/Desktop/flask-project
$ ls
README.md  server.py  static/  templates/
$ ls static/
index.css  index.js
```

### 5.2 コードの追加/変更

CSS, JavaScript を読み込むには, html ファイルに {{ url_for() }} を使用する.

```html
<!-- index.html -->
<!DOCTYPE html>
<html lang="ja">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <link rel="stylesheet" href="{{url_for('static', filename='index.css')}}">
    <script type="text/javascript" src="{{url_for('static', filename='index.js')}}"></script>
    <title>Flask-Project</title>
</head>

<body>
    <h1>Hello</h1>
    <h2 id="test">World !</h2>
</body>

</html>
```

``` css
/* index.css */
h1 {
    color: green;
}
```

```javascript
// index.js
window.onload = function () {
    var e = document.getElementById("test");
    e.style.color = 'red';
}
```

もし, 上手く更新されない場合, キャッシュを消すと吉.

## 6 Python の値をhtml に埋め込む

Flask では [Jinja2](<http://jinja.pocoo.org/docs/2.9/>) というテンプレートエンジンが使用できる.

これを利用することで, html ファイルにPython の値を簡単に埋め込むことができる.

### 6.1 Jinja2 インストール

```
Microsoft Windows [Version 6.1.7601]
Copyright (c) 2009 Microsoft Corporation.  All rights reserved.

C:\Users\Owner>pip install jinja2
Requirement already satisfied: jinja2 in c:\users\owner\appdata\local\programs\python\python37-32\lib\site-packages (2.10.1)
Requirement already satisfied: MarkupSafe>=0.23 in c:\users\owner\appdata\local\programs\python\python37-32\lib\site-packages (from jinja2) (1.1.1)
```

### 6.2 Jinja2 基本的な使い方

[参考URL](<https://www.python.ambitious-engineer.com/archives/760>)

[jinja2｜it-note 1.0 ドキュメント](<https://maman-it-information.readthedocs.io/ja/latest/src/python/jinja2/jinja2.html>)

#### 6.2.1 概要

| 記法      | 概要           |
| --------- | -------------- |
| {% ... %} | 制御構文       |
| {{ ... }} | 変数の埋め込み |
| {# ... #} | コメント       |

#### 6.2.2 文字列の埋め込み

```
{{ 変数名 }}
```

#### 6.2.3 ループ

```html
{% for i in items %}
  <li>{{ i }}</li>
{% endfor %}
```

#### 6.2.4 条件分岐

```html
{% if res.status == 'SUCCESS' %}
    <div class="success">{{ res.status }}</div>
{% else %}
    <div class="error">{{ res.status }}</div>
{% endif %}
```

### 6.3 コードの変更

今回は, 作成したモデルのクラス数, epochs を表形式で表示させてみる.

簡単のため, CSS, JavaScript は使用しないこととする.

```python
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
```

render_template の第二引数以降に値を指定することで, 値を渡すことが出来る.

```html
<!-- index.html -->
<!DOCTYPE html>
<html lang="ja">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Flask-Project</title>
</head>

<body>
    <p>{{ title }}</p>
    <hr>
    <p>作成したモデル</p>
    <table>
        <tr>
            <td>クラス数</td>
            <td>epochs</td>
        </tr>
        {% for x in model_list %}
        <tr>
            <td>{{ x["class"] }}</td>
            <td>{{ x["epochs"] }}</td>
        </tr>
        {% endfor %}
    </table>
</body>

</html>
```

今回はCSS, JavaScript は使用しないため, ```<link>``` ```<script>``` タグは削除した.

## 7 GET/POST で値を渡す

Flask では GET/POST を利用できる.

これを使ってデータをサーバへリクエスト送信する際に使用する.

### 7.1 GET/POST とは

[参考URL](<http://write-remember.com/archives/2530/>)

GET/POST はどちらも入力フォームのデータをサーバへリクエスト送信する際に使用する.

どちらを使うかは, 用途に応じて選択する.

#### 7.1.1 GET の特徴

- データをリクエストURLの後ろに付与して送信する
  - webサーバやプロキシサーバのアクセスログなどに残る
  - ブックマーク等も可能
- 他の人がURL を見ると, 入力したデータが丸見え
  - ログイン画面等では使用NG (ID, パスワードが丸見えになるため)
- URL の後ろにデータを付与するためデータ量に制限が掛かる
- データの取得が簡単
  - HTTPヘッダ情報に含まれるため
- テキストデータのみ送信可能

#### 7.1.2 POST の特徴

* データ量が多い場合POST を使用する
* 取得がちょっと大変
  * BODY部分(form) に含まれるため
* テキスト, バイナリどちらでも送信可能
* POST 送信後にブラウザボタン押下で有効期限切れが発生する可能性がある

### 7.2 コードの変更

1. index.html から /test に GET/POST をする
2. server.py にてその値を取得し表示する

```html
<!-- index.html -->
<!DOCTYPE html>
<html lang="ja">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Flask-Project</title>
</head>

<body>
    <form action="/test" method="get">
        <button name="get_value" value="from get">get submit</button>
    </form>
    <form action="/test" method="post">
        <button name="post_value" value="from post">get submit</button>
    </form>
</body>

</html>
```

 index.html ではボタンを二つ作成し、/test に get と post リクエストを投げられるように変更.

```python
# server.py
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/test", methods=["GET", "POST"])
def test():
    if request.method == "GET":
        res = request.args.get("get_value")
    elif request.method == "POST":
        res = request.form["post_value"]

    return res

if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port=8888)
```

GET/POST で値を取得するには、request をインポートする.

```@app.route("/test", methods=["GET", "POST"])``` にて GET と POST の受け取りを指定している.

GET だけを受け取るときには, ```methods=["GET"]``` のようにする.

また, それぞれの値の取得方法は以下の通り.

|      | 値を取得する関数       |
| ---- | ---------------------- |
| GET  | ```request.args.get``` |
| POST | ```request.form```     |

## 8 外部のPython 関数から GET/POST する

[参考URL1](<https://qiita.com/hoto17296/items/8fcf55cc6cd823a18217>)

[参考URL2](<https://python.civic-apps.com/http-request-post-get/>)

そろそろ本題に入る.

predict.py にて各モデルのスコアをサーバに投げる必要がある. その方法を模索する.

まず, 問題を単純化するため, 外部のPython 関数からサーバに文字列を GET/POST する.

### 8.1 ディレクトリ構成

throw_request.py を追加

```
$ pwd
/c/Users/Owner/Desktop/flask-project
$ ls
README.md  server.py  static/  templates/  throw_request.py
```

### 8.2 GET リクエストを投げる

`Request` オブジェクトを作成し、`urlopen` に渡すことでリクエストが送信される.

今回は7章のように get_value を from get (python) としてサーバにリクエストを投げる.

```python
# throw_request.py
import urllib.request

URL = "" # URL を記述する


def get_request(params):
    """ GET リクエストをサーバに投げる関数.

    Args:
        params (dict): リクエストパラメータ

    Return:
        str: サーバから受け取った文字列
    """
    req = urllib.request.Request('{}?{}'.format(
        URL, urllib.parse.urlencode(params)))
    with urllib.request.urlopen(req) as res:
        body = res.read()
    return body.decode("utf-8")


if __name__ == "__main__":
    params = {"get_value": "from get (python)", }
    print(get_request(params))
```

### 8.3 POST リクエストを投げる

POSTリクエストする場合はRequestオブジェクトを作ってdataを渡す必要がある.
dataはURLエンコードをしなければならないし, 送信データ文字コードを指定してバイト文字列を作る必要がある.

以下, 該当する関数のみ.

```python
# throw_request.py
import urllib.parse

def post_request(data):
    """ POST リクエストをサーバに投げる関数.

    Args:
        data (dict): リクエストパラメータ

    Reutrn:
        str: サーバから受け取った文字列
    """
    data = urllib.parse.urlencode(data).encode('utf-8')
    req = urllib.request.Request(URL, data=data)
    with urllib.request.urlopen(req) as res:
        body = res.read().decode()
    return body

if __name__ == "__main__":
    #params = {"get_value": "from get (python)", }
    #print(get_request(params))
    data = {"post_value": "from post (python)", }
    print(post_request(data))
```

### 8.4 まとめ

8章のプログラムを全てつなげると以下のようになる.

```python
# throw_request.py
import urllib.request
import urllib.parse

URL = "" # URL を記述する


def get_request(params):
    """ GET リクエストをサーバに投げる関数.

    Args:
        params (dict): リクエストパラメータ

    Return:
        str: サーバから受け取った文字列
    """
    req = urllib.request.Request('{}?{}'.format(
        URL, urllib.parse.urlencode(params)))
    with urllib.request.urlopen(req) as res:
        body = res.read()
    return body.decode("utf-8")


def post_request(data):
    """ POST リクエストをサーバに投げる関数.

    Args:
        data (dict): リクエストパラメータ

    Reutrn:
        str: サーバから受け取った文字列
    """
    data = urllib.parse.urlencode(data).encode('utf-8')
    req = urllib.request.Request(URL, data=data)
    with urllib.request.urlopen(req) as res:
        body = res.read().decode()
    return body


if __name__ == "__main__":
    params = {"get_value": "from get (python)", }
    print(get_request(params))
    data = {"post_value": "from post (python)", }
    print(post_request(data))
```

## 9 POST されたデータをhtml に埋め込む

[参考にしたいURL](<https://codeday.me/jp/qa/20190207/231487.html>)

[実際に参考にしたURL](<https://www.sejuku.net/blog/25316>)

8章にて, predict.py から サーバへスコアを投げること (の実験)に成功した.

次は, この値を受けて html の内容を変更する.

【思いついた方法】

1. 受け取ったデータを list に追加
2. list のデータ元に jinja2 を用いて html に埋め込む
3. 埋め込んだ html を表示
4. 一定間隔でページをリロード

【今回あきらめたこと】

リロードせずにページを更新 (想像以上に知らないことが多かった)

### 9.1 コードの変更

```python
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
```

name_list に POST で受け取った値を追加した. その後 html を返す.

```html
<!-- index.html -->
<!DOCTYPE html>
<html lang="ja">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <script type="text/javascript" src="{{url_for('static', filename='index.js')}}"></script>
    <title>Flask-Project</title>
</head>

<body>
    {% for name in name_list %}
    <p>{{ name }}</p>
    {% endfor %}
</body>

</html>
```

受け取った name_list を順に表示

```javascript
// index.js
// reloadの応用方法
// キャッシュを利用してリロードする方法
function doReloadWithCache() {

    // キャッシュを利用してリロード
    window.location.reload(false);

}

window.addEventListener('load', function () {

    // ページ表示完了した5秒後にリロード
    setTimeout(doReloadWithCache, 5000);

});
```

[参考URL](<https://www.sejuku.net/blog/25316>) せめて自動でリロードさせるために 5s ごとに キャッシュを利用してリロード.

```python
# throw_request.py
import urllib.request
import urllib.parse
import sys

URL = "" # URL 記述


def get_request(params):
    """ GET リクエストをサーバに投げる関数.

    Args:
        params (dict): リクエストパラメータ

    Return:
        str: サーバから受け取った文字列
    """
    req = urllib.request.Request('{}?{}'.format(
        URL, urllib.parse.urlencode(params)))
    with urllib.request.urlopen(req) as res:
        body = res.read()
    return body.decode("utf-8")


def post_request(data):
    """ POST リクエストをサーバに投げる関数.

    Args:
        data (dict): リクエストパラメータ

    Reutrn:
        str: サーバから受け取った文字列
    """
    data = urllib.parse.urlencode(data).encode('utf-8')
    req = urllib.request.Request(URL, data=data)
    with urllib.request.urlopen(req) as res:
        body = res.read().decode()
    return body


if __name__ == "__main__":
    args = sys.argv[1:]
    data = {"post_value": args[0], }
    post_request(data)
    print("post data", data)
```

コマンドライン引数に入力された値を POST するように変更.

## 10 CSS フレームワークを使用して見た目を綺麗にする

~~綺麗なレイアウトを作成するCSS コード力も美的センスもなかった~~

最低限の見た目を確保するために, CSS フレームワークの力を借りて UI を作成する.

今回は [Materialize](<https://materializecss.com/>) を使用してみる.

### 10.1 導入

CDN で導入する [公式URL](<https://materializecss.com/getting-started.html>)

```html
<!-- Compiled and minified CSS -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css">

    <!-- Compiled and minified JavaScript -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/js/materialize.min.js"></script>
```

```<head>```  に追加する

実際に上手く動くかテストしてみる.

各要素をカード状にして, かつ文字の色を変えてみる.

```html
<!-- index.html -->
<!DOCTYPE html>
<html lang="ja">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <script type="text/javascript" src="{{url_for('static', filename='index.js')}}"></script>
    <!-- Compiled and minified CSS -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css">
    <!-- Compiled and minified JavaScript -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/js/materialize.min.js"></script>

    <title>Flask-Project</title>
</head>

<body>
    {% for name in name_list %}
    <div class="card-panel">
        <span class="blue-text text-darken-2">{{ name }}</span>
    </div>
    {% endfor %}
</body>

</html>
```

