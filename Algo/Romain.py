"""
Romain :

Ecrir un script qui permet de saisir un entier 
entre 1 et 3999
(pourquoi cette limitation ?).

Le script doit permettre de l'afficher en 
chiffre romain.

En bonus : le convertisseur inverse
"""
romain = {
    1:"I", 2:"II", 3:"III", 4:"IV", 5:"V", 6:"VI", 7:"VII", 8:"VIII", 9:"IX", 10:"X",
    20:"XX", 30:"XXX", 40:"XL", 50:"L", 60:"LX", 70:"LXX", 80:"LXXX", 90:"XC", 100:"C",
    200:"CC", 300:"CCC", 400:"CD", 500:"D", 600:"DC", 700:"DCC", 800:"DCCC", 900:"CM",
    1000:"M", 2000:"MM", 3000:"MMM"
}
entrer = int(input("Entrez un nombre entier entre 1 et 3999 :"))
for cpt in romain.items(): #parcourt le dictionnaire
    if entrer >= cpt[0]:
        print(cpt[1]) #affiche la cle du dictionnaire
    elif entrer > 3999:
        print("Le nombre doit etre compris entre 1 et 3999")
    elif entrer < 1:
        print("Le nombre doit etre compris entre 1 et 3999")


