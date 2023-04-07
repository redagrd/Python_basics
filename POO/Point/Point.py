"""
Créez une classe appelée « Point ». Cette classe doit avoir 2 entiers (x, y) en tant que membres privés. 
Le constructeur doit définir les valeurs de x et y via des paramètres. La classe doit avoir une méthode 
publique appelée « distance ». Cela prend un seul paramètre(Point) et renvoie la distance entre les 2 
points
"""

class Point:

    def __init__ (self, x, y):
        self.x = x
        self.y = y

    def Distance (self, Point):
        return print((self.__x - Point.__x)**2 + (self.__y - Point.__y)**2)
    
    @property
    def x(self):
        return self.__x
    
    @property
    def y(self):
        return
    
    @x.setter
    def x(self, a):
        if type(a) == int or type(a) == float :
            self.__x = a
        else:
            raise TypeError("Il faut un nombre")
        
    @y.setter
    def y(self, b):
        if type(b) == int or type(b) == float :
            self.__y = b
        else:
            raise TypeError("Il faut un nombre")
