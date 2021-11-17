from socket import AF_INET, socket, SOCK_STREAM
from tkinter import *
from tkinter import ttk
import tkinter
from PIL import Image, ImageTk
from tkinter import scrolledtext
import json
import tkinter.messagebox as mbox
import re

HOST='127.0.0.1'
PORT=33000
BUFSIZE=1024
FORMAT="utf8"
CLIENT=socket(AF_INET,SOCK_STREAM)
#connect to sever
CLIENT.connect((HOST,PORT))

#
my_window =Tk()
my_window.title('Client Version')
my_window.geometry("400x350")

frame=Frame()
frame.pack(side='top',fill='both',expand=True)
frame.grid_rowconfigure(0,weight=1)
frame.grid_columnconfigure(0,weight=1)
#
def outputResult(result):
    print(123445)
    global main_frame
    main_frame=Frame(second_big_frame)
    main_frame.pack(fill=BOTH,expand=1)

    global my_canvas
    my_canvas=Canvas(main_frame)
    my_canvas.pack(side=LEFT, fill=BOTH,expand=1)
    global my_scrollbar
    my_scrollbar=ttk.Scrollbar(main_frame, orient=VERTICAL,command=my_canvas.yview)
    my_scrollbar.pack(side=RIGHT, fill=Y)
    my_canvas.configure(yscrollcommand=my_scrollbar.set, width=700, height=100)
    my_canvas.bind('<Configure>', lambda e:my_canvas.configure(scrollregion=my_canvas.bbox("all")))
    global second_frame
    second_frame=Frame(my_canvas)
    my_canvas.create_window((0,0), window=second_frame, anchor="nw")

    global outFrame
    outFrame=Frame(second_frame)
    Label(outFrame,text="           ").grid(column=0,row=1)
    n=1
    Label(outFrame,text="Brand", width=15).grid(column=1,row=n)
    Label(outFrame,text="Company", width=10).grid(column=2,row=n)
    Label(outFrame,text="Brand1", width=10).grid(column=3,row=n)
    Label(outFrame,text="Type", width=30).grid(column=4,row=n)
    Label(outFrame,text="Buy").grid(column=5,row=n)
    Label(outFrame,text="Sell").grid(column=6,row=n)
    outFrame.pack(fill=BOTH)
    for i in range (0,len(result)):
        n=n+1
        Label(outFrame, text='   '+result[i]['brand']+'   ').grid(column=1,row=n)
        Label(outFrame, text='   '+result[i]['company']+'   ').grid(column=2,row=n)
        Label(outFrame, text='   '+result[i]['brand1']+'   ').grid(column=3,row=n)
        Label(outFrame, text='   '+result[i]['type']+'   ').grid(column=4,row=n)
        Label(outFrame, text='   '+result[i]['buy']+'   ').grid(column=5,row=n)
        Label(outFrame, text='   '+result[i]['sell']+'   ').grid(column=6,row=n)


def findInfo(INPUT1, INPUT2, value):
    result=[]

    a=INPUT1.strip("\n")
    b=INPUT2.strip("\n")
    print(len(value))
    for i in range(0, len(value)):
        if a!='' and b!='':
            if value[i]["brand"].lower() == a.lower() and value[i]['company'].lower() == b.lower():
                result.append(value[i])
                break
        if a!='' and b=='':
            if value[i]["brand"].lower() == a.lower():
                result.append(value[i])
        if a=='' and b!='':
            if value[i]['company'].lower() == b.lower():
                result.append(value[i])
    print(result)
    print(len(result))
    if len(result)==0:
        print('Nothing has this brand')
        noti_box=Toplevel()
        noti_box.geometry("400x70")
        noti=Label(noti_box, text="*Error: Nothing has this Brand=\" " + a+ '\" Company=\"'+b+" \"", fg="red", font=("Arial",10, "bold")).pack(expand=True)
    else:
        title=Label(second_big_frame, text="Kết quả trả về cho Brand=\"" + a+ '\" Company=\"'+b+" \"", font=("Arial",10,"bold"), fg="#006699").pack()
        outputResult(result)

