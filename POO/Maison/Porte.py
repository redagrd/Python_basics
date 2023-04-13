'''
    la classe door possède un attribut color de type str
    - elle possède une méthode display qui donne les détails de la porte

'''

class Porte:

    def __init__(self, attr_couleur):
        '''
        Initialisation de l'attribut couleur
        :param attr_couleur: str
        '''
        self.couleur = attr_couleur

    @property
    def couleur(self):
        return self.__couleur

    @couleur.setter
    def couleur(self, value):
        value = value.lower() # on passe la chaine de caractère en minuscule
        couleurs = ("rouge", "verte", "bleue", "jaune", "orange", "violette", "rose", "grise", "blanche", "noire")  # echantillon de couleurs

        if value not in couleurs:   # dans le cas ou la couleur n'est pas dans la liste
            raise TypeError("Veuillez renseigner une couleur")  # on lève l'exception
        self.__couleur = value  # Sinon, on crée l'attribut et on lui affecte la valeur de value

    def affichage(self):
        '''
            Méthode permettant d'afficher les détails de la porte
        :return:
        '''
        return f"qui contient une porte {self.couleur}"