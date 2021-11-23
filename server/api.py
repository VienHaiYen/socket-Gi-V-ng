from typing import Text
import requests, json
from datetime import datetime

from threading import Thread
import threading
import time

from requests.models import ChunkedEncodingError, stream_decode_response_unicode
from requests.sessions import merge_setting

# hàm dùng để set thời gian thực hiện hàm func sau khoảng thời gian time (lấy từ mạng xuống)
def setInterval(func,time):
    e = threading.Event()
    while not e.wait(time):
        func()
# khác với những API ở bài khác, nài mình có thể lấy dữ liệu về, có thể print ra nhưng k thể chuyển về python object được, lí do thì k biết
#các hàm để dùng để lấy api và chuyển api
'''
<tên biến>=json.loads()  -> chuyển thông tin từ dạng json về dạng object có thể sr dụng trong python (dạng ở đây tức là dữ liệu có thể dùng được)
trong json.loads()  -> sẽ đưa response của request lấy api từ mạng xuống, dưới dạng text nên cú pháp viết thông thường sẽ là:
<tên biến>=json.loads(requests.get(<link>).text)

JSON là file dùng để lưu trữ dữ liệu dưới dạng chuỗi "<key>":"<value>" một cách nhỏ gọn và có thể tái dùng nhiều lần, được dùng như một dạng văn bản lưu trữ
để chuyển một object sang một chuỗi thì hàm dùng là ngược lại với loads là json.dumps(<object đó>)

đó là thao tác với các biến hay các chuỗi, còn nếu làm việc với file thì sẽ là .load và .dump

muốn dùng thì thêm vào thư viện resquest và json
'''


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
    api_link2="https://api.covid19api.com/summary"
    api_info = requests.get(api_link).text
    # print(type(api_info))

    # lúc này api_info có dạng chuỗi, lưu ý được là sau khi chuyển về dạng json thì trong file xuất hiện điểm bất thường là dư ra chuỗi
    # "\ufeff\n -> các dòng lệnh (a) nhằm loại bỏ dòng dư thừa đó đi
    # đồng thời chuỗi json lúc này gặp lỗi k loads được còn là do phần sau của json, bắt đầu từ ,\\"time\\" do không đuọc bỏ vào "" đúng với cú pháp json


    data = json.dumps(api_info)

    a='"\\ufeff\n' #(a)
    data2 = data.lstrip(a) #(a)

    a='n' #(a)
    data3 ='\"'+ data2.lstrip(a)   #(a)

    a=data3.split(',\\"time\\"')  #chia chuỗi data3 thành 2 phần được ngăn cách bởi ,\\"time\\"

    info=a[0]+'\"'  #(a) lấy phần tử đầu tiên sau khi tách chuối dât3 thành 2 phần

    result=json.loads(info) +'}' #thành công lấy được dữ liệu

    f=open('myfile.json','w+', encoding='UTF-8') # viết vào myfile.json
    f.write(result)
    res = requests.get(api_link).text
    res=res[2:]
    data=json.loads(res)
    data['last']=str(now)
    f=open('test_api.json','w')
    f.write(json.dumps(data))
    f.close()
    print("Updated")


    with open("myfile.json", "r", encoding='utf-8') as fin: #đọc myfile.json
        data = json.load(fin)
        fin.close()
    # print(type(data))
    x= data['golds']
    # print(type(x))

    x1=x[0]
    # print(type(x1))

    value=x1['value']
    # print(type(value))
    # print(value)
    return value

def startFetchAPI():
    setInterval(reachAPI,600)


#phần timf kiếm thì không cần quan tâm nữa vì nó đã có trong cgui rồi
def outputResult(result):
    print('Gia mua vao: '+result["buy"])
    print('Gia ban ra: '+result["sell"]+'\n\n')

def findInfo(value):
    result=-1
    print('Input your gold brand')
    temp1=input()
    print('Input your gold company')
    temp2=input()
    for i in range(0, len(value)):
        if value[i]["brand"].lower() == temp1.lower() and value[i]["company"].lower() == temp2.lower():
            result = i
            break
    if result==-1:
        print('Nothing has this brand')
    else:
        outputResult(value[result])


def searching():
    while True:
        findInfo(value)


value=reachAPI()


#thực hiện xử lí đa luồng là vừa tìm thông tin từ người dùng vừa canh thời gian sao cho đủ thời gian quy định thì sẽ chạy lại 1 lần
try:
    t1=threading.Thread(target=searching)
    t2=threading.Thread(target=startFetchAPI)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
except:
    print('error')
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
