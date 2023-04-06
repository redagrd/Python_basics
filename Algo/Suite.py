"""
Creer un script qui demande une suite
de nombres positifs ou nuls.

calculez la somme de cette suite
à chaque nombre ajouté.
Comptez combien il y avait de données et
combien étaient supérieures à 100.

afficher le resultat et continer.

Entrer un nombre inférieur à 0 indique la fin de la suite.
"""
"""
nb = int(input("Choisissez une suite de nombres positive ou nulle "))
j = 0
i = 0
#toujouts mettre la variable avant le int dans la boucle(ici nb:)
while nb >= 0:
        nb = int(input("Choisissez une autre suite de nombres positive ou nulle "))
        i += nb
        print(i)
        if nb < 100:
                print(i += nb)
"""

# fonction qui assure l'affichage des differentes variables
def affichage_resultat(nombreTotal, nombreGrands):
    print(nombreTotal, "valeur(s) en tout,")
    print("dont :", nombreGrands, "supérieure(s) à 100")

# fonction qui demande un nombre entier
def inputNombre(msg):
    try:
        prop = int(input(msg))
    except ValueError as e:
        print(e)
        print(" il faut taper un nombre !!! ")
        prop = inputNombre(msg)
    return prop

# Programme principal
def suite100():
    # definition de plusieurs variables d'un coup
    somme, nombreTotal, nombreGrands = 0, 0, 0
    affichage=""
    affichageSup100=""
    x = 0
    while x >= 0:
        somme += x
        nombreTotal += 1
        print("La somme est :", somme)
        if x > 100:
            nombreGrands += 1
            affichageSup100 += "%i "%(x) #on affiche la valeur entiere de X
        x = inputNombre("entrer un nombre (un négatif pour terminer) ?")
        affichage += f"{x} "

    # affichage des resultats
    affichage_resultat(nombreTotal, nombreGrands)
    print("liste des >100 : ", affichageSup100)
    print("liste des chiffres : ",affichage)
    
suite100()