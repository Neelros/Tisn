from tkinter import *
from random import randrange
# +15 +20 rapport

def ann1(): #fonction tracer anneau
    can1.create_oval(40,40,120,120,width=5,outline='blue')

def ann2(): #fonction tracer anneau
    can1.create_oval(80,100,160,180,width=5,outline='yellow')

def ann3(): #fonction tracer anneau
    can1.create_oval(120,40,200,120,width=5,outline='black')

def ann4(): #fonction tracer anneau
    can1.create_oval(160,100,240,180,width=5,outline='green')

def ann5(): #fonction tracer anneau
    can1.create_oval(200,40,280,120,width=5,outline='red')



fen1=Tk()
can1=Canvas(fen1,bg='white',height=250,width=500) #def dimensions fen et couleur du fond
can1.pack(side=LEFT) #met fen à droite
bou1=Button(fen1,text='Quitter',command=fen1.quit) #crée boutton quitter dans fentre 1
bou1.pack(side=BOTTOM) #le place en bas
bou2=Button(fen1,text='Anneau 1',command=ann1)
bou2.pack()
bou3=Button(fen1,text='Anneau 2',command=ann2)
bou3.pack()
bou4=Button(fen1,text='Anneau 3',command=ann3)
bou4.pack()
bou5=Button(fen1,text='Anneau 4',command=ann4)
bou5.pack()
bou6=Button(fen1,text='Anneau 5',command=ann5)
bou6.pack()

fen1.mainloop()
fen1.destroy()