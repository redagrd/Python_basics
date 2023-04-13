'''
    la classe maison comprend 2 attributs :
        - porte : objet de type porte
        - surface : type float

    elle possède une méthode display qui affiche les infos de la maison
'''

from Porte import Porte

class Maison:

    def __init__(self, attr_surface, color):
        '''
        initialisation de la surface
        :param attr_surface: int
        :param color: str
        '''
        self.surface = attr_surface
        self.__porte = Porte(color)     # composition de porte dans Maison


    @property
    def surface(self):
        return self.__surface

    @surface.setter
    def surface(self, value):
        if type(value) != int:
            raise TypeError("Veuillez renseigner des nombres entiers")
        self.__surface = value

    def affichage(self):
        '''
            Méthode permettant d'afficher la surface
        :return: str
        '''
        return f"j'ai une maison, qui a une surface de {self.surface} m2"

    def getPorte(self):
        '''
        Méthode permettant d'accéder à l'objet porte en lecture
        '''
        return self.__porte