"""
    Ecrire un programme de tri a bulle:

    Le principe du tri a bulle est de comparer un element d'un tableau 
    avec son voisin suivant,
    si l'element est plus grand que son voisin, on inverse les positions
    sinon passe à l'élément suivant
    Astuce :
        Au lieu de passer par une variable temporaire
        python permet de swap:
            liste[i], liste[i+1] = liste[i+1], liste[i]

"""
liste = [8 , 5 , 1 , 7 , 6 , 4]
for cpt in range(len(liste)):
    for i in range(len(liste)-1):
        if liste[i+1] < liste[i]:
            liste[i], liste[i+1] = liste[i+1], liste[i]
print(liste)

"""
print("la liste avant d'être trier: ")
print(liste)
while flag:
    flag = False
    for index in range(len(liste)-1):
        if liste[index+1] < liste[index]:
            flag = True
            liste[index], liste[index+1] ) liste[index+1], liste[index]

print("voici la liste après son tri :")
print(liste)
"""