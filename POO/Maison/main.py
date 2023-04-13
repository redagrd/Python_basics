'''
    fichier d'execution du programme maison
'''

from Maison import Maison
from Appartement import Appartement
from Person import Person

maison = Maison(150, "blanche")
appartement = Appartement("noire")
cyriak = Person("Cyriak", maison)
marie = Person("Marie", appartement)
cyriak.affichage()
marie.affichage()