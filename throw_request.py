# throw_request.py
import urllib.request

URL = "http://192.168.10.9:8888/test"


def get_request(params):
    """ GET リクエストをサーバに投げる関数.

    Args:
        params (dict): リクエストパラメータ

    Return:
        object: http.client.HTTPResponse オブジェクト
    """
    req = urllib.request.Request('{}?{}'.format(
        URL, urllib.parse.urlencode(params)))
    with urllib.request.urlopen(req) as res:
        body = res.read()
    return body


if __name__ == "__main__":
    params = {"get_value": "from get (python)"}
    get_request(params)
