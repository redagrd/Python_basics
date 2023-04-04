#
"""
    Ecrire un programme de tri par selection:

    Le tri par selection a pour principe de chercher l'element le plus petit
     d'un tableau puis de le placer au debut du tableau

    par exemple:

    tableau de depart: 8 , 5 , 1 , 7 , 6 , 4

    premiere iteration: 1 , 5 , 8 , 7 , 6 , 4

    deuxieme iteration: 1 , 4 , 8 , 7 , 6 , 5

    troisieme iteration: 1 , 4 , 5 , 7 , 6 , 8

    quatrieme iteration: 1 , 4 , 5 , 6 , 7 , 8

    cinquieme iteration: le tableau est dans l'ordre fin du tri

"""
#
"""
for cpt in range(len(liste)): #boucle de selection
    for i in range(len(liste)-1): #boucle de comparaison
        if liste[i+1] < liste[i]: #si l'element suivant est plus petit
            liste[i], liste[i+1] = liste[i+1], liste[i] #on swap
print(liste)
"""
liste = [8 , 5 , 1 , 7 , 6 , 4]
#liste1 = liste.sort
#while liste1[0] < liste1[1]:
#    liste1
liste1 = min(liste)
for cpt in range(len(liste)):
    min_index = cpt
    for i in range(cpt+1, len(liste)):
        if liste[i] < liste[min_index]:
            min_index = i
    liste[cpt], liste[min_index] = liste[min_index], liste[cpt]
print(liste)

