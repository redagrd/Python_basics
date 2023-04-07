from Student import Student

try :
    etudiant = Student("nom", 0, 0)
    etudiant.Entre()
    etudiant.Show()

except TypeError as error:
    print(error)