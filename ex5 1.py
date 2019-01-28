from tkinter import *
from random import *

def damier():
    y1=0
    for z in range (5):
        x1=0
        for i in range (5):
            can1.create_rectangle(x1,y1,x1+50,y1+50,width=1,fill='black')
            can1.create_rectangle(x1+50,y1+50,x1+100,y1+100,width=1,fill='black')
            x1=x1+100
        y1=y1+100

def pions():
    l=randint(1,10)
    c=randint(1,10)
    can1.create_oval((l-1)*50,(c-1)*50,(l*50),(c*50),width=1,fill='light yellow')


fen1=Tk()
can1=Canvas(fen1,bg='white',height=500,width=500)
can1.pack(side=LEFT)
bou1=Button(fen1,text='Quitter',command=fen1.quit)
bou1.pack(side=BOTTOM)
bou2=Button(fen1,text='Damier',command=damier)
bou2.pack()
bou3=Button(fen1,text='Pions',command=pions)
bou3.pack()


fen1.mainloop()
fen1.destroy()