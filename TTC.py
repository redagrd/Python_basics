"""

Calcul d'un prix TTC.

Creer un script qui demande le prix hors taxe
d'un article.
Pus qui demande si l'article est de la nourriture
ou non.
Le script doit calculer le prix ttc selon si
c'est de la nourriture ou non.

rappel, pour les biens communs la TVA c'est 20.0%
sinon c'est 5.5% pour la nourriture

"""
article = int(input("le prix de votre article "))
food = bool(input("votre article est il de la nourriture "))

if food == True:
        print(article*0.055 + article)
else:
        print(article*1.20 + article)
