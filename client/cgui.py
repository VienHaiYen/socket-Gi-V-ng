
from socket import AF_INET,socket,SOCK_STREAM
from io import BufferedReader

from tkinter import *
from tkinter import ttk



from tkinter import scrolledtext
import json
import tkinter.messagebox as mbox

from PIL import Image, ImageTk


#
my_window =Tk()
my_window.title('Client Version')
my_window.geometry("600x300")



frame=Frame()
frame.pack(side='top',fill='both',expand=True)
frame.grid_rowconfigure(0,weight=1)
frame.grid_columnconfigure(0,weight=1)
#
def outputResult(result):
    global main_frame
    main_frame=Frame(second_big_frame)
    main_frame.pack(fill=BOTH,expand=1)

    global my_canvas
    my_canvas=Canvas(main_frame)
    my_canvas.pack(side=LEFT, fill=BOTH,expand=1)
    global my_scrollbar
    my_scrollbar=ttk.Scrollbar(main_frame, orient=VERTICAL,command=my_canvas.yview)
    my_scrollbar.pack(side=RIGHT, fill=Y)
    my_canvas.configure(yscrollcommand=my_scrollbar.set, width=730, height=200)
    my_canvas.bind('<Configure>', lambda e:my_canvas.configure(scrollregion=my_canvas.bbox("all")))
    global second_frame
    second_frame=Frame(my_canvas)
    my_canvas.create_window((0,0), window=second_frame, anchor="nw")

    global outFrame
    outFrame=Frame(second_frame)
    # Label(outFrame,text="      ").grid(column=0,row=1)
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
        Label(outFrame, text=' '+result[i]['buy']+' ').grid(column=5,row=n)
        Label(outFrame, text=' '+result[i]['sell']+' ').grid(column=6,row=n)
def recvResult(conn):
    length=conn.recv(BUFSIZE).decode(FORMAT)
    conn.send(bytes(length.encode(FORMAT)))
    length=int(length)
    response=""
    while len(response)<length:
        response=response+conn.recv(BUFSIZE).decode(FORMAT)
    list=json.loads(response)
    return list

def startPage():
    star_page=Frame(frame)
    star_page.configure(bg="#fff")
    my_window.title('Start-page')
    my_window.geometry('600x300')

    tempIMG=(Image.open("tech2.jpg"))
    startImg=tempIMG.resize((800,400),Image.ANTIALIAS)
    new_image= ImageTk.PhotoImage(startImg)
    # photo = PhotoImage(file="login.png")
    label = Label(star_page, image=new_image)
    label.image = new_image
    label.place(x=-105, y=-80)

    Label(star_page, text="",font=("iCiel Rukola",5), bg="#fff" ).pack(pady=1)
    Label(star_page, text="Hi Client !!!",font=("iCiel Rukola",28), bg="#fff" ).pack(pady=0)
    signin=Button(star_page,text="Đăng kí", width=20,command=sigIn,bg="#000", fg="#fff",font=("Arial",10,"bold"))
    signin.pack(padx=20, pady=10)
    login=Button(star_page,text="Đăng nhập",width=20, command=logIn,bg="#000", fg="#fff",font=("Arial",10,"bold"))
    login.pack(padx=20, pady=10)
    star_page.grid(row=0,column=0,sticky='nsew')
    changeOnHoverButton(signin)
    changeOnHoverButton(login)
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
    # my_big_scrollbar.pack_forget()

def sendOption(option):
    try:
        CLIENT.sendall(bytes(option.encode(FORMAT)))
    except:
        onErrorLostConnection()
        startPage()



def transfer():
    sendOption('SEARCH')
    INPUT1=brand_box.get()
    INPUT2=company_box.get()
    if INPUT1=='':
        INPUT1='none'
    if INPUT2=='':
        INPUT2='none'
    searchkey=[INPUT1,INPUT2]
    sendList(searchkey)
    result=recvResult(CLIENT)
    if len(result)==0:
        onErrorSearching()
    else:
        Label(second_big_frame, text="Kết quả trả về cho Brand=\"" + INPUT1+ '\" Company=\"'+INPUT2+"\"", font=("Arial",10,"bold"), fg="#006699").pack()
        outputResult(result)

