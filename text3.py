  
from tkinter import *
import tkinter

flag=True
def st(num):
    global flag
    if num==0:
        if flag:
            b1.config(text="O")
        else:
            b1.config(text="X")
        b1.config(state=DISABLED)
    elif num==1: # and b2.cget("text")=="":
        if flag:
            b2.config(text="O")
        else:
            b2.config(text="X")
        b2.config(state=DISABLED)
    elif num==2:
        if flag:
            b3.config(text="O")
        else:
            b3.config(text="X")
        b3.config(state=DISABLED)
    elif num==3:
        if flag:
            b4.config(text="O")
        else:
            b4.config(text="X")
        b4.config(state=DISABLED)
    elif num==4:
        if flag:
            b5.config(text="O")
        else:
            b5.config(text="X")
        b5.config(state=DISABLED)
    elif num==5:
        if flag:
            b6.config(text="O")
        else:
            b6.config(text="X")
        b6.config(state=DISABLED)
    elif num==6:
        if flag:
            b7.config(text="O")
        else:
            b7.config(text="X")
        b7.config(state=DISABLED)
    elif num==7:
        if flag:
            b8.config(text="O")
        else:
            b8.config(text="X")
        b8.config(state=DISABLED)
    elif num==8:
        if flag:
            b9.config(text="O")
        else:
            b9.config(text="X")
        b9.config(state=DISABLED)
    flag= not flag 

    if b1.cget('text')==b2.cget('text') and b1.cget('text')==b3.cget('text'):
        if b1.cget('text')=='O':
            print("O win")
        elif b1.cget('text')=='X':
            print('X win')
    if b4.cget('text')==b5.cget('text') and b4.cget('text')==b6.cget('text'):
        if b4.cget('text')=='O':
            print("O win")
        elif b4.cget('text')=='X':
            print('X win')
    if b7.cget('text')==b8.cget('text') and b7.cget('text')==b9.cget('text'):
        if b7.cget('text')=='O':
            print("O win")
        elif b7.cget('text')=='X':
            print('X win')
    if b1.cget('text')==b4.cget('text') and b1.cget('text')==b7.cget('text'):
        if b1.cget('text')=='O':
            print("O win")
        elif b1.cget('text')=='X':
            print('X win')
    if b2.cget('text')==b5.cget('text') and b2.cget('text')==b8.cget('text'):
        if b2.cget('text')=='O':
            print("O win")
        elif b2.cget('text')=='X':
            print('X win')
    if b3.cget('text')==b6.cget('text') and b3.cget('text')==b9.cget('text'):
        if b3.cget('text')=='O':
            print("O win")
        elif b3.cget('text')=='X':
            print('X win')
    if b1.cget('text')==b5.cget('text') and b1.cget('text')==b9.cget('text'):
        if b1.cget('text')=='O':
            print("O win")
        elif b1.cget('text')=='X':
            print('X win')
    if b3.cget('text')==b5.cget('text') and b3.cget('text')==b7.cget('text'):
        if b3.cget('text')=='O':
            print("O win")
        elif b3.cget('text')=='X':
            print('X win')


w=Tk()
w.geometry("600x600+100+50")
w.title("啥時才能打到疫苗")
w.rowconfigure(0,weight=1)
w.rowconfigure(1,weight=1)
w.rowconfigure(2,weight=1)
w.columnconfigure(0,weight=1)
w.columnconfigure(1,weight=1)
w.columnconfigure(2,weight=1)

b1=Button(w,text="",command=lambda:st(0))
b1.grid(row=0,column=0,sticky=NSEW)
b2=Button(w,text="",command=lambda:st(1))
b2.grid(row=0,column=1,sticky=NSEW)
b3=Button(w,text="",command=lambda:st(2))
b3.grid(row=0,column=2,sticky=NSEW)

b4=Button(w,text="",command=lambda:st(3))
b4.grid(row=1,column=0,sticky=NSEW)
b5=Button(w,text="",command=lambda:st(4))
b5.grid(row=1,column=1,sticky=NSEW)
b6=Button(w,text="",command=lambda:st(5))
b6.grid(row=1,column=2,sticky=NSEW)

b7=Button(w,text="",command=lambda:st(6))
b7.grid(row=2,column=0,sticky=NSEW)
b8=Button(w,text="",command=lambda:st(7))
b8.grid(row=2,column=1,sticky=NSEW)
b9=Button(w,text="",command=lambda:st(8))
b9.grid(row=2,column=2,sticky=NSEW)

w.mainloop()