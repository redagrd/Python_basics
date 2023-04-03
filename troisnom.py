"""
    Ecrire un algo qui demander 3 variable de type String qui sont des noms et qui va vérifier si il sont entrée dans l'ordre alphabétique
    On pourrait pousser l'exercice plus loin en triant les nom si il ne le sont pas de base 
"""
noms = ["Reda", "Helene", "Florent"]

for i in noms:
    if "Florent" <= "Helene" <= "Reda":
        print(noms.sort())
    else:
        print(True)