def startPage():
    star_page=Frame(frame)
    Label(star_page, text="Hi Client !!!",font=("Times New Roman",30) ).pack(pady=30)
    signin=Button(star_page,text="Đăng kí", width=20,command=sigIn).pack(padx=20, pady=10)
    # login=Button(frame,text="Đăng nhập",width=20, command=MainSearch).pack(padx=20, pady=10)
    login=Button(star_page,text="Đăng nhập",width=20, command=logIn).pack(padx=20, pady=10)

    star_page.grid(row=0,column=0,sticky='nsew')
    star_page.tkraise()

def __init__():
    startPage()
def clearFrame():
    # destroy all widgets from frame
    for widget in outFrame.winfo_children():
       widget.destroy()
    for widget in second_frame.winfo_children():
       widget.destroy()
    for widget in my_canvas.winfo_children():
       widget.destroy()
    for widget in main_frame.winfo_children():
       widget.destroy()
    # for widget in total_frame.winfo_children():
    #    widget.destroy()

    for widget in second_big_frame.winfo_children():
       widget.destroy()
    # for widget in my_big_canvas.winfo_children():
    #    widget.destroy()
    # for widget in main_big_frame.winfo_children():
    #    widget.destroy()
    # this will clear frame and frame will be empty
    # if you want to hide the empty panel then

    # outFrame.pack_forget()
    # my_canvas.pack_forget()
    # main_frame.pack_forget()
    my_big_scrollbar.pack_forget()
    # total_frame.pack_forget()

    # my_big_canvas.pack_forget()
    # main_big_frame.pack_forget()
    # my_big_scrollbar.destroy()

    # search_page.pack_forget()




def transfer():
    INPUT1=brand_box.get("1.0",END)
    INPUT2=company_box.get("1.0",END)
    print(INPUT1)
    with open('myfile.json', 'r', encoding='utf-8') as f:
        data=json.load(f)
        f.close()
    x= data['golds']
    x1=x[0]
    value=x1['value']
    findInfo(INPUT1, INPUT2, value)


def MainSearch():
    search_page=Frame(frame)
    my_window.geometry("750x700")
    my_window.title('Tim kiem Vang')
    Label(search_page, text="Bạn đang đăng nhập bằng tài khoản "+ user_log, font=("ROBOTO", 13), fg="red").pack()
    global brand_box
    global company_box
    lbl1=Label(search_page, text="Brand vàng mà bạn muốn tìm: ").pack()
    brand_box=Text(search_page,width=20,height=1)
    brand_box.pack()
    lbl2=Label(search_page, text="Company vàng mà bạn muốn tìm: ").pack()
    company_box=Text(search_page,width=20,height=1)
    company_box.pack()

    btn_frame=Frame(search_page)
    btn_frame.pack(pady=10, padx=5)
    submit_button=Button(btn_frame, text="SUBMIT", command=transfer,bg="#333", fg="#fff").grid(column=1, row=1)
    clear_button=Button(btn_frame, text="Clear all Resuls", command=clearFrame,bg="#333",fg="#fff").grid(column=2, row=1)

    search_page.grid(row=0,column=0,sticky='nsew')
    search_page.tkraise()

    global total_frame
    total_frame=Frame(search_page)
    total_frame.pack(fill=BOTH,expand=1)
    # total_frame.configure(font=("Arial",30))
    Label(total_frame, text="đây là total")

    global main_big_frame
    main_big_frame=Frame(total_frame)
    main_big_frame.pack(fill=BOTH,expand=1)

    Label(main_big_frame, text="đây là total")


    global my_big_canvas
    my_big_canvas=Canvas(main_big_frame)
    my_big_canvas.pack(side=LEFT, fill=BOTH,expand=1)
    global my_big_scrollbar
    my_big_scrollbar=ttk.Scrollbar(main_big_frame, orient=VERTICAL,command=my_big_canvas.yview)
    my_big_scrollbar.pack(side=RIGHT, fill=Y)
    my_big_canvas.configure(yscrollcommand=my_big_scrollbar.set)
    my_big_canvas.bind('<Configure>', lambda e:my_big_canvas.configure(scrollregion=my_big_canvas.bbox("all")))
    Label(my_big_canvas, text="big canvas", font=("Arial",20))
    global second_big_frame
    second_big_frame=Frame(my_big_canvas)
    my_big_canvas.create_window((0,0), window=second_big_frame, anchor="nw")


