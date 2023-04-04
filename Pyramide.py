"""
But de l'exercice :

Reprendre l'exercice 1 Triangle
Votre programme demande un nombre positif à l'utilisateur.
Il affiche un triangle d'astérisques dont la taille dépend du nombre.
Mais cette fois affiché sous forme de pyramide centré

     *
    * *
   * * *
  * * * *
 * * * * *
"""
"""
nb = int(input("Entrez un nombre positif "))
while nb <= 1: int(input("entrez un nb supérieur à 1 svp"))

i = 0


while i <= nb:
    print((nb-i)* " ", (i*"* "))
    i +=1
"""

#autre méthode
nb = int(input("Entrez un nombre positif "))
while nb <= 1: int(input("entrez un nb supérieur à 1 svp"))
espace = " "
etoiles = "* "
i = 0
j = 0
k = 0
for i in range (nb): 
    for j in range ((nb + 1) - i): 
        espace += " " 
        for k in range(i):
            espace += etoiles