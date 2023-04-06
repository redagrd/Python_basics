"""
LeJustePrix !

But de l'exercice :
    
Votre programme génère un nombre aléatoire
entre 1 et 1 000.

Il demande ensuite à l'utilisateur de proposer
un nombre.

L'utilisateur entre un nombre dans la console :
    - Si celui-ci est plus petit que le nombre généré, le programme affiche :
    "C'est PLUS !" et demande un nouveau nombre.
    - Si celui-ci est plus grand que le nombre généré, le programme affiche :
    "C'est MOINS !" et demande un nouveau nombre.
    - Si celui-ci est le nombre généré aléatoirement, le programme affiche :
    "C'est GAGNÉ !" puis l'exécution du programme se termine.

Le nombre d'essaie de l'utilisateur est limité à 10 :
    - Chaque tour, le programme affiche le nombre de tours restants à
    l'utilisateur
    - Si au bout de 10 essais l'utilisateur n'a pas trouvé le nombre,
    le programme affiche : "C'est PERDU ! Le nombre était : nombreAleatoire"
    puis l'exécution du programme se termine.

"""

#TODO
#Pour le nombre aléatoire, utiliser la fonction
# random.randint(1,1000)
#N'oubliez pas d'importer le module random : 
# import random

import random
prix = random.randint(1,1000)
nombre_essais = 10

while nombre_essais >= 0: #si le nombre d'essais n'est pas arrivé à terme
    nb = int(input("Entrez un prix: "))
    if nb == prix:
        print("C'est GAGNÉ !")
        break #permet de mettre fin à la boucle
    elif nb < prix:
        print("C'est PLUS !")
    else:
        print("C'est MOINS !")
    nombre_essais -= 1 #permet d'enlever un essais à chaque erreur
    print("il vous reste", nombre_essais, "vie")
    if nombre_essais == 0: #si le nombre d'essais est arrivé à zero, affiche la réponse
        print("C'est PERDU ! Le nombre était", prix)

"""
autre méthode:

import random

def inputNombre():
    nombre = int(input("entrez un nombre : "))

def JustePrix():

"""