'''
    classe personne possède 2 attributs
    - nom de type str
    - maison de type Maison
    - display pour afficher les détails de la personne, de la maison et de la porte
'''

from Maison import Maison

class Person:

    def __init__(self, attr_nom, attr_logement: Maison):    # Agrégation de maison ou Appartement dans Person
        '''
        initialisation des attributs
        :param attr_nom: str
        :param attr_logement: objet Maison ou objet Porte
        '''
        self.nom = attr_nom
        self.__logement = attr_logement

    @property
    def nom (self):
        return self.__nom

    @nom.setter
    def nom(self, value):
        if len(value) < 2 :     # la taille du nom doit être à minima de 2 caractères
            raise ValueError("Veuillez avoir un nom de plus d'une lettre") # levée de l'exception dans le cas contraire
        self.__nom = value  # creation de l'attribut et affectation de la valeur

    def affichage(self):
        """
        méthode permettant d'afficher le nom de la personne, ainsi que son logement et les informations de la porte du logement
        :return: None
        """
        print(f"je m'appelle {self.nom}, {self.__logement.affichage()}, {self.__logement.getPorte().affichage()}")

# lorsque ce fichier est lancé directement sans passé par un autre (lorsqu'il est exécuté, on crée une instance de la classe Person)
if __name__ == "__main__":
    maison = Maison(150, "blanche")
    personne = Person("Cyriak", Maison)
    personne.affichage()