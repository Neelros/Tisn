def eleMax(liste,debut,fin):
    liste=liste[debut:fin]
    liste.sort()
    x=liste[-1]
    print(x)
liste=[1,57,45,13,25,10]
eleMax(liste,0,3)