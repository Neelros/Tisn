def indexMax(liste):
    liste.sort()
    x=liste[-1]
    print(liste.index(x),x)
liste=[12,1,450,120]
indexMax(liste)