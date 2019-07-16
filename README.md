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