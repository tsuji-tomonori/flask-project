# throw_request.py
import urllib.request
import urllib.parse
import sys

URL = "http://192.168.10.9:8888/"


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
