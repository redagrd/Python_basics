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


class Student(Person):  # héritage de la classe Person
    
    def __init__(self, age):
        super().__init__(age)  # appel du constructeur de la classe Person

    def goToClasse(self):
        '''
        retourne i'm going to class
        :return: str
        '''
        return "Je vais en classe"

    def affichage(self):
        '''
        methode qui retourne une chaine de caractère en implementant les méthodes age et goToClass
        :return: None
        '''
        print(f"j'ai {self.age} ans et {self.goToClasse()}")


if __name__ == "__main__":
    etudiant = Student(15)
    etudiant.affichage()