def MainSearch():
    search_page=Frame(frame)
    search_page.configure(bg="#fff")
    my_window.geometry("780x700")
    my_window.title('Tim kiem Vang')


    tempIMG=(Image.open("square.png"))
    startImg=tempIMG.resize((500,300),Image.ANTIALIAS)
    new_image= ImageTk.PhotoImage(startImg)
    # photo = PhotoImage(file="login.png")
    label = Label(search_page, image=new_image)
    label.image = new_image
    label.place(x=0, y=0)

    label2 = Label(search_page, image=new_image)
    label2.image = new_image
    label2.place(x=500, y=0)

    label3 = Label(search_page, image=new_image)
    label3.image = new_image
    label3.place(x=1000, y=0)

    tempIMG=(Image.open("user.png"))
    startImg=tempIMG.resize((50,50),Image.ANTIALIAS)
    new_image= ImageTk.PhotoImage(startImg)
    label = Label(search_page, image=new_image)
    label.image = new_image
    label.place(x=0, y=0)

    Label(search_page, text="TÌM KIẾM GIÁ VÀNG", font=("iCiel Rukola", 15,"bold"), fg="red").place(x=0, y=50)


    Label(search_page, text="Name: "+ user_log, font=("ROBOTO", 12), fg="#292F34").place(x=60, y=15)
    Label(text="", font=("ROBOTO",10)).pack()
    input_bar=Frame(search_page)
    input_bar.pack()

    global brand_box
    global company_box
    lbl1=Label(input_bar, text="Gold Brand:                                                   ",font=("Arial",10,"bold")).pack()
    brand_box=Entry(input_bar,width=25,justify='center',font=("Arial",12))
    brand_box.pack()
    lbl2=Label(input_bar, text="Gold Company:                                           ",font=("Arial",10,"bold")).pack()
    company_box=Entry(input_bar,width=25,justify='center',font=("Arial",12))
    company_box.pack()

    btn_frame=Frame(input_bar)
    btn_frame.pack(pady=10)
    submitbtn=Button(btn_frame, text="SUBMIT", command=transfer,bg="#333", fg="#fff")
    submitbtn.grid(column=1, row=1)
    changeOnHoverButton(submitbtn)
    Label(btn_frame,text="   ").grid(column=2, row=1)
    clearbtn=Button(btn_frame, text="Clear all Resuls", command=clearFrame,bg="#333",fg="#fff")
    clearbtn.grid(column=3, row=1)
    changeOnHoverButton(clearbtn)


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
    # my_big_canvas.configure(bg="red")

    my_big_canvas.pack(side=RIGHT, fill=BOTH,expand=1)
    global my_big_scrollbar
    my_big_scrollbar=ttk.Scrollbar(main_big_frame, orient=VERTICAL,command=my_big_canvas.yview)
    my_big_scrollbar.pack(side=RIGHT, fill=Y)
    my_big_canvas.configure(yscrollcommand=my_big_scrollbar.set)
    my_big_canvas.bind('<Configure>', lambda e:my_big_canvas.configure(scrollregion=my_big_canvas.bbox("all")))
    Label(my_big_canvas, text="big canvas", font=("Arial",20))
    global second_big_frame
    second_big_frame=Frame(my_big_canvas)
    my_big_canvas.create_window((0,0), window=second_big_frame, anchor="nw")

def changeOnHoverText(button):
    button.bind("<Enter>", func=lambda e: button.config(fg="#39729b"))
    button.bind("<Leave>", func=lambda e: button.config(fg="#000"))

def changeOnHoverButton(button):
    button.bind("<Enter>", func=lambda e: button.config(bg="#37393b"))
    button.bind("<Leave>", func=lambda e: button.config(bg="#000"))

