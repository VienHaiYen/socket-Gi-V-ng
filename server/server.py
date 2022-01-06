from re import search
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import json
from typing import Dict
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from PIL.ImagePalette import load
from threading import Event
from datetime import datetime, time
import requests
# API
def setInterval(func,time=1800):
    e = Event()
    if time != 1800:
        if not e.wait(time):
            func()
    else:
        while not e.wait(time):
            func()

def reachAPI():
    now = datetime.now()
    api_link="https://tygia.com/json.php?ran=0&rate=0&gold=1&bank=VIETCOM&date=now"
    res = requests.get(api_link).text
    res=res[2:]
    data=json.loads(res)
    with open("data.json", "r", encoding='utf-8') as fin:
        file = json.load(fin)
        fin.close()
    file['last']=str(now)
    append=True
    try:
        for i in range(0,len(file['golds'])):
            if data['golds'][0]['date']==file['golds'][i]['date']:
                file['golds'][i]=data['golds'][0]
                append=False
                break
        if append:
            file['golds'].insert(0,data['golds'][0])
    except:
        pass
    f=open("data.json","w")
    f.write(json.dumps(file))
    f.close()
    print("Updated")

def start_api():
    with open("data.json", "r", encoding='utf-8') as fin:
        data = json.load(fin)
        fin.close()
    data=datetime.fromisoformat(data["last"])
    now = datetime.now()
    countdown=now-data
    if countdown.total_seconds() > 1800:
        reachAPI()
    else:
        setInterval(reachAPI,1800-countdown.total_seconds())
    setInterval(reachAPI)
# GUI Sever - sử dụng tkinter
my_window =Tk()
my_window.title('Server Version')
my_window.geometry("550x350")
load=Image.open('marketing.jpg')
render=ImageTk.PhotoImage(load)
img=Label(my_window, image=render)
img.place(x=0, y=-50)
def __init__(my_window):
    welcomeBoss = Label(my_window, text="Hello server", bg="#F4F8FB")
    welcomeBoss.config(font=("Humblle Rought All Caps",30))
    welcomeBoss.place(x=180,y=50)
    btn_start_frame=Frame(my_window)
    btn_start_frame.configure(bg="#fff", width=10)
    btn_start_frame.place(x=160,y=140)
    clientsList=Button(btn_start_frame, text='Clients\' Information', width=25, height=1, background='#7FBDEA', fg="#fff", command=pageOne)
    clientsList.pack(pady=5)
    clientsList.config(font=(".VnSouthern",10, "bold"))
    onlineClient=Button(btn_start_frame, text='Accounts online now',width=25, height=1, background='#7FBDEA', fg="#fff", command=pageTwo)
    onlineClient.pack(pady=5)
    onlineClient.config(font=(".VnSouthern",10, "bold"))
    dataInserver=Button(btn_start_frame, text='Data about gold',width=25, height=1,background='#7FBDEA', fg="#fff",command=pageThree)
    dataInserver.pack(padx=20, pady=3)
    dataInserver.config(font=(".VnSouthern",10, "bold"))

def display(x,accounts):
    main_frame=Frame(x)
    main_frame.pack(fill=BOTH,expand=1)
    my_canvas=Canvas(main_frame,bg="#fff")
    my_canvas.pack(side=LEFT, fill=BOTH,expand=1)
    my_scrollbar=ttk.Scrollbar(main_frame, orient=VERTICAL,command=my_canvas.yview)
    my_scrollbar.pack(side=RIGHT, fill=Y)
    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.config(bg="#fff")
    my_canvas.bind('<Configure>', lambda e:my_canvas.configure(scrollregion=my_canvas.bbox("all")))
    second_frame=Frame(my_canvas)
    second_frame.configure(bg="#fff")
    my_canvas.create_window((0,0), window=second_frame, anchor="nw")
    n=1
    for i in range(0, len(accounts)):
        x=accounts[i]
        print(x['username'] + '   '+ x['password'])
        num=Label(second_frame, text=n, width=10,bg="#fff")
        num.grid(column=1, row=n)
        n1=Label(second_frame, text=x['username'],bg="#fff", width=20)
        n1.grid(column=2, row=n)
        n2=Label(second_frame, text=x['password'],bg="#fff",width=20)
        n2.grid(column=3, row=n)
        n=n+1

def pageOne():
    pop=Toplevel()
    pop.geometry("400x500")
    pop.title('Danh sach tai khoan')
    tempIMG=(Image.open("111.jpg"))
    startImg=tempIMG.resize((400,200),Image.ANTIALIAS)
    new_image= ImageTk.PhotoImage(startImg)
    label = Label(pop, image=new_image)
    label.image = new_image
    label.place(x=-5, y=0)

    lbl=Label(pop, text='TOTAL ACCOUNTS',bg="#fff",font=("iCiel Pacifico",15))
    lbl.pack(padx=50, pady=5)
    with open('infoclient.json', 'r') as f:
        data=json.load(f)
        f.close()
    accounts=data['account']
    lbl=Label(pop,text='Hien co ' + str(len(accounts)) + ' tai khoan da dang ki',bg="#fff").pack()
    display(pop,accounts)

