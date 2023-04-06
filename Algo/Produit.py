"""
    Ecrire un algo qui demande deux nombre a l'utilisateur et qui va vérifier si le produit des deux nombre est positif ou négatif ou nul
    Mais on ne réalise pas le calcul
"""
"""
#faux il y a un calcul
nb1 = int(input("Entrez un nombre "))
nb2 = int(input("Entrez un autre nombre "))

if nb1 * nb2 > 1:
    print("le nombre est positif")
if nb1 * nb2  < 0:
    print("le nombre est négatif")
if nb1 * nb2 == 0:
    print("le nombre est nul")
"""

nb1 = int(input("Entrez un nombre "))
nb2 = int(input("Entrez un autre nombre "))

if nb1 == 0 or nb2 == 0:
    print("le produit est nul")
elif(nb1>0 and nb2>0) or (nb1<0 and nb2<0):
    print("le produit est positif")
else:
    print("le produit est négatif")