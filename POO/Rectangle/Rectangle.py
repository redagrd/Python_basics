"""
Écrivez une classe « Rectangle » ayant deux variables « a » et « b » et une fonction membre 
« surface() » qui retournera la surface du rectangle.

"""
class Rectangle:

    def __init__(self, longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur

    def area(self):
        print(f"aire du rectangle: {self.__longueur * self.__largeur}")

    @property
    def longueur(self):
        return self.__longueur
    
    @property
    def largeur(self):
        return self.__largeur
    
    @longueur.setter
    def longueur(self, longueur):
        if type(longueur) == int or type(longueur) == float :
            self.__longueur = longueur
        else:
            raise TypeError("Il faut un nombre")
    
    @largeur.setter
    def largeur(self, largeur):
        if type(largeur) == int or type(largeur) == float :
            self.__largeur = largeur
        else:
            raise TypeError("Il faut un nombre")


