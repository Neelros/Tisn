nb=int(input("Entrer une année"))
if nb%400==0 or (nb % 4 == 0 and nb %100 !=0) :
   print("bissextile")
else:
    print("pas bissextile")