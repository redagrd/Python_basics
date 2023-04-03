"""
    Ecrire un algo qui demande un nombre entier positif et qui nous retourne le carré de ce nombre
    Un carré est le résultat de la multiplication du nombre par lui même
    On peux pousser un peux et ajouter la vérification de la donnée avec une boucle "while"
"""

nb = int(input("entrez un nombre entier positif "))
while nb <= 1: int(input("entrez un nb supérieur à 1 svp"))
carre = nb **2
print ("le carré de", nb, "est", carre )
