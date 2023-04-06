"""
    Ecrire un algo qui demande un nombre a l'utilisateur et qui va vérifier si ce nombre est positif ou négatif ou nul
    
"""
nb = int(input("Entrez un nombre "))
if nb > 0:
    print("le nombre est positif")
elif nb < 0:
    print("le nombre est négatif")
elif nb == 0:
    print("le nombre est nul")