def sigIn():
    sign_in=Frame(frame)
    my_window.title('Sign-In')
    my_window.geometry('600x300')

    tempIMG=(Image.open("tech3.jpg"))
    startImg=tempIMG.resize((800,400),Image.ANTIALIAS)
    new_image= ImageTk.PhotoImage(startImg)
    label = Label(sign_in, image=new_image)
    label.image = new_image
    label.place(x=-105, y=-80)

    Label(sign_in, text="Đăng kí tài khoản", font=("iCiel Pacifico",20),bg="#fff").place(x=270,y=30)

    input_signin=Frame(sign_in)
    input_signin.place(x=280,y=100)
    global username_box, password_box
    username=Label(input_signin, text="User Name:", font=("Arial",10),bg="#fff").grid(column=1, row=1)
    username_box=Entry(input_signin)
    username_box.grid(column=2, row=1)
    Label(input_signin, text="   ", height=1,font=("Arial",2)).grid(column=1, row=2)
    password=Label(input_signin, text="Password: ", font=("Arial",10),bg="#fff").grid(column=1, row=3)
    password_box=Entry(input_signin)
    password_box.grid(column=2, row=3)
    confirm=Button(sign_in,text="Sign-in Account",bg="#000", fg="#fff",command=saveNewAcc,width=20)
    confirm.place(x=310,y=170)
    out_line=Button(sign_in,text="Back to StarPage",bg="#fff", fg="#000",border=False,command=startPage,width=20)
    out_line.place(x=310,y=220)
    changeOnHoverText(out_line)
    changeOnHoverButton(confirm)

    sign_in.grid(row=0,column=0,sticky='nsew')
    sign_in.tkraise()


def onErrorSignIn():
    mbox.showerror("Error", "Tên tài khoản đã được sử dụng, vui lòng thử lại")

def onErrorSearching():
    mbox.showerror("Error", "Không tìm thấy kết quả, vui lòng thử lại")

def onErrorLogIn():
    mbox.showerror("Error", "Sai thông tin đăng nhập, vui lòng thử lại")

def successfullSignIn():
    mbox.showinfo("Infomation", "Tạo tài khoản thành công, vui lòng đăng nhập")

def onErrorLetterSpacing():
    mbox.showerror("Error", "Username và password không tồn tại dấu cách")
def onErrorNumberLetter():
    mbox.showerror("Error", "Username phải bao gồm nhiều hơn 5 kí tự")

def validSyntax(username, password):
    if username.find(' ')!=-1 or password.find(' ')!=-1:
        onErrorLetterSpacing()
        return False
    if len(username)<5:
        onErrorNumberLetter()
        return False
    return True

def saveNewAcc():
    user_sign=username_box.get()
    print("tên dang kí " + user_sign)
    password_sign=password_box.get()
    print("pass dang kí " +password_sign)
    if validSyntax(user_sign,password_sign):
        sendOption('SIGNIN')
        account=[user_sign,password_sign]
        sendList(account)

        response=CLIENT.recv(BUFSIZE).decode(FORMAT)
        if response=='signin failed':
            onErrorSignIn()
        else:
            successfullSignIn()
            logIn()


def logIn():
    log_in=Frame(frame)
    my_window.title('Log-In')
    my_window.geometry('600x300')

    tempIMG=(Image.open("tech5.jpg"))
    startImg=tempIMG.resize((800,400),Image.ANTIALIAS)
    new_image= ImageTk.PhotoImage(startImg)
    # photo = PhotoImage(file="login.png")
    label = Label(log_in, image=new_image)
    label.image = new_image
    label.place(x=-50, y=-80)

    Label(log_in, text="Đăng nhập tài khoản", font=("iCiel Pacifico",20),bg="#fff").place(x=50, y=10)
    input_login=Frame(log_in)
    input_login.place(x=55, y=85)
    global username_box_log, password_box_log
    Label(input_login, text="User Name:",font=("Arial",10),bg="#fff").grid(column=1, row=1)
    username_box_log=Entry(input_login)
    username_box_log.grid(column=2, row=1)
    Label(input_login, text="   ", height=1,font=("Arial",2)).grid(column=1, row=2)
    Label(input_login, text="Password: ",font=("Arial",10),bg="#fff").grid(column=1, row=3)
    password_box_log=Entry(input_login)
    password_box_log.grid(column=2, row=3)
    confirm=Button(log_in,text="Log-in Account",bg="#000", fg="#fff",command=confirmAcc,width=20)
    confirm.place(x=62,y=170)
    out_line=Button(log_in,text="Go back to StartPage",bg="#fff", fg="#000",border=False,command=startPage,width=20)
    out_line.place(x=62,y=220)
    changeOnHoverText(out_line)
    changeOnHoverButton(confirm)

    log_in.grid(row=0,column=0,sticky='nsew')
    log_in.tkraise()