def pageTwo():
    pop1=Toplevel()
    pop1.geometry("400x500")
    pop1.title('Danh sach tai khoan')

    tempIMG=(Image.open("111.jpg"))
    startImg=tempIMG.resize((400,200),Image.ANTIALIAS)
    new_image= ImageTk.PhotoImage(startImg)
    label = Label(pop1, image=new_image)
    label.image = new_image
    label.place(x=-5, y=0)

    with open('onlinelist.json', 'r') as f:
        data=json.load(f)
        f.close()
        print(data)
    accounts=data['account']
    lbl=Label(pop1, text='Online  NOW',bg="#fff",font=("iCiel Pacifico",15))
    lbl.pack(padx=50, pady=5)
    display(pop1,accounts)

def clearFrame():
    # destroy all widgets from frame
    main_frame.destroy()

choosenvalue=-1
def getCombobox():
    try:
        clearFrame()
    except:
        pass
    global main_frame
    main_frame=Frame(display_frame)
    main_frame.configure(bg="#fff")
    loading=Label(main_frame,text="Loading",font=("Arial",10,"italic"),fg="grey",bg="#fff", width=15)
    loading.pack(fill=BOTH)
    main_frame.pack(fill=BOTH,expand=1)
    main_frame.update_idletasks()

    my_canvas=Canvas(main_frame)
    my_canvas.pack(side=LEFT, fill=BOTH,expand=1)
    my_canvas.configure(bg="#fff")
    my_scrollbar=ttk.Scrollbar(main_frame, orient=VERTICAL,command=my_canvas.yview)
    my_scrollbar.pack(side=RIGHT, fill=Y)
    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind('<Configure>', lambda e:my_canvas.configure(scrollregion=my_canvas.bbox("all")))

    global second_frame
    second_frame=Frame(my_canvas)
    second_frame.configure(bg="#fff")
    my_canvas.create_window((0,0), window=second_frame, anchor="nw")
    out_frame=Frame(second_frame)
    out_frame.configure(bg="#fff")

    choosenvalue=daychoosen.get()
    num=-1
    for i in range(0, len(combdate)):
        print(combdate[i])
        if combdate[i] == choosenvalue:
            num=i
            break
    with open('data.json', 'r', encoding='utf-8') as f:
        value=json.load(f)
        f.close()
    value=value['golds'][num]['value']
    n=1
    Label(out_frame, text="Company",bg="#fff",font=("Arial",10,"bold"),fg="blue").grid(column=1,row=0)
    Label(out_frame, text="Brand",bg="#fff",font=("Arial",10,"bold"),fg="blue").grid(column=2,row=0)
    Label(out_frame, text="Brand1",bg="#fff",font=("Arial",10,"bold"),fg="blue").grid(column=3,row=0)
    Label(out_frame, text="Type",bg="#fff",font=("Arial",10,"bold"),fg="blue").grid(column=4,row=0)
    Label(out_frame, text="Buy",bg="#fff",font=("Arial",10,"bold"),fg="blue").grid(column=5,row=0)
    Label(out_frame, text="Sell",bg="#fff",font=("Arial",10,"bold"),fg="blue").grid(column=7,row=0)
    for i in range(0, len(value)):
        Label(out_frame,text=n,bg="#fff").grid(column=0,row=n)
        Label(out_frame, text=value[i]['company'],bg="#fff").grid(column=1,row=n)
        Label(out_frame, text=value[i]['brand'],bg="#fff").grid(column=2,row=n)
        Label(out_frame, text=value[i]['brand1'],bg="#fff").grid(column=3,row=n)
        Label(out_frame, text=value[i]['type'],bg="#fff").grid(column=4,row=n)
        Label(out_frame, text=value[i]['buy'],bg="#fff").grid(column=5,row=n)
        Label(out_frame, text="      ",bg="#fff").grid(column=6,row=n)
        Label(out_frame, text=value[i]['sell'],bg="#fff").grid(column=7,row=n)
        n=n+1
    out_frame.pack(fill=BOTH,expand=True)
    out_frame.wait_visibility()
    loading.destroy()
