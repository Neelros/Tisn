s=0
s=int(input("Quelle somme voulez vous retirer ?"))
if s%10!= 0:
    print("Je ne peux pas vous verser cette somme")
else:
    print(s//500, "billets de 500")
    s=s%500
    print(s//200, "billets de 200")
    s=s%200
    print(s//100, "billets de 100")
    s=s%100
    print(s//50,"billets de 50")
    s=s%50
    print(s//20,"billets de 20")
    s=s%20
    print(s//10,"billets de 10")
    s=s%10