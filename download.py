import re
from get_cookie import *
import fake_useragent


def user_info_loaded():
    try:
        with open('user_cookie/cookie.json', 'r') as f:
            user_info = json.loads(f.read())
            cookie = {
                'SESSDATA': user_info['SESSDATA'],
                'bili_jct': user_info['bili_jct']
            }
            return cookie
    except FileNotFoundError:
        cookie = {
            'SESSDATA': '',
            'bili_jct': ''
        }
        return cookie


user_agent = fake_useragent.UserAgent()
header = {
    'Referer': 'https://www.bilibili.com/',
    'User-Agent': user_agent.random
}


def get_html(url):
    response = requests.get(url=url, headers=header, cookies=user_info_loaded(), timeout=10000)

    return response.text


def find_title(html):
    title = re.findall('<title data-vue-meta="true">(.*?)</title>', html)[0]
    return title


def replace_error_character(title):
    pattern = r'[\\/:*?"<>|]'
    text = re.sub(pattern, "", title)
    return text


def find_bv(url):
    BV = re.findall("BV\w{10}", url)[0]
    return BV


def resolution(html):
    video_data = re.findall('<script>window.__playinfo__=(.*?)</script', html)[0]  # 选取最高画质
    data = json.loads(video_data)
    height_indexes = {}
    for height_index in range(len(data['data']['dash']['video'])):
        video_url = data['data']['dash']['video'][height_index]['width']
        height_indexes[video_url] = height_index
    return height_indexes


def get_audiodata(html):
    data = re.findall('<script>window.__playinfo__=(.*?)</script', html)  # 选取最高画质

    jsom_data = json.loads(data[0])
    audio_url = jsom_data['data']['dash']['audio'][0]['baseUrl']
    return audio_url


def get_videodata(html, index):
    data = re.findall('<script>window.__playinfo__=(.*?)</script', html)  # 选取最高画质

    jsom_data = json.loads(data[0])
    video_url = jsom_data['data']['dash']['video'][index]['baseUrl']
    return video_url
