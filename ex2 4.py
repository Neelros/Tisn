ph="hello world"
m="sos"
t=""
for i in range (len(ph)):
        t=t+ph[i]+m[i%(len(m))]
print (t)