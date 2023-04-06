"""
Donner un algorithme qui détermine le prix d'entré dans un cinéma. (Les mineurs payent 5 euros, les autres
10 euros) avec un Dictionnaire de données

"""
prix = prix = {"mineur":5, "majeur":10}

age = input("Etes vous majeur ou mineur ? ")

if age == "mineur":
    prix_entree = prix["mineur"]
else:
    prix_entree = prix["majeur"]
print("le prix est de ", prix_entree)