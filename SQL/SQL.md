# Exercices SQL - Bases

Insertion de données dans la table `eleves` :

```sql
INSERT INTO eleves
VALUES (1, 'DAVID', 'BOWIE', '1947-01-08', 6);
```
Sélection de toutes les données de la table `eleves` :

```sql
SELECT *
FROM eleves;
```

sélection des colonnes `nom` et `prenom` de la table `eleves` :

```sql
SELECT nom, prenom
FROM eleves;
```

Insertion du reste des données dans la table `eleves` :

```sql
INSERT INTO eleves (nom, prenom, date_Naissance, classe_id)
VALUES ('Elton', 'John', '1947-03-25', 6),
('Cartman', 'Éric', '1989-07-01', 7),
('Norton', 'Edward', '1959-08-18', 5),
('Nicks', 'Stevie', '1948-05-26', 4),
('Kilmister', 'Lemmy', '1945-12-24', 3);
```

On change le nom de la colonne `date_Naissance` en `date_naissance` :

```sql
ALTER TABLE eleves
CHANGE date_Naissance date_naissance DATE NOT NULL;
```

On met a jour le nom de David Bowie qui était inversé:

```sql
UPDATE eleves
SET nom = 'Bowie', prenom ='David'
WHERE nom LIKE 'David';
```

On tri les élèves en fonction de leur date de naissance de manière ascendante en affichant que les colonnes `nom`, `prenom` et `date_naissance`:

```sql
SELECT nom, prenom, date_naissance
FROM eleves
ORDER BY date_naissance ASC;
```

On met a jour le nom de Elton John qui était inversé:

```sql
UPDATE eleves
SET nom = 'John', prenom = 'Elton'
WHERE nom LIKE 'Elton';
```

Filtrer les élèves nés après 1945, dont le nom ne contient pas de 'a' ET pas de 'k', dont le prénom contient un 'n', et n'affiche que le nom, prénom et date de naissance :

```sql
SELECT nom, prenom, date_naissance
FROM eleves 
WHERE (date_naissance > '1945-12-31')
	AND (nom NOT LIKE '%a%' AND nom NOT LIKE '%k%')
    AND nom LIKE '%n%';
```

Afficher les élèves nés entre le 01/01/1945 et le 31/12/1947, n'afficher que le nom, prénom et date de naissance :

```sql
SELECT nom, prenom, date_naissance
FROM eleves
WHERE date_naissance BETWEEN '1945-01-01' AND '1947-12-31';
```

N'afficher QUE les élèves de 6eme et 5eme, n'afficher que le nom, prénom et la classe :

```sql
SELECT nom, prenom, classe_id
FROM eleves
WHERE classe_id IN ('5', '6');
```

Après avoir crée une nouvelle table `classes` avec les colonnes `id` et `niveau`, on insère les données suivantes :

```sql
INSERT INTO classes (id, niveau)
VALUES (7, 'segpa'),
(6, 'Sixième'),
(5, 'Cinquième'),
(4, 'Quatrième'),
(3,'Troisième');
```