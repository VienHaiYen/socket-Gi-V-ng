from tkinter import *
from tkinter import ttk

def callback():
    text=cmb.get()
    print(text)
    
window=Tk()
window.title('Combobox') 
window.geometry('300x200')

course=["none","Pizza1","Burger","Noodles","Pizza2","Pizza3","Pizza4","Pizza5","Pizza6","Pizza7","Pizza8"]

l1=Label(window,text="Choose Your Favorite Food")
l1.grid(column=0, row=0)
cmb=ttk.Combobox(window,values=course,width=30,)
cmb.grid(column=0, row=1)

btn=Button(window,text="Click Here",command=callback)
btn.grid(column=0, row=2)

l2=Label(window,text="")
l2.grid(column=0, row=3)
window.mainloop()