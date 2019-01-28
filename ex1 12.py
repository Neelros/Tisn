from random import *
j=0
o=0
#1 pierre 2 feuille 3 ciseaux
j=int(input("1=pierre, 2=feuille, 3=ciseaux"))
o=randint(1,3)
print(o)
if o==j:
    print("Egalite")
else:
    if o==1 and j==2:
        print("Vous avez gagné")
    else:
        if o==1 and j==3:
            print("Vous avez perdu")
        else:
            if o==2 and j==1:
                print("Vous avez perdu")
            else:
                if o==2 and j==3:
                    print("Vous avez gagné")
                else:
                    if o==3 and j==1:
                        print("Vous avez gagné")
                    else:
                        if o==3 and j==2:
                            print("Vous avez perdu")
                        else:
                            print("Impossible")
