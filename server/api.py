import requests, json
from datetime import datetime

from threading import Thread
import threading
import time


def setInterval(func,time):
    e = threading.Event()
    while not e.wait(time):
        func()

def reachAPI():
    now = datetime.now()
    print("now =", now)
    print('Cap nhat API thanh cong\n')
    api_link="https://tygia.com/json.php?ran=0&rate=0&gold=1&bank=VIETCOM&date=now"
    api_link2="https://api.covid19api.com/summary"
    api_info = requests.get(api_link).text


    # print(type(api_info))
    data = json.dumps(api_info)

    a='"\\ufeff\n'
    data2 = data.lstrip(a)

    a='n'
    data3 ='\"'+ data2.lstrip(a)

    a=data3.split(',\\"time\\"')

    info=a[0]+'\"'

    result=json.loads(info) +'}'

    f=open('myfile.json','w+', encoding='UTF-8')
    f.write(result)
    f.close()

    with open("myfile.json", "r", encoding='utf-8') as fin:
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

try:
    t1=threading.Thread(target=searching)
    t2=threading.Thread(target=startFetchAPI)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
except:
    print('error')
