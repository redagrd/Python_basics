"""
Train :

Un train est parti de la gare du Nord à 9 h
(il y a 170 km entre la gare du Nord et Arras).

Écrire un script qui affiche un tableau me permettant de connaître
l'heure à laquelle le train passe à Arras.

Le tableau prédira les différentes heures possibles:
pour toutes les vitesses de 100 km/h à 300 km/h, par pas de 10 km/h,
les résultats étant arrondis à la minute inférieure.

Écrire une fonction tchoutchou qui reçoit la vitesse du train et
qui affiche l'heure du passage;

Écrire le programme principal qui affiche le tableau demandé.


"""
tableau = "vitesse | heure\n"
distance = 170
for cpt in range(100, 301, 10):
    heure = 9 + distance / cpt
    tableau += str(cpt) + " km/h | " + str(heure) + "h\n"
    print(tableau)