from tkinter import *
mot=""

def ok():
    global choix,mot
    mot = choix.get()
    if mot=='HELLO':
        print('Bravo!')

fen=Tk()
fen.geometry('500x250')
text1=Label(fen,text='LOLHE',fg='red')
text1.pack(side=TOP)
choix=Entry()
choix.pack(side=TOP)
bou1=Button(fen,text='Quitter',command=fen.quit)
bou1.pack(side=BOTTOM)
bou2=Button(fen,text='Valider',command=ok)
bou2.pack(side=TOP)
fen.mainloop()
fen.destroy()
