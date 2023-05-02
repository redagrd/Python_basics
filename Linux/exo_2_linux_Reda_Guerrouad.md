# TP 2 Linux

## Partie 1

- ex 1 :

```bash
     apt update

```

- ex 2 :

```bash
    apt-get upgrade
```

- ex 3 :

```bash
    cat /etc/apt/sources.list
```

- ex 4 :

``` bash
    apt search main && apt search contrib && apt search non-free
```

## Partie 2

- ex 1 :

``` bash
    cd /home/redagrd/Documents
    mkdir Exercice_Archive
```

- ex 2 :

``` bash
    mkdir DossierA
    cd /home/redagrd/Documents/Exercice_Archive/DossierA
    touch f1_dossierA && touch f2_dossierA && touch f3_dossierA
    #  autre méthode
    mkdir Dossier{A,B,C}

```

- ex 3 :

``` bash
    tar -czvf Archive.tar.gz Exercice_Archive
``` 

- ex 4 :

``` bash
    tar -xvf old_Archive.tar.gz
```

- ex 5 :

``` bash
    mv Archive.tar.gz old_Archive.tar.gz
```

- ex  :

``` bash
    tar -tf Exercice_Archive
```

## Partie 3

- ex 1 :

La commande apt search package_name permet de rechercher les paquets disponibles dans les dépôts de paquets Debian qui correspondent au terme de recherche spécifié par package_name.
Lorsqu'on exécute cette commande, apt recherche dans les index de paquets de tous les dépôts configurés sur le système Debian. Si des paquets correspondant au terme de recherche sont trouvés, ils seront affichés dans la sortie de la commande.

-ex 2 :

La commande apt show package_name permet d'afficher des informations détaillées sur un paquet spécifique installé ou disponible dans les dépôts de paquets Debian.

- ex 3 :

voici la description de tree après avoir utlisé la commande apt show tree :

Description: Affichage d’un arbre indenté de répertoires, en couleur

 Tree est une commande de listage récursive des répertoires pour produire un

 arbre des fichiers, indenté suivant la profondeur, coloré d’une manière

 similaire à dircolors si la variable d’environnement LS_COLORS est définie

 et la sortie produite sur un terminal en mode caractère.

- ex 4 :

apt-get install tree

- ex 5 :

On obtien cette sortie : bash: /usr/bin/tree: Aucun fichier ou dossier de ce type

- ex 6 :

Il faut utiliser la commande : apt-get clean

