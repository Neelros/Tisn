from tkinter import *
from random import *

ta=0
b1=randint(1,9)
b2=randint(1,9)
b3=randint(1,9)
b4=randint(1,9)
b5=randint(1,9)
t=randint(1,40)

def s1():
    bou2.destroy()
    global ta
    ta=ta+b1
    text2.config(text=('Total actuel',ta))
    if ta==t:
        

def s2():
    bou3.destroy()
    global ta
    ta=ta+b2
    text2.config(text=('Total actuel',ta))


def s3():
    bou4.destroy()
    global ta
    ta=ta+b3
    text2.config(text=('Total actuel',ta))


def s4():
    bou5.destroy()
    global ta
    ta=ta+b4
    text2.config(text=('Total actuel',ta))


def s5():
    bou6.destroy()
    global ta
    ta=ta+b5
    text2.config(text=('Total actuel',ta))


fen=Tk()
fen.geometry('500x250')
bou1=Button(fen,text='Quitter',command=fen.quit)
bou1.pack(side=BOTTOM)
bou2=Button(fen,text=b1,command=s1)
bou2.pack(side=TOP)
bou3=Button(fen,text=b2,command=s2)
bou3.pack(side=TOP)
bou4=Button(fen,text=b3,command=s3)
bou4.pack(side=TOP)
bou5=Button(fen,text=b4,command=s4)
bou5.pack(side=TOP)
bou6=Button(fen,text=b5,command=s5)
bou6.pack(side=TOP)
text3=Label(fen,text="En attente",fg='red')
text3.pack(side=BOTTOM)
text1=Label(fen,text=('Total à atteindre:',t),fg='red')
text1.pack(side=BOTTOM)
text2=Label(fen,text=('Total actuel',ta),fg='red')
text2.pack(side=BOTTOM)
fen.mainloop()
fen.destroy()
