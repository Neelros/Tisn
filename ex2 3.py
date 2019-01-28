ch=input("Entrez votre mot")
hc=""
for i in range(len(ch)):
    hc=hc+ch[-i+len(ch)-1]
print(hc)
if hc==ch:
    print("Votre mot est un palindrome")
else:
    print("Votre mot n'est pas un palindrome")