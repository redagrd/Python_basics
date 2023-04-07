"""
Écrivez une classe appelée « Student » avec les membres suivant :
    •nom (de type String),
    •note1, note2 (de type int)
Le programme demande à l’utilisateur d’entrer le nom et les notes. calc_moy() calcule la note 
moyenne et show() affiche le nom et la note moyenne 
"""

class Student:

    def __init__(self, nom, note1, note2):
        self.nom = nom
        self.note1 = 0
        self.note2 = 0

    def Entre(self):
        self.__nom = input("entrez votre nom: ")
        self.__note1 = int(input("entrez votre première note/20 : "))
        self.__note2 = int(input("entrez votre seconde note/20 : "))

    @property
    def nom(self):
        return self.__nom
    
    @property
    def note1(self):
        return self.__note1
    
    @property
    def note2(self):
        return self.__note2
    
    @nom.setter
    def nom(self, nom):
        if type(nom) == str :
            self.__nom = nom
        else:
            raise TypeError("Il faut des lettres")

    @note1.setter
    def note1(self, a):
        if type(a) == int or type(a) == float :
            self.__note1 = a
        else:
            raise TypeError("Il faut un nombre")
    @note2.setter
    def note2(self, b):
        if type(b) == int or type(b) == float :
               self.__note2 = b
        else:
               raise TypeError("Il faut un nombre")

    def Calcul(self):
        return (self.__note1 + self.__note2) //2

    def Show(self):
        print("votre nom est : ", self.__nom, " et votre moyenne est : ", self.Calcul())