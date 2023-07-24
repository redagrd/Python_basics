# mapReduce

```python

# import de defaultdict de la librairie collections
from collections import defaultdict

def wordCount(text):
    ```
    fonction qui sert à compter le nombre de mots dans un texte
    @param : du texte
    @return : dictionnaire [clé: mot, valeur: nombre d'occurence]
    ```
    counts = defaultdict(int)
    for word in text.split():
        counts[word.lower()] += 1
    return counts

```

 modification en mapReduce de ce programme simple

```python

def map(key, valeur):
    ```
    fonction qui permet de transformaer l'élément clé/valeur en liste d'élément (mot, occurence)
    ```
    intermediaire = []
    for word in valeur.split():
        intermediaire.append((word.lower(), 1))
    return intermediaire

def reduce(key, valeurs):
    ```
    fonction qui permet de fusionner les occurences de la liste des valeurs en une seule valeur
    ```
    valeur = 0
    for chaque_element in valeurs:
        valeur += chaque_element
    return (key, valeur)

```
