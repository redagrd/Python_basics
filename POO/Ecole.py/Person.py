"""
– Créez une classe « Person »
– Créez une classe « Student » et une autre classe « Teacher », les deux héritent de la classe « Person ».
– La classe « Student » aura une méthode publique « GoToClasses », qui affichera à l’écran « I’m going
to class. ».
– La classe « Teacher » aura une méthode publique « Explain », qui affichera à l’écran « Explanation
begins ». En plus, il aura un attribut privé « subject » de type string.
– La classe « Person » doit avoir une méthode « SetAge(int n) » qui indiquera la valeur de leur âge (par 
exemple, 15 years old).
– La classe « Student » aura une méthode publique « DisplayAge » qui écrira sur l’écran « My age is: 
XX years old ».
– Vous devez créer une autre classe de test appelée « Test » qui contiendra « Main » et:
– Créez un objet Person et faites-lui dire « Hello »
– Créer un objet Student, définir son âge à 15 ans, faites-lui dire « Hello », « I’m going to class. » et 
afficher son âge
– Créez un objet Teacher, 40 ans, demandez-lui de dire « Hello » puis commence l’explication
"""
"""
class Person:


    def __init__(self, age):
        self.age = age
        return print(f"Age: {self.age}")
    
    def Bonjour(self):
        return "Hello"
"""
from abc import ABC, abstractmethod

class Person(ABC): # héritage de la metaclass ABC (classe abstraite)
    '''
    classe abstraite (ne peut être instancié)
    '''

    def __init__(self, age):
        '''
        initialisation de l'age
        :param age: int
        '''
        self.age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if type(value) != int: # dans le cas ou ce n'est pas un  entier
            raise TypeError("Veuillez renseigner un age") # lève une exception
        self.__age = value

    def Hello(self):
        '''
        retourne Hello
        :return: str
        '''
        return "Bonjour"

    @abstractmethod
    def affichage(self):    # méthode abstraite, oblige les enfants à la redéfinir
        pass
