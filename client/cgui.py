from tkinter import *
from tkinter import ttk
import tkinter
from PIL import Image, ImageTk
from tkinter import scrolledtext
import json
import tkinter.messagebox as mbox
import re


my_window =Tk()
my_window.title('Client Version')
my_window.geometry("400x350")

load=Image.open('white.jpg')
render=ImageTk.PhotoImage(load)
img=Label(my_window, image=render)
img.place(x=0, y=0)

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
    my_canvas.configure(yscrollcommand=my_scrollbar.set, width=750, height=100)
    my_canvas.bind('<Configure>', lambda e:my_canvas.configure(scrollregion=my_canvas.bbox("all")))
    global second_frame
    second_frame=Frame(my_canvas)
    my_canvas.create_window((0,0), window=second_frame, anchor="nw")

    global outFrame
    outFrame=Frame(second_frame)
    Label(outFrame,text="        ").grid(column=0,row=1)
    n=1
    Label(outFrame,text="Brand", width=10).grid(column=1,row=n)
    Label(outFrame,text="Company", width=10).grid(column=2,row=n)
    Label(outFrame,text="Brand1", width=10).grid(column=3,row=n)
    Label(outFrame,text="Type", width=30).grid(column=4,row=n)
    Label(outFrame,text="Buy").grid(column=5,row=n)
    Label(outFrame,text="Sell").grid(column=6,row=n)
    outFrame.pack(fill=BOTH)
    for i in range (0,len(result)):
        n=n+1
        Label(outFrame, text=' '+result[i]['brand']+' ').grid(column=1,row=n)
        Label(outFrame, text='  '+result[i]['company']+' ').grid(column=2,row=n)
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
        noti_box.geometry("300x70")
        # noti=Label(noti_box, text="Error: Nothing has this Brand=\" " + a+ '\" Company=\"'+b+" \"", fg="red", font=("Arial",10, "bold")).pack(expand=True)
        noti=Label(noti_box, text="Cannot find you request!!").pack(expand=True)
    else:
        title=Label(second_big_frame, text="Kết quả trả về cho Brand=\"" + a+ '\" Company=\"'+b+" \"", font=("Arial",10,"bold"), fg="#006699").pack()
        outputResult(result)

def __init__():

    frame=Frame(my_window)
    frame.pack()
    Label(frame, text="Hi Client",font=("Humblle Rought All Caps",30) ).pack(pady=30)
    signin=Button(frame,text="Đăng ký", width=25,command=sigIn,fg="#fff", bg="#333",font=(".VnSouthern",12, "bold")).pack(padx=20, pady=10)
    # login=Button(frame,text="Đăng nhập",width=20, command=MainSearch).pack(padx=20, pady=10)
    login=Button(frame,text="Đăng nhập",width=25, command=logIn,fg="#fff", bg="#333",font=(".VnSouthern",12, "bold")).pack(padx=20, pady=10)

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
    global search_page
    search_page=Toplevel()
    search_page.geometry("800x700")
    search_page.title('ăn ở do trời')
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
    sign_in=Toplevel()
    sign_in.title('Sign-In')
    sign_in.geometry('400x300')
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
    sign_in_btn=Button(sign_in,text="Sign-in Account",bg="#000", fg="#fff",command=saveNewAcc)


    sign_in_btn.pack(pady=20)


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

def errorFinding():
    mbox.showerror("Error", "Không tìm được từ khóa")

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
    log_in=Toplevel()
    log_in.title('Log-In')
    log_in.geometry('400x300')
    Label(log_in, text="Đăng nhập tài khoản", font=("Arial",15)).pack(pady=20)
    input_login=Frame(log_in)
    input_login.pack()
    global username_box_log, password_box_log
    username=Label(input_login, text="User Name:").grid(column=1, row=1)
    username_box_log=Text(input_login,width=20,height=1)
    username_box_log.grid(column=2, row=1)
    Label(input_login, text="   ", height=1,font=("Arial",2)).grid(column=1, row=2)
    password=Label(input_login, text="Password: ").grid(column=1, row=3)
    password_box_log=Text(input_login,width=20,height=1)
    password_box_log.grid(column=2, row=3)
    log_in_btn=Button(log_in,text="Sign-in Account",bg="#000", fg="#fff",command=confirmAcc)
    log_in_btn.pack(pady=20)


def confirmAcc():
    global user_log
    global password_log
    user_log=username_box_log.get("1.0", END).strip('\n')
    print("tên dang nhập" + user_log)
    password_log=password_box_log.get("1.0", END).strip('\n')
    print("pass dang nhập" +password_log)
    with open('D:/Destop/testing_python/server/infoclient.json', 'r', encoding='utf8') as f:
        data=json.load(f)
        print(data)
    f.close()
    accounts=data['account']

    for i in range (0, len(accounts)):
        if accounts[i]["username"]==user_log and accounts[i]["password"]==password_log:
            MainSearch()
            return
    onErrorLogIn()


# MainSearch()
__init__()

# saveNewAcc()
my_window.mainloop()

