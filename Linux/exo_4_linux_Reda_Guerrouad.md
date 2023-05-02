# TP Gestion des droits

## Partie 1: Exploration des droits

1. Quelle commande permet de lister les fichiers ainsi que les droits affectés

```bash
    ls -l
```

2. Etude du résultat de la commande de la question 1.

```bash
user@debian10:~/Documents <Commande de la question 1.
total 8 
drwxr-xr-- 2 user user 4096 juil. 10 17:56 bidule 
-rwxrw---x 1 user profs  0 juil. 10 17:56 machin.sh 
-rwxr-x--- 1 bob profs  3 juil. 10 17:57 truc 
```

- L'utilisateur est : user@debian10

- Le répertoire courant est : Documents

- Le répertoire contient 1 dossiers : bidule, et 2 fichier : machin.sh et truc

- pour le fichier machin.sh, les droits sont : rwxrw---x, il est rattaché à l'utilisateur user et au groupe profs, le 0 indique que le fichier est vide, et le 10 juil. 17:56 indique la date de la dernière modification.

- pour bidule drwxr-xr-- correspond à la valeur Octale 754, pour machin.sh rwxrw---x correspond à la valeur Octale 761, et pour truc rwxr-x--- correspond à la valeur Octale 750.

- les droits expriment que les droits de lecture et d'écriture sont accordés à l'utilisateur, et uniquement les droits de lecture sont accordés aux groupes et aux autres, et il s'agit de cette ligne :

```bash
rw-r--r--
```	

## Partie 2: Manipulation des droits

```bash
mkdir droits
```	

### Utilisation de la forme symbolique

1. Créer un fichier s_proprio, en utilisant la forme symbolique, affecter les droits en lecture, écriture, et
exécution uniquement au propriétaire du fichier.

    ```bash
    touch s_proprio
    chmod u=rwx s_proprio
    ```

2. Créer un fichier s_commun, en utilisant la forme symbolique, affecter les droits en lecture, écriture, et
exécution au propriétaire et groupe.

    ```bash
    touch s_commun
    chmod ug=rwx s_commun
    ```

3. Créer un fichier s_partiel, en utilisant la forme symbolique, affecter les droits en lecture, écriture, et
exécution au propriétaire et la lecture au groupe.

    ```bash
    touch s_partiel
    chmod u=rwx,g=r s_partiel
    ```

4. Créer un fichier s_restreint, en utilisant la forme symbolique, affecter les droits en lecture, écriture, et
exécution au propriétaire et la lecture au groupe et aux autres.

    ```bash
    touch s_restreint
    chmod u=rwx,g=r,o=r s_restreint
    ```

### Utilisation de la forme numérique

1. Créer un fichier n_proprio, en utilisant la forme numérique, affecter les droits en lecture, écriture, et exécution uniquement au propriétaire du fichier.

    ```bash
    touch n_proprio
    chmod 700 n_proprio
    ```

2. Créer un fichier n_commun, en utilisant la forme numérique, affecter les droits en lecture, écriture, et exécution au propriétaire et groupe.

    ```bash
    touch n_commun
    chmod 770 n_commun
    ```

3. Créer un fichier n_partiel, en utilisant la forme numérique, affecter les droits en lecture, écriture, et exécution au propriétaire et la lecture au groupe.

    ```bash
    touch n_partiel
    chmod 740 n_partiel
    ```

4. Créer un fichier dn_restreint, en utilisant la forme numérique, affecter les droits en lecture, écriture, et exécution au propriétaire et la lecture au groupe et aux autres.

    ```bash
    touch n_restreint
    chmod 744 n_restreint
    ```

## PARTIE 3: Liens physiques et symboliques

1. Qu’est ce qu’une inode pour linux ?
une inode pour linux correspond à un numéro qui identifie un fichier ou un dossier.

2. Comment verifier les inodes ?
pour voir le numéro d'inode des fichiers on utilise la commande ls -i

3. Recherche sur les liens symboliques 
les liens symbolique sont des raccourcis vers un fichier ou un dossier, ils sont représentés par un numéro d'inode différent de celui du fichier ou du dossier car il ne s'agit pas d'une copie physique du fichier ou du dossier d'origine.

4. Recherche sur les liens physiques.
Les liens physiques sont des raccourcis vers un fichier ou un dossier, ils sont représentés par le même numéro d'inode que le fichier ou le dossier car il s'agit d'une copie physique du fichier ou du dossier d'origine.

5. Créez dans votre répertoire personnel droits un fichier de test nommé “original” et un lien physique sur ce fichier nommé “physique”.

```bash
touch original
ln original physique
```

6. Exécutez la commande ls –lhi original physique et comparez les N° d’inodes et les tailles des deux fichiers que remarquez-vous ?

On remarque que les deux fichiers ont le même numéro d'inode et la même taille.

7. Insérez une ligne dans original avec un éditeur de texte puis ouvrez avec cat les fichiers original et physique. Que constate-t-on après après l'édition du fichier original

```bash
nano original
cat original physique
```

On constate que la ligne ecrite dans le fichier orignale se retrouve dans le fichier physique

8. Supprimer le fichier original puis ouvrir le fichier physique, que remarquez-vous ?

```bash
rm -r original
nano physique
```

Le fichier physique est toujours présent et contient toujours la ligne écrite dans le fichier original

9. Supprimer le fichier physique

```bash
rm -r physique
```

10. Créer ensuite un autre nouveau fichier toujours nommé original et créer un lien symbolique sur ce fichier nommé symbolique.

```bash
ln -s original symbolique
```

11. Exécutez la commande ls –lhi original symbolique et comparez les N° d’inodes et les tailles des deux fichiers que remarquez-vous ?

Cela me renvoie les lignes suivantes :

```bash
261363 -rw-r--r-- 1 redagrd redagrd 0 21 avril 13:41 original
263393 lrwxrwxrwx 1 redagrd redagrd 8 21 avril 13:42 symbolique -> original
```
On remarque que les inodes sont différents, et que les tailles le sont également.

12. Insérez une ligne dans original avec un éditeur de texte puis ouvrez avec cat les fichiers original et symbolique. Que constate-t-on après après l'édition du fichier original

```bash
nano original
cat origninal symbolique
```

On constate que les lignes écrites dans original se retrouvenet également dans symbolique

13. Supprimer le fichier original puis ouvrir le fichier symbolique, que remarquez-vous ?

```bash
rm -r original
nano symbolique
```

On constate que le fichier symbolique a été supprimé en même temps que le fichier original
