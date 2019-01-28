md='labyrinthe'
md=list(md)
m='**********'
m=list(m)
c=0
print("Jeu du pendu.Vous avez 15 coups")
while c <=15:
    l=input("Entrez une lettre pour deviner le mot!")
    print(l)
    for i in range (len(md)):
        if l==md[i]:
            m[i]=md[i]
            print("Votre lettre est dans le mot.",m,"Vous en êtes à votre",c+1,"tour")
            l=input("Entrez une lettre pour deviner le mot!")
            print(l)
        else:
            c=c+1
            print("Votre lettre n'est pas dans le mot.")
            l=input("Entrez une lettre pour deviner le mot!")
            print(l)
    if m==md:
        print("Bravo! Vous avez trouvé le mot:",m)
print("Fin de jeu")