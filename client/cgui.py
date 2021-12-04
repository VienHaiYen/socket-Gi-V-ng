
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
    try:
        clearFrame()
    except:
        pass
    global second_big_frame_result
    second_big_frame_result=Frame(second_big_frame_blank)
    second_big_frame_result.pack(fill=BOTH,expand=1)
    loading=Label(second_big_frame_result,text="Loading",font=("Arial",10,"italic"),fg="grey", width=15)
    loading.pack(fill=BOTH)
    second_big_frame_result.update_idletasks()

    global my_canvas
    my_canvas=Canvas(second_big_frame_result)
    my_canvas.pack(side=LEFT, fill=BOTH,expand=1)
    
    
    global my_scrollbar
    my_scrollbar=ttk.Scrollbar(second_big_frame_result, orient=VERTICAL,command=my_canvas.yview)
    my_scrollbar.pack(side=RIGHT, fill=Y)
    second_big_frame_result.focus_force()
    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind('<Configure>', lambda e:my_canvas.configure(scrollregion=my_canvas.bbox("all")))
    global second_frame
    second_frame=Frame(my_canvas)
    my_canvas.create_window((0,0), window=second_frame, anchor="nw")


    global outFrame
    outFrame=Frame(second_frame)


    n=1
    Label(outFrame,text="Brand",font=("Arial",10,"bold"),fg="blue", width=15).grid(column=1,row=n)
    Label(outFrame,text="Company",font=("Arial",10,"bold"),fg="blue", width=10).grid(column=2,row=n)
    Label(outFrame,text="Brand1",font=("Arial",10,"bold"),fg="blue", width=10).grid(column=3,row=n)
    Label(outFrame,text="Type",font=("Arial",10,"bold"),fg="blue", width=30).grid(column=4,row=n)
    Label(outFrame,font=("Arial",10,"bold"),fg="blue",text="Buy").grid(column=5,row=n)
    Label(outFrame,font=("Arial",10,"bold"),fg="blue",text="Sell").grid(column=6,row=n)
    for i in range (0,len(result)):
        n=n+1
        Label(outFrame, text='   '+result[i]['brand']+'   ').grid(column=1,row=n)
        Label(outFrame, text='   '+result[i]['company']+'   ').grid(column=2,row=n)
        Label(outFrame, text='   '+result[i]['brand1']+'   ').grid(column=3,row=n)
        Label(outFrame, text='   '+result[i]['type']+'   ').grid(column=4,row=n)
        Label(outFrame, text=' '+result[i]['buy']+' ').grid(column=5,row=n)
        Label(outFrame, text=' '+result[i]['sell']+' ').grid(column=6,row=n)
    outFrame.pack(fill=BOTH)
    outFrame.wait_visibility()
    loading.destroy()

def recvResult(conn):
    length=conn.recv(BUFSIZE).decode(FORMAT)
    conn.send(bytes(length.encode(FORMAT)))
    length=int(length)
    response=b''
    while len(response)<length:
        response=response+conn.recv(BUFSIZE)
    response=response.decode(FORMAT)
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
    star_page.focus_force()

def __init__():
    startPage()
def clearFrame():
    # destroy all widgets from frame
    second_big_frame_result.destroy()

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
    INPUT3=datecomb.get()
    if INPUT1=='':
        INPUT1='none'
    if INPUT2=='':
        INPUT2='none'
    searchkey=[INPUT1,INPUT2,INPUT3]
    sendList(searchkey)
    result=recvResult(CLIENT)
    if len(result)==0:
        onErrorSearching()
    else:
        outputResult(result)
def updateBrand(e):
    typed=brand_box.get()
    if typed=="":
        data=guilist['brand']
    else:
        data=[]
        for i in guilist['brand']:
            if typed.lower() in i.lower():
                data.append(i)
    brand_box['value']=data
    #brand_box.focus_force()

