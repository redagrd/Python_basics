"""
Donner un algorithme qui détermine le prix d'entré dans un cinéma. (Les mineurs payent 5 euros, les autres
10 euros).
"""
age = int(input("quel est votre age ? "))
if age >= 18:
    print("le prix est de 10 euros")
else:
    print("le prix est de 5 euros")
7