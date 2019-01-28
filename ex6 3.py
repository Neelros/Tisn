from tkinter import *
from math import *

def p():
    global x1,x2,y1,y2,a
    a=a+pi/8
    x1,y1,x2,y2=x1+50*cos(a),y1+50*sin(a),x2+50*cos(a),y2+50*sin(a)
    can.coords(b,x1,y1,x2,y2)
    can.create_line(x1+23,y1+23,x2-23,y2-23,width=2,fill='red')


x1,y1,x2,y2=500,50,550,100
a=0
fen = Tk()
can=Canvas(fen,bg='light blue',height=550,width=1000)
b=can.create_oval(x1,y1,x2,y2,width=2,fill='yellow')
bou1=Button(fen,text='Lancer la balle dans un cercle trigonométrique infini',command=p)
bou1.pack(side=BOTTOM)
can.pack()
fen.mainloop()