from tkinter import *
from random import randrange

def drawline(): #fonction tracer ligne
    global x1,y1,x2,y2,coul
    can1.create_line(x1,y1,x2,y2,width=2,fill=coul)
    y2,y1=y2+10,y1-10

def changecolor(): #fonction changement couleur
    global coul
    pal=['purple','red','blue','orange','yellow''cyan','maroon','green'] #liste couleur
    c=randrange(2) #choisit couleur dans liste
    coul=pal[c] #def couleur

x1,y1,x2,y2=10,190,190,10
coul='dark green'
fen1=Tk()
can1=Canvas(fen1,bg='dark grey',height=200,width=200) #def dimensions fen et couleur du fond
can1.pack(side=LEFT) #met fen à droite
bou1=Button(fen1,text='Quitter',command=fen1.quit) #crée boutton quitter dans fentre 1
bou1.pack(side=BOTTOM) #le place en bas
bou2=Button(fen1,text='Tracer une ligne',command=drawline) #crée boutton tracer ligne dans fen1
bou2.pack()
bou3=Button(fen1,text='Autre couleur',command=changecolor) #crée bouton changer couleur
bou3.pack()

fen1.mainloop()
fen1.destroy()