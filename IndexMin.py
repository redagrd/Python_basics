"""
Index Minimum:

Ecrir un script qui permet de generer une liste 
de nombres entiers aleatoires,
de taille et de borne définis.


Utiliser la fonction randint(a, b) du module random.

Le script doit permettre de recuperer l'index de l'element le plus petit,
puis de le dépacer en premier position.

liste1 = min(liste)
for cpt in range(len(liste)): #boucle de selection
    min_index = cpt #on initialise l'index du minimum
    for i in range(cpt+1, len(liste)): #boucle de comparaison
        if liste[i] < liste[min_index]: #si l'element suivant est plus petit
            min_index = i 
    liste[cpt], liste[min_index] = liste[min_index], liste[cpt] #on swap
print(liste)
"""
import random
arr = []
for i in range(500):
    arr.append(random.randrange(0,1000))

arr1 = min(arr)
for cpt in range(len(arr)): #boucle de selection
    min_index = cpt #on initialise l'index du minimum
    for i in range(cpt+1, len(arr)): #boucle de comparaison
        if arr[i] < arr[min_index]: #si l'element suivant est plus petit
            min_index = i 
    arr[cpt], arr[min_index] = arr[min_index], arr[cpt] #on swap
print(arr)
               
