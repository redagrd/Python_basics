# Codage Modulaire:

Toujours écrire une documentation pour les fonctions, classes et méthodes.
Lorsqu'on créer des fonctions, on les sépare dans des fichiers différents selon leur rôle.
Il s'agit du concept de single responsability, où chaque fichier ne fait qu'une seule chose.
Dans ce cas, il devient nécessaire de documenter les fichiers.
A noter que lorsqu'on importe un fichier d'appel, il est exécuté. Donc pour éviter ça, on n'appele pas la fonction dans le fichier ou elle est crée

## Documentation du fichier:

```python
""" fichier qui contient la logique de l'application
"""
```

Fonction main() :

```python
"""fichier qui contient la fonction main() qui est appelée au lancement du programme
"""
def main():
    """ Une méthode main() est une fonction qui est appelée au lancement du programme.
        Cette fonction montre que la fonction marche.
    """
    print("je fonctionne!")

if __name__ == __main__:
    print("coucou")
else:
    print("je suis importé !")
```

Fonction start() :

```python
"""fichier qui sert à démarrer mon projet
"""

from Tuto_fonctions import main as principal

if __name__ == __main__:
    principal()
```

Creation d'un fichier A contenant des fonctions:

```python
    """ mon super fichier A
    """

def maPartieA():
    """fonction demo d'un module
    """
    print("je suis dans le fichier A")
    maPartieB()
```

Creation d'un fichier B contenant des fonctions:

```python
    """ mon super fichier B
    """

def maPartieB():
    """fonction demo d'un module
    """
    print("je suis dans le fichier B")
    maPartieA()

```

Dans le fichier __init__.py, on peut importer les fonctions des autres fichiers:
Cela permet de centraliser les imports et de les rendre plus lisibles.

```python
from Tuto_fonctions import maPartieA
from Tuto_fonctions import maPartieB
```

Variables importantes à connaître :

```python
__name__ # contient le nom du fichier
__main__ # contient le nom du fichier principal
__init__.py # fichier qui permet de centraliser les imports
```

librairie a connaitre :

```python
pip install python-dotenv # permet de créer un fichier .env pour stocker les variables d'environnement de manière sécurisée
```