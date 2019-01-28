from tkinter import *
from random import *
x1,y1,x2,y2=0,0,0,0
j=0

def neige():
    pn=PhotoImage(file='perenoel1.gif')
    can1.create_image(10,20,image=pn)
    global x1,y1,x2,y2,j
    for i in range (250):
        j=randrange(15)
        x1=randint(0,1000)
        y1=randint(0,1000)
        x2,y2=x1+j,y1+j
        can1.create_oval(x1,y1,x2,y2,width=2,fill='white')
        i=i+1

fen1=Tk()
can1=Canvas(fen1,bg='black',height=500,width=1000)
can1.pack(side=TOP)
bou1=Button(fen1,text='Neige !',command=neige)
bou1.pack(side=BOTTOM)
bou2=Button(fen1,text='Quitter',command=fen1.quit)
bou2.pack(side=BOTTOM)
txt=can1.create_text(500,200,text='Bataille de boules de neige!', fill='dark grey',font=40)


fen1.mainloop()
fen1.destroy()