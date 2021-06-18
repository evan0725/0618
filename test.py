from enum import EnumMeta
from tkinter import *
import hashlib
from tkinter.font import names 

s256=hashlib.sha256()
btnLabs=["7","8","9","/",
         "4","5","6","*",
         "1","2","3","-",
         "0",".","(","+",
         ")","C","EXIT","="]

def Login():
    idData=ei.get()
    pwData=ep.get()
    if len(idData)>0 and len(pwData)>0:
        s256.update(pwData.encode('utf8'))
        pwH=s256.hexdigest()
        # print(pwH)
        if idData=="h304" and pwH=="9af15b336e6a9619928537df30b2e6a2376569fcf9d7e773eccede65606529a0":
            root.deiconify()
            top.destroy()
        else:
            ei.delete(0,"end")
            ep.delete(0,"end")
    else:
        ei.delete(0,"end")
        ep.delete(0,"end")

def Exit():
    top.destroy()
    root.destroy()

def click(btnStr):
    return lambda:btnClick(btnStr)

def btnClick(btnStr):
    if btnStr=="EXIT":
        root.destroy()
    elif btnStr in ["+","-","*","/","(",")","."] or btnStr in map(str,range(0,10)):
        if cLab['text']=="0":
            cLab['text']=btnStr
        else:
            cLab['text']+=btnStr
    elif btnStr=="=":
        cLab('text')=str(eval(cLab['text']))
    elif btnStr=="C":
        cLab['text']=="0"


root=Tk()
root.geometry("400x300+100+100")
top=Toplevel(root)
labID=Label(top,text="ID",anchor=E,justify=RIGHT,font=("Times",20))
labPw=Label(top,text="PASSWORD",anchor=E,justify=RIGHT,font=("Times",20))
ei=Entry(top)
ep=Entry(top,show="*")
btnLogin=Button(top,text="LOGIN",command=Login)
btnExit=Button(top,text="EXIT",command=Exit)

labID.grid(row=0,column=0,sticky=NSEW)
ei.grid(row=0,column=1,sticky=NSEW)
labPw.grid(row=1,column=0,sticky=NSEW)
ep.grid(row=1,column=1,sticky=NSEW)
btnLogin.grid(row=2,column=0,sticky=NSEW)
btnExit.grid(row=2,column=1,sticky=NSEW)

root.rowconfigure(0,weight=1)
root.rowconfigure(1,weight=1)
root.rowconfigure(2,weight=1)
root.rowconfigure(3,weight=1)
root.rowconfigure(4,weight=1)
root.rowconfigure(5,weight=1)
root.columnconfigure(0,weight=1)
root.columnconfigure(1,weight=1)
root.columnconfigure(2,weight=1)
root.columnconfigure(3,weight=1)

cLab=Label(root,text="0",bg="#0080FF",font=("Times",20),anchor=E,justify=RIGHT)
cLab.grid(row=0,column=0,sticky=NSEW,columnspan=4)

i=0
btns=[]
for btnLab in btnLabs:
    btn=Button(root,text=btnLab,command=click(btnLab),font=("Times",20))
    btns.append(btn)
    btn.grid(row=i//4+1,column=i%4,sticky=NSEW)
    i+=1

root.withdraw()
root.mainloop()