def recvDict(client):
    msg=client.recv(BUFSIZE).encode(FORMAT)

    print(dict)

    return dict

def sendList(list):
    for item in list:
        CLIENT.sendall(item.encode(FORMAT))
        #wait response
        CLIENT.recv(1024)
    msg = "end"
    CLIENT.send(msg.encode(FORMAT))
def confirmAcc():
    # gui option login
    sendOption('LOGIN')
    global user_log
    global password_log
    user_log=username_box_log.get()
    password_log=password_box_log.get()
    # Sever check account
    account=[user_log,password_log]
    sendList(account)
    response=CLIENT.recv(BUFSIZE).decode(FORMAT)
    print(response)
    if response=='accepted':
        MainSearch()
        return

    onErrorLogIn()

def onErrorLostConnection():
    mbox.showerror("Error", "Sever đã đóng!")



def quit():
    while True:
        try:
            pass
        except OSError:
            msg='exit'
            print(msg)
            CLIENT.send(bytes(msg.encode(FORMAT)))
#Thread(target=quit,daemon=True).start()


error_server=Frame(frame)
errorImg=PhotoImage(file="4042.jpg")
errorBg=Label(error_server,image=errorImg)
errorBg.pack()

def error404():
    print(12345)
    my_window.title('Not responsding')
    my_window.geometry('600x600')
    #
    Label(error_server, text="Không thể kết nối được tới server, vui lòng thử lại", font=("Arial",15)).pack(pady=20)

    error_server.grid(row=0,column=0,sticky='nsew')
    error_server.tkraise()


def on_closing(event=None):
    msg='exit'
    try:
        CLIENT.send(bytes(msg.encode(FORMAT)))
        CLIENT.close()
    except ConnectionResetError:
        pass
    finally:
        my_window.quit()

HOST='127.0.0.1'
PORT=33000
BUFSIZE=1024
FORMAT="utf8"
CLIENT=socket(AF_INET,SOCK_STREAM)
#connect to sever

def catchHost():
    ip=ipHost_box.get()
    port=portHost_box.get()
    print(ip)
    print(port)
    port=int(port)
    try:
        CLIENT.connect((ip,port))
        __init__()
    except:
        print("Server is not responding")
        error404()


def entryHost():
    entry_host=Frame(frame)
    tempIMG=(Image.open("nottech.jpg"))
    startImg=tempIMG.resize((800,420),Image.ANTIALIAS)
    new_image= ImageTk.PhotoImage(startImg)
    label = Label(entry_host, image=new_image)
    label.image = new_image
    label.place(x=0, y=0)
    Label(entry_host, font=("iCiel Crocante",15),bg="#fff").pack()
    iput_host=Frame(entry_host)
    iput_host.configure(bg="#fff")
    iput_host.pack()
    ipHost=Label(iput_host, text="IP",fg="#333", font=("iCiel Crocante",15),bg="#fff").pack()
    global ipHost_box
    global portHost_box
    ipHost_box=Entry(iput_host,width=20,fg="blue",font=("iCiel Pacifico",20),justify='center',borderwidth=5)
    ipHost_box.pack()
    portHost=Label(iput_host, text="Port",fg="#333", font=("iCiel Crocante",15),bg="#fff").pack()
    portHost_box=Entry(iput_host,width=20,fg="blue",font=("iCiel Pacifico",20),justify='center',borderwidth=5)
    portHost_box.pack()

    host_btn=Button(entry_host,text="Submit",command=catchHost,bg="#000",fg="#fff", font=("Arial", 15), width=10)
    host_btn.pack(pady=5)
    changeOnHoverButton(host_btn)
    entry_host.grid(row=0,column=0,sticky='nsew')
    entry_host.tkraise()

entryHost()


# MainSearch()
my_window.protocol("WM_DELETE_WINDOW", on_closing)

my_window.mainloop()