def pageThree():
    pop2=Toplevel()
    pop2.geometry("700x500")
    pop2.title('Toan bo du lieu')
    pop2.configure(bg="#fff")

    tempIMG=(Image.open("111.jpg"))
    startImg=tempIMG.resize((700,300),Image.ANTIALIAS)
    new_image= ImageTk.PhotoImage(startImg)
    label = Label(pop2, image=new_image)
    label.image = new_image
    label.place(x=-5, y=0)

    Label(pop2, text="BẢNG GIÁ VÀNG",font=("iCiel Pacifico",15),bg="#fff").pack()
    combo_frame=Frame(pop2)
    combo_frame.pack()
    global daychoosen, combdate
    daychoosen = ttk.Combobox(combo_frame,justify="center", width = 24)

    f=open('data.json','r')
    data=json.load(f)
    f.close()
    combdate=[]
    for i in data['golds']:
        combdate.append(i['updated'][0:i['updated'].find(' ')])

    daychoosen['value']=combdate
    daychoosen.current(0)
    daychoosen.grid(column=1,row=1)
    Label(combo_frame,text=" ").grid(column=2,row=1)
    Button(combo_frame, text="Chọn",width=12,font=("Arial",10,"bold"),command=getCombobox,bg="#000",fg="#fff").grid(column=3,row=1)

    global display_frame
    display_frame=Frame(pop2)
    display_frame.configure(bg="#fff")
    display_frame.pack(fill=BOTH,expand=1)
    with open('data.json', 'r', encoding='utf-8') as f:
        data=json.load(f)
        f.close()
    x= data['golds']
    x1=x[0]
    value=x1['value']
    n=1

__init__(my_window)
# SEVER FUNCTIONS
HOST='127.0.0.1'
PORT=33000
BUFSIZE=1024
FORMAT="utf8"
# tạo socket server IPv4 type: Stream (TCP)
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
    length=len(bytes(msg.encode(FORMAT)))
    client.send(bytes(str(length).encode(FORMAT)))
    client.recv(BUFSIZE)
    client.sendall(bytes(msg.encode(FORMAT)))
def checkLogin(client):
    acc=""
    account=recvList(client)
    f=open('infoclient.json','r')
    data=json.load(f)
    f.close()
    msg='declined'
    for i in range (0, len(data['account'])):
        if data['account'][i]["username"]==account[0] and data['account'][i]["password"]==account[1]:
            msg='accepted'
            break
    client.send(bytes(msg.encode(FORMAT)))
    if msg=='accepted':
        acc=account[0]
        f=open('onlinelist.json','r')
        data=json.load(f)
        f.close()
        x={
            'username': account[0],
            'password': account[1]
        }
        data['account'].append(x)
        f=open('onlinelist.json','w')
        f.write(json.dumps(data))
        f.close()
    return acc
def checkSignin(client):
    account=recvList(client)
    f=open('infoclient.json','r')
    data=json.load(f)
    f.close()
    msg='signin succeed'
    for i in range (0, len(data['account'])):
        if data['account'][i]["username"]==account[0]:
            msg='signin failed'
            break
    client.send(bytes(msg.encode(FORMAT)))
    if msg=='signin succeed':
        x={
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
    brand,company,date=recvList(client)
    print(brand)
    print(company)
    print(date)
    # mở file lấy data
    with open('data.json', 'r', encoding='utf-8') as f:
        file=json.load(f)
        f.close()
    for i in file['golds']:
        if date in i['updated']:
            data=i['value']
            break
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
        except OSError:
            break
def logOut(acc):
    if acc=="":
        return
    f=open('onlinelist.json','r')
    data=json.load(f)
    f.close()
    for i in range (0, len(data['account'])):
        if data['account'][i]["username"] == acc:
            del data['account'][i]
            break
    f=open('onlinelist.json','w')
    f.write(json.dumps(data))
    f.close()
def deleteOnlineList():
    f=open('onlinelist.json','r')
    data=json.load(f)
    f.close()
    data['account']=[]
    f=open('onlinelist.json','w')
    f.write(json.dumps(data))
    f.close()
def sendGuiList(client):
    f=open('data.json','r')
    data=json.load(f)
    f.close()
    result={"brand" : [],"company":[],"date":[]}
    for i in data['golds']:
        date=i['updated'][0:i['updated'].find(' ')]
        result['date'].append(date)
        for j in i['value']:
            if j['company']!='' and not j['company'] in result['company']:
                result['company'].append(j['company'])
        for j in i['value']:
            if j['brand']!='' and not j['brand'] in result['brand']:
                result['brand'].append(j['brand'])
    sendResult(client,result)
def handleClient(client):
    acc=""
    while True:
        try:
            option=client.recv(BUFSIZE).decode(FORMAT)
            print(option)
            if option=="LOGIN":
                acc=checkLogin(client)
                print(acc)
            elif option=='SIGNIN':
                checkSignin(client)
            elif option=='GETGUILIST':
                sendGuiList(client)
            elif option=='SEARCH':
                search(client)
            elif option=='LOGOUT':
                logOut(acc)
            elif option=='exit':
                client.close()
                logOut(client,acc)
                break
        except:
            client.close()
            logOut(acc)
            print('except')
            break
SEVER.listen(5)
Thread(target=acceptConnection,daemon=True).start()
Thread(target=start_api,daemon=True).start()
my_window.mainloop()
deleteOnlineList()
SEVER.close()