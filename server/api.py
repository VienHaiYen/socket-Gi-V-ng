from typing import Text
import requests, json
from datetime import datetime

from threading import Thread
import threading
import time

from requests.models import ChunkedEncodingError, stream_decode_response_unicode
from requests.sessions import merge_setting


# hàm dùng để set thời gian thực hiện hàm func sau khoảng thời gian time (lấy từ mạng xuống)
def setInterval(func,time=1800):
    e = threading.Event()
    if time != 1800:
        if not e.wait(time):
            func()
    else:
        while not e.wait(time):
            func()
# khác với những API ở bài khác, nài mình có thể lấy dữ liệu về, có thể print ra nhưng k thể chuyển về python object được, lí do thì k biết
#các hàm để dùng để lấy api và chuyển api

def reachAPI():
    now = datetime.now()
    api_link="https://tygia.com/json.php?ran=0&rate=0&gold=1&bank=VIETCOM&date=now"
    res = requests.get(api_link).text
    res=res[2:]
    data=json.loads(res)
    data['last']=str(now)
    f=open('test_api.json','w')
    f.write(json.dumps(data))
    f.close()
    print("Updated")


def start_api():
    with open("test_api.json", "r", encoding='utf-8') as fin: #đọc myfile.json
        data = json.load(fin)
        fin.close()
    data=datetime.fromisoformat(data["last"])
    now = datetime.now()
    countdown=now-data
    if countdown.seconds > 1800:
        reachAPI()
    else:
        setInterval(reachAPI,1800-countdown.seconds)
    setInterval(reachAPI)
start_api()
print("end")