def MainSearch():
    sendOption("GETGUILIST")
    # Dạng dict ["brand": [],"company": []]
    global guilist
    guilist=recvResult(CLIENT)
    guilist['brand'].insert (0, '')
    guilist['company'].insert (0, '')

    global search_page
    search_page=Frame(frame)
    search_page.configure(bg="#fff")
    my_window.geometry("780x700")
    my_window.title('Tim kiem Vang')
    search_page.tkraise()
    search_page.focus_force()

    tempIMG=(Image.open("square.png"))
    startImg=tempIMG.resize((500,300),Image.ANTIALIAS)
    new_image= ImageTk.PhotoImage(startImg)
    label = Label(search_page, image=new_image)
    label.image = new_image
    label.place(x=0, y=0)

    label2 = Label(search_page, image=new_image)
    label2.image = new_image
    label2.place(x=500, y=0)

    label3 = Label(search_page, image=new_image)
    label3.image = new_image
    label3.place(x=1000, y=0)

    label4 = Label(search_page, image=new_image)
    label4.image = new_image
    label4.place(x=1500, y=0)

    # Label(search_page,text="", font=("ROBOTO",10)).pack(pady=10)
    input_bar=Frame(search_page)
    input_bar.pack(pady=10)
    # Label(input_bar,text="      ").grid(column=1,row=0)
    Label(input_bar, text="Date",font=("Arial",10,"bold"),justify="left").grid(column=1,row=1)
    global datecomb
    global brand_box
    global company_box

    datecomb=ttk.Combobox(input_bar,justify="center",width=25,font=("Arial",10))
    datecomb['value']=guilist['date']
    datecomb.current(0)
    datecomb.grid(column=1,row=2)
    

    Label(input_bar,text="      ").grid(column=2,row=1)
    Label(input_bar, text="Gold Brand",font=("Arial",10,"bold"),justify="left").grid(column=3,row=1)
    brand_box=ttk.Combobox(input_bar,justify="center",width=25,font=("Arial",10))
    brand_box['value']=guilist['brand']
    brand_box.current(0)
    brand_box.grid(column=3,row=2)
    brand_box.bind("<KeyRelease>",updateBrand)
    # brand_box=Entry(input_bar,width=25,justify='center',font=("Arial",12))
    # brand_box.pack()

    Label(input_bar,text="      ").grid(column=4,row=1)
    Label(input_bar, text="Gold Company",font=("Arial",10,"bold"),justify="left").grid(column=5,row=1)
    company_box=ttk.Combobox(input_bar,justify="center",width=25,font=("Arial",10))
    company_box['value']=guilist['company']
    company_box.current(0)
    company_box.grid(column=5,row=2)
    # company_box=Entry(input_bar,width=25,justify='center',font=("Arial",12))
    # company_box.pack()
    # Label(input_bar,text="      ").grid(column=6,row=1)

    Label(input_bar,text="           ").grid(column=7,row=0)

    tempIMG=(Image.open("exit.png"))
    startImg=tempIMG.resize((25,30),Image.ANTIALIAS)
    new_image= ImageTk.PhotoImage(startImg)
    exit_btn = Button(input_bar, image=new_image,border=False,command=logOut)
    exit_btn.image = new_image
    exit_btn.grid(column=8,row=0,rowspan=2)

    btn_frame=Frame(search_page)
    # btn_frame.grid(column=7,row=1,rowspan=2)
    btn_frame.pack()
    submitbtn=Button(btn_frame, text="SUBMIT",font=("Arial",10,"bold"),width=15, command=transfer,bg="#333", fg="#fff")
    submitbtn.grid(column=1, row=1)
    changeOnHoverButton(submitbtn)
    Label(btn_frame,text="   ").grid(column=2, row=1)
    clearbtn=Button(btn_frame, text="Clear all Resuls",font=("Arial",10,"bold"),width=20, command=clearFrame,bg="#333",fg="#fff")
    clearbtn.grid(column=3, row=1)
    Label(btn_frame,text="\t\t\t\t").grid(column=4, row=1)
    changeOnHoverButton(clearbtn)
    Label(search_page,text="", font=("ROBOTO",10)).pack(pady=10)
    search_page.grid(row=0,column=0,sticky='nsew')

    global second_big_frame_blank
    second_big_frame_blank=Frame(search_page)
    second_big_frame_blank.pack(fill=BOTH,expand=1)



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
    Label(input_signin, text="User Name:", font=("Arial",10),bg="#fff").grid(column=1, row=1)
    username_box=Entry(input_signin)
    username_box.grid(column=2, row=1)
    Label(input_signin, text="   ", height=1,font=("Arial",2)).grid(column=1, row=2)
    Label(input_signin, text="Password: ", font=("Arial",10),bg="#fff").grid(column=1, row=3)
    password_box=Entry(input_signin,show="*")
    password_box.grid(column=2, row=3)
    confirm=Button(sign_in,text="Sign-in Account",bg="#000", fg="#fff",command=saveNewAcc,width=20)
    confirm.place(x=310,y=170)
    out_line=Button(sign_in,text="Back to StarPage",bg="#fff", fg="#000",border=False,command=startPage,width=20)
    out_line.place(x=310,y=220)
    changeOnHoverText(out_line)
    changeOnHoverButton(confirm)
    username_box.focus_set()
    password_box.bind("<Return>",saveNewAcc)

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
def onErrorLostConnection():
    mbox.showerror("Error", "Sever đã đóng!")

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

def logOut():
    sendOption('LOGOUT')
    startPage()

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
    password_box_log=Entry(input_login,show="*")
    password_box_log.grid(column=2, row=3)
    confirm=Button(log_in,text="Log-in Account",bg="#000", fg="#fff",command=confirmAcc,width=20)
    confirm.place(x=62,y=170)
    out_line=Button(log_in,text="Go back to StartPage",bg="#fff", fg="#000",border=False,command=startPage,width=20)
    out_line.place(x=62,y=220)
    changeOnHoverText(out_line)
    changeOnHoverButton(confirm)

    username_box_log.focus_set()
    password_box_log.bind("<Return>",confirmAcc)

    log_in.grid(row=0,column=0,sticky='nsew')
    log_in.tkraise()

def sendList(list):
    for item in list:
        CLIENT.sendall(item.encode(FORMAT))
        #wait response
        CLIENT.recv(1024)
    msg = "end"
    CLIENT.send(msg.encode(FORMAT))
def confirmAcc(e=""):
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
error_server.grid(row=0,column=0,sticky='nsew')

def error404():
    my_window.title('Not responsding')
    my_window.geometry('600x600')

    error_server.tkraise()
    error_server.focus_force()


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

def catchHost(e=""):
    ip=ipHost_box.get()
    port=int(portHost_box.get())
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
    ipHost_box.focus_set()
    portHost_box.bind("<Return>",catchHost)
    entry_host.grid(row=0,column=0,sticky='nsew')
    entry_host.tkraise()

entryHost()

my_window.protocol("WM_DELETE_WINDOW", on_closing)
my_window.mainloop()
