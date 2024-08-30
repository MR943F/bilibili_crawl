import json
import os
from time import sleep
import fake_useragent
import httpx
import qrcode
import requests
from PIL import Image

user_agent = fake_useragent.UserAgent()
header = {
    'Referer': 'https://www.bilibili.com/',
    'User-Agent': user_agent.random
}


def ger_qrcode_url():
    url = 'https://passport.bilibili.com/x/passport-login/web/qrcode/generate?source=main-fe-header'

    response = requests.get(url=url, headers=header)
    html = response.text
    jsom_data = json.loads(html)
    qrcode_url = jsom_data['data']['url']
    qrcode_key = jsom_data['data']['qrcode_key']
    data = {'url': qrcode_url, 'qrcode_key': qrcode_key}
    return data


def make_qrcode(data):
    qr = qrcode.QRCode(
        version=10,
        error_correction=qrcode.ERROR_CORRECT_L,
        box_size=20,
        border=8
    )
    qr.add_data(data['url'])
    qr.make()
    img = qr.make_image()
    try:
        img.save('user_cookie//2.png')
        re = Image.open('user_cookie/2.png')
        re1 = re.resize((300, 300))
        re1.save('user_cookie/re.png')
        os.remove('user_cookie/2.png')
    except FileNotFoundError:
        os.mkdir('user_cookie')


def get_cookie(data):
    token = data['qrcode_key']
    url = f'https://passport.bilibili.com/x/passport-login/web/qrcode/poll?qrcode_key={token}&source=main-fe-header'
    while True:
        with httpx.Client() as client:
            login_json = client.get(url=url, headers=header)
            cookie_json = json.loads(login_json.text)
            code = cookie_json['data']['code']
            sleep(1)
        if code == 0:
            cookie = dict(client.cookies)
            save_cookie(cookie)
            os.remove('user_cookie/re.png')
            break


def save_cookie(data):
    try:
        with open('user_cookie//cookie.json', 'w') as f:
            json.dump(data, f, ensure_ascii=False)
    except FileNotFoundError:
        os.mkdir('user_cookie')
        with open('user_cookie//cookie.json', 'w') as f:
            json.dump(data, f, ensure_ascii=False)


def delete_cookie():
    with open('user_cookie//cookie.json', 'r+') as f:
        f.truncate(0)


def delete_qrcode():
    with open('user_cookie/1.jpg', 'r+') as f:
        f.truncate(0)
