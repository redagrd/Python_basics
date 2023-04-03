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

