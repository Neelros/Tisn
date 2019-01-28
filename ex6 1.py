from tkinter import *
from math import *

def pointeur(event):
    global X,Y
    chaine.configure(text='Clic detecte en X=' + str(event.x)+", Y="+str(event.y))
    X=event.x
    Y=event.y

def p1():
    global x1,x2,x3,x4,y1,y2,y3,y4,X,Y
    x1,y1,x2,y2=X-10,Y-10,X+10,Y+10
    can.coords(o1,x1,y1,x2,y2)
    print(0.00000000000667*((100*500)/(((x1+10)-(x3-30))**2+((y1+10)-(y3-30))**2)))

def p2():
    global x1,x2,x3,x4,y1,y2,y3,y4,X,Y
    x3,y3,x4,y4=X-30,Y-30,X+30,Y+30
    can.coords(o2,x3,y3,x4,y4)
    print(0.00000000000667*((100*500)/(((x1+10)-(x3-30))**2+((y1+10)-(y3-30))**2)))

x1,y1,x2,y2,x3,y3,x4,y4=0,0,0,0,0,0,0,0
fen = Tk()
can=Canvas(fen,bg='dark blue',height=700,width=1200)
can.bind("<Button-1>",pointeur)
o1=can.create_oval(x1,y1,x2,y2,width=2,fill='blue')
bou1=Button(fen,text='Planète bleue',command=p1)
bou1.pack()
o2=can.create_oval(x3,y3,x4,y4,width=2,fill='yellow')
bou2=Button(fen,text='Planète jaune',command=p2)
bou2.pack()
texte=Label(fen,text="Masse planète bleue:100 kg, masse planète jaune: 500kg",fg='black')
texte.pack(side=TOP)
d=sqrt(((x1+10)-(x3-30))**2+((y1+10)-(y3-30))**2)
text1=Label(fen,text=d,fg='black')
text1.pack(side=BOTTOM)
f=(0.00000000000667*((100*500)/(((x1+10)-(x3-30))**2+((y1+10)-(y3-30))**2)))
text2=Label(fen,text=f,fg='black')
text2.pack(side=BOTTOM)
can.pack()
chaine=Label(fen)
chaine.pack()
fen.mainloop()
