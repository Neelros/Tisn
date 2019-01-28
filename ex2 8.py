l=input("Entrez vos lettres")
l=list(l)
print(l)
m=input("Quel mot proposez vous?")
m=list(m)
print(m)
c=0
for i in range (len(m)):
    for j in range (len(l)):
        if m[i]==l[j]:
            l[j]="*"
            c=c+1
            print(l)
            j=len(l)+1
if c==(len(m)):
    print("Le tirage est bon")
print(c)