def sigIn():
    sign_in=Frame(frame)
    my_window.title('Sign-In')
    my_window.geometry('400x300')
    Label(sign_in, text="Đăng kí tài khoản", font=("Arial",15)).pack(pady=20)
    
    input_signin=Frame(sign_in)
    input_signin.pack()
    global username_box, password_box
    username=Label(input_signin, text="User Name:").grid(column=1, row=1)
    username_box=Text(input_signin,width=20,height=1)
    username_box.grid(column=2, row=1)
    Label(input_signin, text="   ", height=1,font=("Arial",2)).grid(column=1, row=2)
    password=Label(input_signin, text="Password: ").grid(column=1, row=3)
    password_box=Text(input_signin,width=20,height=1)
    password_box.grid(column=2, row=3)
    Button(sign_in,text="Sign-in Account",bg="#000", fg="#fff",command=saveNewAcc).pack(pady=20)
    Button(sign_in,text="Back to StarPage",bg="#000", fg="#fff",command=startPage).pack(pady=20)


    sign_in.grid(row=0,column=0,sticky='nsew')
    sign_in.tkraise()


def isSameAccount(accounts):
    for i in range (0,len(accounts)):
        if(accounts[i]["username"]==user_sign):
            return True
    return False

def onErrorSignIn():
    mbox.showerror("Error", "Tên tài khoản đã được sử dụng, vui lòng thử")

def onErrorLogIn():
    mbox.showerror("Error", "Sai thông tin đăng nhập, vui lòng thử lại")

def successfullSignIn():
    mbox.showerror("Infomation", "Tạo tài khoản thành công, vui lòng thoát ra và đăng nhập lại")

def saveNewAcc():
    global user_sign
    global password_sign
    user_sign=username_box.get("1.0", END).strip('\n')
    print("tên dang kí" + user_sign)
    password_sign=password_box.get("1.0", END).strip('\n')
    print("pass dang kí" +password_sign)
    with open('D:/Destop/testing_python/server/infoclient.json', 'r', encoding='utf8') as f:
        data=json.load(f)
        print(data)
    f.close()
    accounts=data['account']
    if(isSameAccount(accounts)==True):
        onErrorSignIn()
    else:
        print(123)
        x={
            'id':len(accounts)+1,
            'username': user_sign,
            'password': password_sign
        }
        accounts.append(x)
        print(accounts)
        data["account"]=accounts
        global convertJson
        convertJson=json.dumps(data)
        print(convertJson)
        with open('D:/Destop/testing_python/server/infoclient.json', 'w+') as f:
            f.write(convertJson)
            f.close()
        successfullSignIn()


def logIn():
    log_in=Frame(frame)
    my_window.title('Log-In')
    my_window.geometry('400x300')
    Label(log_in, text="Đăng nhập tài khoản", font=("Arial",15)).pack(pady=20)
    input_login=Frame(log_in)
    input_login.pack()
    global username_box_log, password_box_log
    username=Label(input_login, text="User Name:").grid(column=1, row=1)
    username_box_log=Entry(input_login)
    username_box_log.grid(column=2, row=1)
    Label(input_login, text="   ", height=1,font=("Arial",2)).grid(column=1, row=2)
    password=Label(input_login, text="Password: ").grid(column=1, row=3)
    password_box_log=Entry(input_login)
    password_box_log.grid(column=2, row=3)
    Button(log_in,text="Log-in Account",bg="#000", fg="#fff",command=confirmAcc).pack(pady=20)
    Button(log_in,text="Go back to StartPage",bg="#000", fg="#fff",command=startPage).pack(pady=20)

    log_in.grid(row=0,column=0,sticky='nsew')
    log_in.tkraise()

def sendList( list):

    for item in list:
        CLIENT.sendall(item.encode(FORMAT))
        #wait response
        CLIENT.recv(1024)

    msg = "end"
    CLIENT.send(msg.encode(FORMAT))
def confirmAcc():
    # gui option login
    option='LOGIN'
    CLIENT.send(option.encode(FORMAT))
    global user_log
    global password_log
    user_log=username_box_log.get()
    password_log=password_box_log.get()
    # Sever check account
    account=[user_log,password_log]
    sendList(account)
    check=CLIENT.recv(BUFSIZE).decode(FORMAT)
    print(check)
    if check=='accepted':
        MainSearch()
        return
    
    onErrorLogIn()


# MainSearch()
__init__()

# saveNewAcc()
my_window.mainloop()

CLIENT.close()