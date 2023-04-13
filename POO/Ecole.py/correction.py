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


class Person:
    """_summary_ : Une personne est n'importequi inscrit sur notre application. Il possède obligatoirement un nom et un prénom. L'age est optionnel.

    """

    def __init__(self, nom, prenom) -> None:
        self.nom = nom
        self.prenom = prenom
        self.age = None

    def setAge(self, age: int):
        """_summary_ : Change l'âge de la Personne

        Args:
            age (int): Le nouvel âge
        """
        self.age = age

    def saluer(self):
        print("Bonjour !")


class Student(Person):
    def __init__(self, nom, prenom, classe) -> None:
        super().__init__(nom, prenom)
        self.classe = classe

    def GoToClasses(self):
        return print("I'm going to class.")

    def displayAge(self):
        if self.age == None:
            print(f"{self.nom} n'a pas d'age")
        else:
            print(f"My age is {self.age} years old")


class Teacher(Person):
    def __init__(self, nom, prenom, subject) -> None:
        super().__init__(nom, prenom)
        self.__subject = subject

    def Explain(self):
        """_summary_ : Affiche un message en précisant le sujet
        """
        print("Explanation about", self.__subject,"begins.")


if __name__ == "__main__":

    utilisateur1 = Person("Michel", "Michel")
    utilisateur1.saluer()
    etudiant1 = Student("Steve", "Caron", "Data")
    etudiant1.setAge(15)
    etudiant1.saluer()
    etudiant1.GoToClasses()
    etudiant1.displayAge()
    prof1 = Teacher("Adrien", "Vossough", "POO")
    prof1.setAge(40)
    prof1.saluer()
    prof1.Explain()
