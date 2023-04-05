"""

Ecrire l'algorithme qui permet de vérifier
si un triangle est rectangle

Rappel un triangle est rectangle 
si il respecte le triplet pythagoricien a²+b²=c²


"""
arr = []

# Tant que l'utilisateur n'a pas rentrer 3 chiffres il recommence
while len(arr) != 3:
    numbers = input("Entrez les 3 longueurs (séparée d'un espace) :")
    arr = numbers.split()  # split est une méthode qui s'applique sur des chaines de caractères pour les transformer en tableau de "mots"
    # "15 2 8" devient [ "15" , "2" , "8" ]
    numbers.strip()
    arr = [int(i) for i in arr]  # on transforme les chaines de caractères en int


# On vérifie le triplet pythagoricien
if arr[0] ** 2 + arr[1] ** 2 == arr[2] ** 2:
    print("Le triangle est rectangle")
else:
    print("le triangle n'est pas rectangle")