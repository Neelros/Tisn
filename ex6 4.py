from tkinter import *
from math import *
from random import *
p,v=[],[]
x3,x4,y3,y4,d=0,50,110,160,50

def dep():
    global x3,y3,x4,y4,d
    x3,y3,x4,y4=x3+d,y3,x4+d,y4
    can.coords(b,x3,y3,x4,y4)
    if x4>700:
        d=-1*d
    elif x3<=0:
        d=d*-1


def f():
    p=c[randint(0,1)]
    if p==c[0]:
        v=c[1]
        can.itemconfig(o1,fill=p)
        can.itemconfig(o2,fill=p)
        can.itemconfig(o3,fill=v)
        can.itemconfig(o4,fill=v)

    elif p==c[1]:
        v=c[0]
        can.itemconfig(o1,fill=p)
        can.itemconfig(o2,fill=p)
        can.itemconfig(o3,fill=v)
        can.itemconfig(o4,fill=v)
        dep()



fen = Tk()
can=Canvas(fen,bg='dark grey',height=700,width=700)
c=['red','green']
x1=50
y1=100
x2=100
y2=600
for i in range (6):
    can.create_rectangle(x1,y1,x2,y2,width=2,fill='yellow')
    x1=x1+100
    x2=x2+100
o1=can.create_oval(0,50,50,100,width=10,outline='black',fill='black')
o2=can.create_oval(600,50,650,100,width=10,outline='black',fill='black')
o3=can.create_oval(0,650,50,700,width=10,outline='black',fill='black')
o4=can.create_oval(600,650,650,700,width=10,outline='black',fill='black')
bou1=Button(fen,text='Changement couleur',command=f)
bou1.pack(side=BOTTOM)
b=can.create_oval(x3,y3,x4,y4,width=2,fill='white')
can.pack()
fen.mainloop()