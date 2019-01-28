t='hseolslsoo swsoorslsdo'
ph=''
m=''
for i in range (len(t)):
    if i%2==0:
        ph=ph+t[i]
    else:
        m=m+t[i]
print(ph,m[0:3])
