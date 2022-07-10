
import config
import requests


def push_to_wechat(text,desp,secretKey):
    """
    通过serverchan将消息推送到微信
    :param secretKey: severchan secretKey
    :param text: 标题
    :param desp: 内容
    :return resp: json
    """
    url = f'http://sc.ftqq.com/{secretKey}.send'
    session = requests.Session()
    data = {'title':text,'desp':'messagecontent'}
    resp = session.post(url,data = data)
    print(text)
    print(resp)
    #return resp.json()
    return 1


if __name__ == '__main__':
    resp = push_to_wechat(text = 'test', desp='hi', secretKey= config.SERVERCHAN_SECRETKEY)
    print(resp)
