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
from Person import Person
"""
class Teacher:
    def __init__(self, attr_):
        pass

    def Explain(self, exp):
        self.exp = " Explaination begins"
        return print(self.exp)
"""  

class Teacher(Person): # héritage de la classe Person

    def __init__(self, attr_age, attr_subject):
        '''
        Initialise les attributs age et sujet
        :param attr_age:
        :param attr_subject:
        '''
        super().__init__(attr_age) # surcharge du constructeur parent (Person)
        self.subject = attr_subject # ajoute le sujet à l'objet


    @property
    def subject(self):
        return self.__subject

    @subject.setter
    def subject(self, value):
        if type(value) != str :
            raise TypeError("Veuillez renseigner une phrase")
        self.__subject = value

    def Hello(self):
        '''
        retourne Hello
        :return: str
        '''
        return super().Hello() + " à tous"

    def affichage(self):
        '''
        retourne une chaine de caractère avec appel des méthodes Hello et subject
        :return: None
        '''
        print(f"{self.Hello()}, Explication {self.subject} commence.")

if __name__ == "__main__":
    prof = Teacher(40, "Math")
    prof.affichage()
