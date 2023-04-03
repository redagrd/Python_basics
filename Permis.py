"""
Permis :

Un permis de chasse à points possède au départ 
un capital de 100 points.

Si le chasseur tire sur (on sait pas si la cibl à survecue) :
    - une poule, il perd 1 point,
    - un chien, il perd 3 points,
    - une vache, il perd 5 points,
    - un autre chasseur, il perd 25.

Écrire un script qui  permet de calculer le nombre de point perdus.
sachant qu'un permis coute 200 euros,
calculer en fonction de son tableau de chasse,
le cout déboursé par ce chasseur.

"""

"""
def points():
     poule = int(input("Entrez le nombre poules"))
     chien = int(input("Entrez le nombre chiens"))
     vache = int(input("Entrez le nombre vaches"))
     chasseur = int(input("Entrez le nombre chasseurs"))
     return points
"""
def inputNombre(msg):
    try:
        test = int(input(msg))
    except ValueError as e:
        print(e)
        print(" il faut taper un nombre !!! ")
        test = inputNombre(msg)
    return test

# fonction qui regroupe toutes les demandes d'input
def safari():
    poules = inputNombre("Combien de poules ?")
    chiens = inputNombre("Combien de chiens ?")
    vaches = inputNombre("Combien de vaches ?")
    chasseurs = inputNombre("Combien de chasseurs ?")
    return poules, chiens, vaches, chasseurs

# fonction qui decompte le coup des permis perdus
def persSup(nb):
    nbrePermis = 0
    while nb > 0:
        nb -= 100
        nbrePermis += 1
    if nb < 0:
        nb = abs(nb)
    else:
        nb = 100
    return (200*nbrePermis), nb


# fonction qui decompte le nombre totale de points perdus
def pertePoints(p, c, v, a):
    pointsPerdus = p + 3*c + 5*v + 25*a
    if pointsPerdus > 0:
        print("le chasseur a perdu "+str(pointsPerdus)+" points")
    else :
        print("le chasseur n'a pas perdu de point")
    return pointsPerdus

# Programme principal
def partieChasse():
    poules, chiens, vaches, chasseurs = safari()
    pertepts = pertePoints(p=poules, c=chiens, v=vaches, a=chasseurs)# on pré-assigne les variable pour ne pas ce tromper
    payer, reste = persSup(pertepts)
    print("le cout reviens a :", end=' ')
    if payer == 0:
        print("rien à payer")
    else :
        print(payer, "euros")
    print("et il lui reste : "+str(reste)+" points")


# appel du programme principale
partieChasse()