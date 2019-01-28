l=['Louise','Audrey','Jean','Maximilien','Christine']
m=[]
p=[]
for i in range (len(l)):
    if len(l[i])>6:
        p.append(l[i])
    else:
        m.append(l[i])
print (p,m)

