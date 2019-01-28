from math import *
x=sqrt (2)
t=int(input("Entrer n de la troncure à n chiffres de racine carrée de 2"))
x= x*10**t
x= int(x)
x= x/10**t
print(x)