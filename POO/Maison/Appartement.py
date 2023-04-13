'''
    - la classe appartement hérite de maison et force la surface à 50
'''
from Maison import Maison

class Appartement(Maison):
    def __init__(self, color):
        '''
        Initialisation des attributs de l'appartement
        :param color: str
        '''
        super().__init__(50, color) # on surcharge le constructeur parent
        # Maison.__init__(self, 50, color) # autre possibilité pour surcharger

    def affichage(self):
        '''
        Méthode permettant d'afficher les détails de l'appartement
        :return: str
        '''
        return f"J'ai un appartement ayant une surface de {self.surface} m2"