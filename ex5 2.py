from tkinter import *
from random import *
o=0

def p():
    global o
    bou3.destroy()
    bou4.destroy()
    o=randint(1,3)
    if o==1:
        bou6.destroy()
        bou7.destroy()
        text3.config(text='Egalité')
    elif o==2:
        bou5.destroy()
        bou7.destroy()
        text3.config(text='Vous avez perdu')
    elif o==3:
        bou5.destroy()
        bou6.destroy()
        text3.config(text='Vous avez gagné')

def f():
    global o
    bou2.destroy()
    bou4.destroy()
    o=randint(1,3)
    if o==1:
        bou6.destroy()
        bou7.destroy()
        text3.config(text='Vous avez gagné')
    elif o==2:
        bou5.destroy()
        bou7.destroy()
        text3.config(text='Egalité')
    elif o==3:
        bou5.destroy()
        bou6.destroy()
        text3.config(text='Vous avez perdu')

def c():
    global o
    bou2.destroy()
    bou3.destroy()
    o=randint(1,3)
    if o==1:
        bou6.destroy()
        bou7.destroy()
        text3.config(text='Vous avez perdu')
    elif o==2:
        bou5.destroy()
        bou7.destroy()
        text3.config(text='Vous avez gagné')
    elif o==3:
        bou5.destroy()
        bou6.destroy()
        text3.config(text='Egalité')


fen=Tk()
fen.geometry('500x250')
bou1=Button(fen,text='Quitter',command=fen.quit)
bou1.pack(side=BOTTOM)
text1=Label(fen,text=('Votre choix:'),fg='red')
text1.pack(side=TOP)
bou2=Button(fen,text='Pierre',command=p)
bou2.pack(side=TOP)
bou3=Button(fen,text='Feuille',command=f)
bou3.pack(side=TOP)
bou4=Button(fen,text='Ciseaux',command=c)
bou4.pack(side=TOP)
text2=Label(fen,text=('Ordinateur:'),fg='red')
text2.pack(side=TOP)
bou5=Button(fen,text='Pierre')
bou5.pack(side=TOP)
bou6=Button(fen,text='Feuille')
bou6.pack(side=TOP)
bou7=Button(fen,text='Ciseaux')
bou7.pack(side=TOP)
text3=Label(fen,text=('Résultat'),fg='red')
text3.pack(side=BOTTOM)

fen.mainloop()
fen.destroy()
