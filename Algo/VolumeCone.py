"""

Ecrire l'algorithme qui permet de calculer
le volume d'un cone

Rappel le volume d'un cone 
c'est (pi*rayon²*hauteur)/3


"""
def volume_cone(rayon, hauteur):
    return (3.14 * rayon ** 2 * hauteur) / 3

print(volume_cone(6, 12))