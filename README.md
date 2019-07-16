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

