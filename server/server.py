from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import json
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
def check(account):
    f=open('infoclient.json','r')
    data=json.load(f)
    f.close()
    accounts=data['account']

    for i in range (0, len(accounts)):
        if accounts[i]["username"]==account[0] and accounts[i]["password"]==account[1]:
            return True
            break
    return False
    
SEVER.listen(1)
client, client_address=SEVER.accept()
while True:
    try:
        option=client.recv(BUFSIZE).decode(FORMAT)
        if option=="LOGIN":
            account=recvList(client)
            if check(account):
                msg='accepted'
            else:
                msg='declined'
            client.send(bytes(msg.encode(FORMAT)))
    except:
        client.close()
        print('closed')
        break


SEVER.close()