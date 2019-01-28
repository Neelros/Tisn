from tkinter import *

def p():
    global x1,x2,y1,y2,d
    x1,y1,x2,y2=x1+d,y1,x2+d,y2
    can.coords(b,x1,y1,x2,y2)
    if x2>1200:
        d=-1*d
    print(x1,y1,x2,y2)
    if x1<=0:
        d=d*-1

x1,x2,y1,y2,d=0,50,10,60,20
fen = Tk()
can=Canvas(fen,bg='green',height=700,width=1200)
b=can.create_oval(x1,y1,x2,y2,width=2,fill='yellow')
bou1=Button(fen,text='Pousser la balle',command=p)
bou1.pack(side=BOTTOM)
can.pack()
fen.mainloop()