s=int(input("Entrer le nombre de secondes"))
m=s//60
s=s%60
j=m//1440
m=m%1440
o=j//30
j=j%30
a=o//12
o=o%12
print("Cela fait",a,"années",o,"mois",j,"jours",m,"minutes",s,"secondes")