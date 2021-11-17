import requests, json
from datetime import datetime

from threading import Thread
import threading
import time

from requests.auth import HTTPDigestAuth

def setInterval(func,time):
    e = threading.Event()
    while not e.wait(time):
        func()

def reachAPI():
    now = datetime.now()
    print("now =", now)
    print('Cap nhat API thanh cong\n')
    # api_link="https://tygia.com/json.php?ran=0&rate=0&gold=1&bank=VIETCOM&date=now"
    api_link="https://vapi.vnappmob.com/api/v2/exchange_rate/vcb"
    key_api=json.loads(requests.get("https://vapi.vnappmob.com/api/request_api_key?scope=exchange_rate").text)
    key=key_api['results']
    api_info=json.loads(requests.get("https://vapi.vnappmob.com/api/v2/exchange_rate/vcb", headers={"Authorization":"Bearer "+key}).text)
    # print(api_info)
    api_link2="https://api.covid19api.com/summary"

    data = json.dumps(api_info)

    f=open('money.json','w+', encoding='UTF-8')
    f.write(data)
    f.close()

    result=api_info['results']
    return result

def startFetchAPI():
    setInterval(reachAPI,600)

def outputResult(result):
    print('Gia tien mat: '+str(result["buy_cash"]))
    print('Gia chuyen khaon: '+str(result["buy_transfer"]))
    print('Gia ban ra: '+str(result["sell"])+'\n')

def findInfo(value):
    result=-1
    print('Input currency unit')
    temp1=input()
    for i in range(0, len(value)):
        if value[i]["currency"].lower() == temp1.lower():
            result = i
            break
    if result==-1:
        print('Wrong')
    else:
        outputResult(value[result])


def searching():
    while True:
        findInfo(value)


value=reachAPI()

try:
    t1=threading.Thread(target=searching)
    t2=threading.Thread(target=startFetchAPI)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
except:
    print('error')

reachAPI()