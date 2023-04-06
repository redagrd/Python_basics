from Rectangle import Rectangle

try :
    longueur = input("entrez la longueur du rectangle: ")
    largeur = int(input("entrez la largeur du rectangle: "))
    rect = Rectangle(longueur, largeur)
    rect.area()
except TypeError as error:
    print(error)

    
