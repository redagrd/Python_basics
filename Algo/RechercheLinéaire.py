"""
Algorithme pour recherche lineaire:
Cet algo a pour but de chercher trés simplement un element dans 
un tableau et de retourner sa postion.

Il suffit de parcourir un par un les elements d'un tableau
 jusqu'a trouver celui demander.

"""
import random # import de la librairie random pour generer un nombre aléatoire
arr = []

# bout de code pour remplir un tableau de 500 nombres aléatoires compris entre 0 et 1000
for i in range(500):
    arr.append(random.randrange(0,1000))

# élément a trouver
elem = 42
cptrange = 0
for cpt in range(len(arr)): #parcours la liste
    cptrange += 1 #compteur de comparaison
    if arr[cpt] == elem: #si l'element est trouvé dans l'index de arr
        print("l'element est a la position: ", cpt)
        break #on sort de la boucle
if cptrange == len(arr): #si le compteur est égal a la taille du tableau
    print("l'element n'est pas dans le tableau")