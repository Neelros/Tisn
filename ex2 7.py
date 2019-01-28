from random import*
m=input("Entrez un mot")
m=list(m)
print(m)
for i in range(len(m)):
    n=randint(0,len(m)-1)
    l=m[n]
    del m[n]
    u=randint(0,len(m)-1)
    m.insert(u,l)
print(m)
