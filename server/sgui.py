from tkinter import *
from tkinter import ttk
import tkinter
from PIL import Image, ImageTk
from tkinter import scrolledtext
import json

my_window =Tk()
my_window.title('Server Version')
my_window.geometry("400x350")

def __init__(my_window):

    load=Image.open('background4.jpeg')
    render=ImageTk.PhotoImage(load)
    img=Label(my_window, image=render)
    img.place(x=0, y=0)

    welcomeBoss = Label(my_window, text="Hello server", bg="#ADD9E6")
    welcomeBoss.config(font=("Humblle Rought All Caps",30))
    welcomeBoss.pack(pady=20)

    clientsList=Button(my_window, text='Clients\' Information', width=30, height=2, background='#FFA07A', fg="#333", command=pageOne)
    clientsList.pack(pady=5)
    clientsList.config(font=(".VnSouthern",10, "bold"))

    onlineClient=Button(my_window, text='Accounts online now',width=30, height=2, background='#FFA07A', fg="#333", command=pageTwo)
    # onlineClient.grid(column=0, row=2)
    onlineClient.pack(pady=5)
    onlineClient.config(font=(".VnSouthern",10, "bold"))


    dataInserver=Button(my_window, text='Data about gold',width=30, height=2,background='#FFA07A', fg="#333",command=pageThree)
    # dataInserver.grid(column=0, row=3)
    dataInserver.pack(padx=20, pady=3)
    dataInserver.config(font=(".VnSouthern",10, "bold"))

    my_window.mainloop()

def printAccount1(accounts):
    n=1
    frame_account=Frame(pop)
    frame_account.pack(padx=20, pady=10)
    for i in range(0, len(accounts)):
        x=accounts[i]
        print(x['username'] + '   '+ x['password'])
        num=Label(frame_account, text=n,bg='#fff', width=5)
        num.grid(column=0, row=n)
        n1=Label(frame_account, text=x['username'],bg='#fff', width=15)
        n1.grid(column=1, row=n)
        # n1.pack()
        n2=Label(frame_account, text=x['password'],bg='#fff',width=15)
        n2.grid(column=2, row=n)
        n=n+1

def printAccount2(accounts):
    n=1
    frame_account=Frame(pop1)
    frame_account.pack(padx=20, pady=10)
    print(456)

    for i in range(0, len(accounts)):
        x=accounts[i]
        print(x['username'] + '   '+ x['password'])
        num=Label(frame_account, text=n,bg='#fff', width=5)
        num.grid(column=0, row=n)
        n1=Label(frame_account, text=x['username'],bg='#fff', width=15)
        n1.grid(column=1, row=n)
        # n1.pack()
        n2=Label(frame_account, text=x['password'],bg='#fff',width=15)
        n2.grid(column=2, row=n)
        n=n+1

def pageOne():
    global pop
    pop=Toplevel()
    # scroll = Scrollbar(pop)
    # scroll.pack( side = RIGHT, fill = Y )
    pop.geometry("400x500")
    pop.title('Danh sach tai khoan')
    lbl=Label(pop, text='TOTAL ACCOUNTS')
    lbl.pack(padx=50, pady=10)
    # lbl.config(font=("Humblle Rought All Caps",30))
    with open('D:/Destop/testing_python/server/infoclient.json', 'r') as f:
        data=json.load(f)
        f.close()
    accounts=data['account']
    lbl=Label(pop,text='Hien co ' + str(len(accounts)) + ' tai khoan da dang ki').pack()
    printAccount1(accounts)

def pageTwo():
    global pop1
    pop1=Toplevel()
    # scroll = Scrollbar(pop)
    # scroll.pack( side = RIGHT, fill = Y )
    pop1.geometry("400x500")
    pop1.title('Danh sach tai khoan')
    # lbl.config(font=("Humblle Rought All Caps",30))
    with open('D:/Destop/testing_python/server/onlinelist.json', 'r') as f:
        data=json.load(f)
        f.close()
        print(data)
    accounts=data['account']
    lbl=Label(pop1, text='TOTAL ACCOUNTS ONLINE NOW')
    lbl.pack(padx=50, pady=10)
    printAccount2(accounts)

def pageThree():
    global pop2
    pop2=Toplevel()
    pop2.geometry("500x500")
    pop2.title('Toan bo du lieu')
    with open('myfile.json', 'r', encoding='utf-8') as f:
        data=json.load(f)
        f.close()
    # print(data)
    x= data['golds']
    x1=x[0]
    value=x1['value']
    # print(value)
    n=1
    main_frame=Frame(pop2)
    main_frame.pack(fill=BOTH,expand=1)
    my_canvas=Canvas(main_frame)
    my_canvas.pack(side=LEFT, fill=BOTH,expand=1)
    my_scrollbar=ttk.Scrollbar(main_frame, orient=VERTICAL,command=my_canvas.yview)
    print(123)
    my_scrollbar.pack(side=RIGHT, fill=Y)
    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind('<Configure>', lambda e:my_canvas.configure(scrollregion=my_canvas.bbox("all")))
    second_frame=Frame(my_canvas)
    my_canvas.create_window((0,0), window=second_frame, anchor="nw")
    Label(second_frame, text="Company").grid(column=1,row=0)
    Label(second_frame, text="Brand").grid(column=2,row=0)
    Label(second_frame, text="Buy").grid(column=3,row=0)
    Label(second_frame, text="Sell").grid(column=5,row=0)

    for i in range(0, len(value)):
        print(value[i])
        Label(second_frame,text=n).grid(column=0,row=n)
        Label(second_frame, text=value[i]['company']).grid(column=1,row=n)
        Label(second_frame, text=value[i]['brand']).grid(column=2,row=n)
        Label(second_frame, text=value[i]['buy']).grid(column=3,row=n)
        Label(second_frame, text="      ").grid(column=4,row=n)
        Label(second_frame, text=value[i]['sell']).grid(column=5,row=n)


        # x.pack(side=LEFT)
        n=n+1

__init__(my_window)

# pageOne()