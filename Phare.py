"""
Phare :

Un gardien de phare doit se rendre au toillette 5 fois par jour.
Malheuresement, elle se trouve au rez-de-chaussé.

Creer un script qui permet calculer pour x marche de y cm
la distance parcourue par semaine de se gardien de phare.

astuce : une fois terminer il doit remonté

bonus : afficher une tour qui à la largeur des marches en *
et un nombre d'etage correspondant au nombre de marches

"""
nb_marches = int(input("entrez le nombre de marches: "))
hauteur_marches = int(input("entrez la hauteur des marches en cm: "))
distance = nb_marches * hauteur_marches *2 *5 *7
distanceKM = distance / 100
print("le gardien à parcouru", distanceKM, "km par semaines")

affichage = ""
etoiles = "* "
cpt = 0
for cpt in range(nb_marches+1):
    for j in range( ((nb_marches+1)-cpt)):
        affichage+= " "
        for k in range(cpt):
            affichage += etoiles
            affichage += "\n"
print(affichage)
