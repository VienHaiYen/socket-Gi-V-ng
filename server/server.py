from codecs import encode
from re import search
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import json
from typing import Dict

from PIL.ImagePalette import load



HOST='127.0.0.1'
PORT=33000
BUFSIZE=1024
FORMAT="utf8"
SEVER=socket(AF_INET,SOCK_STREAM)
SEVER.bind((HOST,PORT))
def recvList(conn):
    list = []

    item = conn.recv(1024).decode(FORMAT)
    while (item != "end"):
        
        list.append(item)
        #response
        conn.sendall(item.encode(FORMAT))
        item = conn.recv(1024).decode(FORMAT)
    
    return list
def sendResult(client,list):
    msg=json.dumps(list,ensure_ascii=False)
    length=len(msg)
    client.send(bytes(str(length).encode(FORMAT)))
    client.recv(BUFSIZE)
    client.sendall(bytes(msg.encode(FORMAT)))
def checkLogin(client):
    account=recvList(client)
    f=open('infoclient.json','r')
    data=json.load(f)
    f.close()
    accounts=data['account']

    msg='declined'
    for i in range (0, len(accounts)):
        if accounts[i]["username"]==account[0] and accounts[i]["password"]==account[1]:
            msg='accepted'
            break
    client.send(bytes(msg.encode(FORMAT)))
def checkSignin(client):
    account=recvList(client)
    f=open('infoclient.json','r')
    data=json.load(f)
    f.close()
    accounts=data['account']

    msg='signin succeed'
    for i in range (0, len(accounts)):
        if accounts[i]["username"]==account[0]:
            msg='signin failed'
            break
    client.send(bytes(msg.encode(FORMAT)))
    if msg=='signin succeed':
        x={
            'id':len(accounts)+1,
            'username': account[0],
            'password': account[1]
        }
        data["account"].append(x)
        f=open('infoclient.json','w+')
        f.write(json.dumps(data))
        f.close()
    print(msg)
def search(client):
    # lấy search keys
    brand,company=recvList(client)
    print(brand)
    print(company)
    # mở file lấy data
    with open('myfile.json', 'r', encoding='utf-8') as f:
        file=json.load(f)
        f.close()
    data= file['golds'][0]['value']
    # lấy kết quả
    result=[]
    if brand!='none' and company!='none':
        for i in range(0, len(data)):
            if data[i]["brand"].lower() == brand.lower() and data[i]['company'].lower() == company.lower():
                result.append(data[i])
    elif brand!='none' and company=='none':
        for i in range(0, len(data)):
            if data[i]["brand"].lower() == brand.lower():
                result.append(data[i])
    elif brand=='none' and company!='none':
        for i in range(0, len(data)):
            if data[i]['company'].lower() == company.lower():
                result.append(data[i])
    else:
        result=data
    sendResult(client,result)


def acceptConnection():
    while True:
        try:
            client, client_address=SEVER.accept()
            Thread(target=handleClient,args=(client,)).start()
        except KeyboardInterrupt:
            break

def handleClient(client):
    while True:
        try:
            option=client.recv(BUFSIZE).decode(FORMAT)
            print(option)
            if option=="LOGIN":
                checkLogin(client)
            elif option=='SIGNIN':
                checkSignin(client)
            elif option=='SEARCH':
                search(client)
            elif option=='exit':
                client.close()
                print('closed')
                break
        except:
            client.close()
            print('closed')
            break
SEVER.listen(5)
acceptConnection()


SEVER.close()