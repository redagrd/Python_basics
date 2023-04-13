"""
Écrivez une classe « Somme » ayant deux variables « n1 » et « n2 » et une fonction membre « sum() » 
qui calcule la somme. Dans la méthode principale main demandez à l’utilisateur d’entrez deux entiers 
et passez-les au constructeur par défaut de la classe « Somme » et afficher le résultat de l’addition des 
deux nombres
"""

class Somme:

    def __init__(self, n1, n2):  # constructeur, on initialise avec None
        self.n1 = None
        self.n2 = None

    def Sum(self):  # calcul
        return self.__n1 + self.__n2
    pass

    @property
    def n1(self):
        return self.__n1

    @property
    def n2(self):
        return self.__n2

    @n1.setter
    def n1(self, a):
        if type(a) == int or type(a) == float:
            self.__n1 = a
        else:
            raise TypeError("Il faut un nombre")

    @n2.setter
    def n2(self, b):
        if type(b) == int or type(b) == float:
            self.__n2 = b
        else:
            raise TypeError("Il faut un nombre")

    def n2(self, b):
        self.__n2 = b

    def entre(self):  # défini l'entrée utilisateur
        self.__n1 = int(input("Entrez le premier nombre: "))
        self.__n2 = int(input("Entrez le deuxième nombre: "))