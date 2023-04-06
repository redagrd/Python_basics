"""
FizzBuzz !

But de l'exercice :

Afficher en console les nombres de 1 à 35 (un par ligne) en remplaçant les
multiples de 3 par "Fizz!" et les multiples de 5 par "Buzz!". Les
multiples de 3 et 5 seront remplacés par "FizzBuzz!".

"""


for nb in range (1, 36) :
    if nb %3==0 and nb %5==0:
        print("FizzBuzz")
    elif nb %5 == 0:
        print("Buzz")
    elif nb %3 == 0:
        print("Fizz")
    else:
        print(nb)
