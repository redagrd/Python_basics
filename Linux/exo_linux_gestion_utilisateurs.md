# TP Linux 3 : Gestion des utilisateurs

## Partie 1 : Manipulation user et group

- 1 Création de 3 groupes : formateur, etudiant, administration

``` bash
 addgroup formateur etudiant administration
 cat /etc/group
```

- 2 Création de 5 utilisateurs avec création de leurs répertoire home : u1, u2, u3, u4, u5

``` bash
 sudo adduser -m u1 u2 u3 u4 u5
 cat /etc/passwd
```

- 3 Ajouter les utilisateurs u1, u2 au groupe formateur

``` bash
 sudo usermod -aG u1 u2 u3 formateur
```

- 4 Ajouter les utilisateurs u3 au groupe etudiant

``` bash
 sudo usermod -aG u1 u2 u3 etudiant
 # -aG = ajoute au groupe
```

- 5 Ajouter les utilisateurs u4, u5 au groupe administration

``` bash
 sudo usermod -aG u1 u2 u3 administration
```

- 6 Utiliser la commande getent pour verifier l'ajout dans les différents groupes.

``` bash
 getent group formateur etudiant administration
```

- 7 Verifier à l'aide du fichier /etc/passwd le terminal utilisé par les nouveaux utilisateurs ?

``` bash
 cat /etc/passwd
```

- 8 Modifier le terminal utilisé par les utilisateurs créés par /bin/bash

Pour moi le terminal utilisé par les utilisateurs créés est déjà /bin/bash, mais la commande qui devrait être utilisée est :

``` bash
    usermod -s /bin/bash u1 u2 u3 u4 u5
    # Autre méthode : chsh -s /bin/bash u1 u2 u3 u4 u5
    # -s = shell
```

- 9 Acceder a la console de l'utilisateur u2, verifier l'utilisateur connecté et créer un fichier nommé test dans le repertoire /home/u2

``` bash
 su u2
 whoami
 touch test
```

- 10 Verifier le groupe propriétaire du fichier et modifier celui-ci par le groupe root

``` bash
ls -l
sudo chgrp root test
ls -l
```

- 11 Modifier le groupe et l'utilisateur propriétaire par root:root avec la commande chown sur le fichier test

``` bash
sudo chown root:root test
```

- 12 Mettre l'utilisateur u1 en mode sudo

``` bash
sudo usermod -aG sudo u1
```

- 13 Supprimer les utilisateurs créés

``` bash
 sudo deluser u1 u2 u3 u4 u5
```

- 14 Supprimer les groupes créés

``` bash
 sudo delgroup formateur etudiant administration
```

## Partie 2 : Filtrer le contenu des fichiers

- 1 Filtrer le fichier /etc/passwd pour obtenir uniquement l’utilisateur root et l’utilisateur principal(Premier utilisateur créé)et rediriger la sortie dans un fichier nommé passwd_dep.

le > = redirige une sortie d'une commande vers un fichier, mais écrase le contenu du fichier existant
le >> = redirige une sortie d'une commande vers un fichier, mais l'ajoute au fichier sans supprimer l'ancien
les deux peuvent permettre de créer des fichiers

``` bash
sudo grep -E "1000" /etc/passwd >> passwd_dep
sudo grep -E "root" /etc/passwd >> passwd_dep
# Autre méthode : sudo grep "root\|1000" /etc/passwd > passwd_dep
# -E = expression régulière
```

- 2 Trouver le nombre de lignes que contient le fichier /etc/passwd et mettre la réponse à la fin du fichier fraîchement créé

wc = compte le nb de lignes, mots et caractères
wc -l = compte le nb de lignes

``` bash
sudo wc -l /etc/passwd >> passwd_dep
```

- 3 Filtrer le fichier /etc/shadow pour obtenir uniquement l’utilisateur root et l’utilisateur principal et rediriger la sortie dans un fichier nommé shadow_dep.

``` bash
sudo grep -E "redagrd" /etc/shadow >> shadow_dep
sudo grep -E "root" /etc/shadow >> shadow_dep
```

- 4 Trouver le nombre de lignes que contient le fichier /etc/shadow et mettre la réponse à la fin du fichier fraîchement créé.

``` bash
sudo wc -l /etc/shadow >> shadow_dep
```

- 5 Filtrer le fichier /etc/group pour obtenir uniquement l’utilisateur root et l’utilisateur principal et rediriger la sortie dans un fichier nommé group_dep.

``` bash
sudo grep -E "1000" /etc/group >> group_dep
sudo grep -E "root" /etc/group >> group_dep
```

- 6 Trouver le nombre de lignes que contient le fichier /etc/group et mettre la réponse à la fin du fichier fraîchement créé.

``` bash
sudo wc -l /etc/group >> group_dep
```
