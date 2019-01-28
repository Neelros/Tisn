chaine= "hello"
hc=""
for i in range(len(chaine)):
    hc=hc+chaine[-i+len(chaine)-1]
print(hc)