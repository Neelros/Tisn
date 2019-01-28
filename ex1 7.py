m=t=0
m=eval(input("Quelle est votre masse en kg?"))
t=eval(input("Quelle est votre taille en m?"))
imc=(m/t**2)
print (imc)
if imc > 25 :
    print ("Vous devez manger plus equilibre et faire de l'exercice regulierement")
elif imc < 18.5 :
    print ("Mangez plus")
else :
    print ("Votre IMC est ideal")
