from Somme import Somme

try :

    somme = Somme(1,2) # on initialise avec 0
    somme.entre() # on entre les valeurs
    resultat = somme.Sum() # on calcule
    print("le résultat est : ", resultat)

except TypeError as error:
    print(error)