def nomMois(n):
    if n==1:
        print("Janvier")
    elif n==2:
        print("Février")
    elif n==3:
        print("Mars")
    elif n==4:
        print("Avril")
    elif n==5:
        print("Mai")
    elif n==6:
        print("Juin")
    elif n==7:
        print("Juillet")
    elif n==8:
        print("Aout")
    elif n==9:
        print('Septembre')
    elif n==10:
        ("Octobre")
    elif n==11:
        ("Novembre")
    elif n==12:
        ("Decembre")
    else:
        print("Votre mois n'existe pas")
n=int(input("Entrez votre n mois"))
nomMois(n)