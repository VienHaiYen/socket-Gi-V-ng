from tkinter import *
from tkinter import ttk
import tkinter
from PIL import Image, ImageTk
from tkinter import scrolledtext
import json

my_window =Tk()
my_window.title('Server Version')
my_window.geometry("550x350")



def __init__(my_window):

    load=Image.open('marketing.jpg')
    render=ImageTk.PhotoImage(load)
    img=Label(my_window, image=render)
    img.place(x=0, y=-50)

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
    # onlineClient.grid(column=0, row=2)
    onlineClient.pack(pady=5)
    onlineClient.config(font=(".VnSouthern",10, "bold"))


    dataInserver=Button(btn_start_frame, text='Data about gold',width=25, height=1,background='#7FBDEA', fg="#fff",command=pageThree)
    # dataInserver.grid(column=0, row=3)
    dataInserver.pack(padx=20, pady=3)
    dataInserver.config(font=(".VnSouthern",10, "bold"))

    my_window.mainloop()

def printAccount1(accounts):
    main_frame=Frame(pop)
    main_frame.pack(fill=BOTH,expand=1)
    my_canvas=Canvas(main_frame)
    my_canvas.pack(side=LEFT, fill=BOTH,expand=1)
    my_scrollbar=ttk.Scrollbar(main_frame, orient=VERTICAL,command=my_canvas.yview)
    my_scrollbar.pack(side=RIGHT, fill=Y)
    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind('<Configure>', lambda e:my_canvas.configure(scrollregion=my_canvas.bbox("all")))
    second_frame=Frame(my_canvas)
    my_canvas.create_window((0,0), window=second_frame, anchor="nw")
    second_frame.configure(border=True ,highlightbackground="black",highlightthickness=1,width=300)
    second_frame.place(x=60,y=15)

    n=1
    for i in range(0, len(accounts)):
        x=accounts[i]
        print(x['username'] + '   '+ x['password'])
        num=Label(second_frame, text=n, width=5)
        num.grid(column=1, row=n)
        n1=Label(second_frame, text=x['username'], width=15)
        n1.grid(column=2, row=n)
        # n1.pack()
        n2=Label(second_frame, text=x['password'],width=15)
        n2.grid(column=3, row=n)
        n=n+1

def printAccount2(accounts):
    n=1
    main_frame=Frame(pop1)
    main_frame.pack(fill=BOTH,expand=1)
    my_canvas=Canvas(main_frame)
    my_canvas.pack(side=LEFT, fill=BOTH,expand=1)
    my_scrollbar=ttk.Scrollbar(main_frame, orient=VERTICAL,command=my_canvas.yview)
    my_scrollbar.pack(side=RIGHT, fill=Y)
    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind('<Configure>', lambda e:my_canvas.configure(scrollregion=my_canvas.bbox("all")))
    second_frame=Frame(my_canvas)
    my_canvas.create_window((0,0), window=second_frame, anchor="nw")
    second_frame.configure(border=True ,highlightbackground="black",highlightthickness=1,width=300)
    second_frame.place(x=60,y=15)
    for i in range(0, len(accounts)):
        x=accounts[i]
        print(x['username'] + '   '+ x['password'])
        num=Label(second_frame, text=n, width=5)
        num.grid(column=0, row=n)
        n1=Label(second_frame, text=x['username'], width=15)
        n1.grid(column=1, row=n)
        # n1.pack()
        n2=Label(second_frame, text=x['password'],width=15)
        n2.grid(column=2, row=n)
        n=n+1

def pageOne():
    global pop
    pop=Toplevel()
    pop.geometry("400x500")

    pop.title('Danh sach tai khoan')
    lbl=Label(pop, text='TOTAL ACCOUNTS',font=("iCiel Pacifico",15))
    lbl.pack(padx=50, pady=5)
    # lbl.config(font=("Humblle Rought All Caps",30))
    with open('infoclient.json', 'r') as f:
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
    with open('onlinelist.json', 'r') as f:
        data=json.load(f)
        f.close()
        print(data)
    accounts=data['account']
    lbl=Label(pop1, text='Online  NOW',font=("iCiel Pacifico",15))
    lbl.pack(padx=50, pady=5)
    printAccount2(accounts)

def pageThree():
    global pop2
    pop2=Toplevel()
    pop2.geometry("700x500")
    pop2.title('Toan bo du lieu')
    pop2.configure(bg="#fff")
    Label(pop2, text="BẢNG GIÁ VÀNG",font=("iCiel Pacifico",15),bg="#fff").pack()
    with open('myfile.json', 'r', encoding='utf-8') as f:
        data=json.load(f)
        f.close()
    x= data['golds']
    x1=x[0]
    value=x1['value']
    n=1
    main_frame=Frame(pop2)
    main_frame.pack(fill=BOTH,expand=1)
    my_canvas=Canvas(main_frame)
    my_canvas.pack(side=LEFT, fill=BOTH,expand=1)
    my_canvas.configure(bg="#fff")
    my_scrollbar=ttk.Scrollbar(main_frame, orient=VERTICAL,command=my_canvas.yview)
    my_scrollbar.pack(side=RIGHT, fill=Y)
    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind('<Configure>', lambda e:my_canvas.configure(scrollregion=my_canvas.bbox("all")))
    second_frame=Frame(my_canvas)
    second_frame.configure(bg="#fff")
    my_canvas.create_window((0,0), window=second_frame, anchor="nw")
    Label(second_frame, text="Company",bg="#fff").grid(column=1,row=0)
    Label(second_frame, text="Brand",bg="#fff").grid(column=2,row=0)

    Label(second_frame, text="Brand1",bg="#fff").grid(column=3,row=0)
    Label(second_frame, text="Type",bg="#fff").grid(column=4,row=0)

    Label(second_frame, text="Buy",bg="#fff").grid(column=5,row=0)
    Label(second_frame, text="Sell",bg="#fff").grid(column=7,row=0)

    for i in range(0, len(value)):
        print(value[i])
        Label(second_frame,text=n,bg="#fff").grid(column=0,row=n)
        Label(second_frame, text=value[i]['company'],bg="#fff").grid(column=1,row=n)
        Label(second_frame, text=value[i]['brand'],bg="#fff").grid(column=2,row=n)

        Label(second_frame, text=value[i]['brand1'],bg="#fff").grid(column=3,row=n)
        Label(second_frame, text=value[i]['type'],bg="#fff").grid(column=4,row=n)

        Label(second_frame, text=value[i]['buy'],bg="#fff").grid(column=5,row=n)
        Label(second_frame, text="      ",bg="#fff").grid(column=6,row=n)
        Label(second_frame, text=value[i]['sell'],bg="#fff").grid(column=7,row=n)

        n=n+1

__init__(my_window)

# pageOne()