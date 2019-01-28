from tkinter import *
from random import randrange

def drawline(): #fonction tracer ligne
    global x1,y1,x2,y2,coul
    can1.create_line(x1,y1,x2,y2,width=2,fill=coul) #rectangle=diagonales,oval=cercle ds rect
    y2,y1=y2-10,y1-10

def drawline2(): #fonction viseur
    global x3,y3,x4,y4,rouge
    can1.create_line(250,0,250,650,width=2,fill=rouge)
    can1.create_line(0,325,500,325,width=2,fill=rouge)

def changecolor(): #fonction changement couleur
    global coul
    pal=['cyan','maroon','green'] #liste couleur
    c=randrange(2) #choisit couleur dans liste
    coul=pal[c] #def couleur

x1,y1,x2,y2=0,500,500,500 #pour // passer mm coordonnées 2
rouge='red'
coul='dark green'
fen1=Tk()
can1=Canvas(fen1,bg='dark grey',height=650,width=500) #def dimensions fen et couleur du fond
can1.pack(side=LEFT) #met fen à droite
bou1=Button(fen1,text='Quitter',command=fen1.quit) #crée boutton quitter dans fentre 1
bou1.pack(side=BOTTOM) #le place en bas
bou2=Button(fen1,text='Tracer une ligne',command=drawline) #crée boutton tracer ligne dans fen1
bou2.pack()
bou3=Button(fen1,text='Autre couleur',command=changecolor) #crée bouton changer couleur
bou3.pack()
bou4=Button(fen1,text='Viseur',command=drawline2)
bou4.pack()

fen1.mainloop()
fen1.destroy()