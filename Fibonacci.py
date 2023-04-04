"""
Ecrire l'algorithme de la suite de fibonacci:

C'est une suite définie par Un = Un-1 + Un-2

Si vous trouvez ça trop facile, passez par une fonction récursive
( c'est à dire fonction qui s'appelle elle meme)
"""
def fibonacci(n):
    if n == 0: return 0
    elif n == 1: return 1 
    else: return fibonacci(n-1) + fibonacci(n-2) #appel récursif
for i in range(0, 20): #affiche les 20 premiers termes
    print(fibonacci(i))

