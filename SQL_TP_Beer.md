# TP 1

## Exercice 1

```sql
SELECT ventes.NUMERO_TICKET
FROM ventes
WHERE ventes.ID_ARTICLE = 500;
```

## Exercice 2

```sql
SELECT ANNEE, NUMERO_TICKET, DATE_VENTE
FROM ticket
WHERE ticket.DATE_VENTE = '2014-01-15';
```

## Exercice 3

```sql
SELECT ANNEE, NUMERO_TICKET, DATE_VENTE
FROM ticket
WHERE ticket.DATE_VENTE BETWEEN '2014-01-15 00:00:00' AND  '2014-01-17 00:00:00';
```

## Exercice 4

```sql
SELECT NUMERO_TICKET, NOM_ARTICLE, QUANTITE
FROM ventes
INNER JOIN article
	ON article.ID_ARTICLE = ventes.ID_ARTICLE
WHERE ventes.QUANTITE >= 50;
```

## Exercice 5

```sql
SELECT ANNEE, NUMERO_TICKET, DATE_VENTE
FROM ticket
WHERE ticket.DATE_VENTE BETWEEN '2014-03-1 00:00:00' AND  '2014-03-31 00:00:00';

#Autre solution
SELECT NUMERO_TICKET, DATE_VENTE
FROM ticket
WHERE ANNEE = 2014 AND MONTH(DATE_VENTE) LIKE 3;
```

## Exercice 6

```sql
SELECT ANNEE, NUMERO_TICKET, DATE_VENTE
FROM ticket
WHERE ticket.DATE_VENTE BETWEEN '2014-03-1 00:00:00' AND  '2014-04-30 00:00:00';

#Autre solution
SELECT NUMERO_TICKET, DATE_VENTE
FROM ticket
WHERE ANNEE = 2014 AND MONTH(DATE_VENTE) BETWEEN 3 AND 4;
```

## Exercice 7

```sql
SELECT ANNEE, NUMERO_TICKET, DATE_VENTE
FROM ticket
WHERE ticket.DATE_VENTE LIKE '%2014-03%' OR ticket.DATE_VENTE LIKE '%2014-06%';

#Autre solution
SELECT NUMERO_TICKET, DATE_VENTE
FROM ticket
WHERE ANNEE = 2014 AND MONTH(DATE_VENTE) IN (3, 6);
```

## Exercice 8

```sql
SELECT couleur.NOM_COULEUR, article.ID_ARTICLE, article.NOM_ARTICLE
FROM article
INNER JOIN couleur
	ON couleur.ID_Couleur = article.ID_Couleur
ORDER BY couleur.ID_Couleur;
```

## Exercice 9

```sql
SELECT article.ID_ARTICLE, article.NOM_ARTICLE
FROM article
WHERE article.ID_Couleur IS NULL;
```

## Exercice 10

```sql
SELECT ventes.NUMERO_TICKET, SUM(ventes.QUANTITE)
FROM ventes
GROUP BY ventes.NUMERO_TICKET;
```

## Exercice 11

```sql
SELECT ventes.NUMERO_TICKET, SUM(ventes.QUANTITE)
FROM ventes
GROUP BY ventes.NUMERO_TICKET
HAVING SUM(ventes.QUANTITE) > 500
ORDER BY SUM(ventes.QUANTITE) ASC;
```

## Exercice 12

```sql
SELECT ventes.NUMERO_TICKET, SUM(ventes.QUANTITE)
FROM ventes
WHERE ventes.QUANTITE < 50
GROUP BY ventes.NUMERO_TICKET
HAVING SUM(ventes.QUANTITE) > 500
ORDER BY SUM(ventes.QUANTITE) ASC;
```

## Exercice 13

```sql
SELECT article.ID_ARTICLE, type.NOM_TYPE, article.NOM_ARTICLE, article.VOLUME, article.TITRAGE
FROM article
INNER JOIN type
	ON type.ID_TYPE = article.ID_TYPE
WHERE article.ID_TYPE LIKE 13;
```

## Exercice 14

```sql
SELECT marque.NOM_MARQUE
FROM marque
INNER JOIN pays
	ON marque.ID_PAYS = pays.ID_PAYS
WHERE pays.ID_CONTINENT LIKE 1;

# Autre solution

SELECT ID_MARQUE, NOM_MARQUE, NOM_PAYS, NOM_CONTINENT
FROM marque
JOIN pays
	ON marque.ID_PAYS = pays.ID_PAYS
JOIN continent
	ON pays.ID_CONTINENT = continent.ID_CONTINENT
WHERE continent.NOM_CONTINENT = 'Amérique';
```

## Exercice 15

```sql
SELECT article.NOM_ARTICLE
FROM article
INNER JOIN marque
	ON marque.ID_MARQUE = article.ID_MARQUE
INNER JOIN pays
	ON pays.ID_PAYS = marque.ID_PAYS
WHERE pays.ID_CONTINENT LIKE 1;

# Autre solution

SELECT ID_ARTICLE, NOM_ARTICLE, NOM_MARQUE, NOM_PAYS, NOM_CONTINENT
FROM article
JOIN marque
	ON marque.ID_MARQUE = article.ID_MARQUE
JOIN pays
	ON pays.ID_PAYS = marque.ID_PAYS
JOIN continent
	ON pays.ID_CONTINENT = continent.ID_CONTINENT
WHERE continent.NOM_CONTINENT = 'Afrique';
```

## Exercice 16

```sql
SELECT ventes.ANNEE, ventes.NUMERO_TICKET, SUM(ventes.QUANTITE * article.PRIX_ACHAT ) * 1.15 AS total
FROM ventes
INNER JOIN  article
	ON article.ID_ARTICLE = ventes.ID_ARTICLE
GROUP BY ventes.ANNEE, ventes.NUMERO_TICKET;

# Autre solution en incluant les tickets

SELECT ticket.ANNEE, ticket.NUMERO_TICKET, SUM(ventes.QUANTITE * article.PRIX_ACHAT ) * 1.15 AS PRIX_VENTE
FROM ticket
INNER JOIN  ventes
	USING(NUMERO_TICKET, ANNEE)
INNER JOIN  article
	ON article.ID_ARTICLE = ventes.ID_ARTICLE
GROUP BY ticket.ANNEE, ticket.NUMERO_TICKET;
```

## Exercice 17

```sql
SELECT ventes.ANNEE, ventes.NUMERO_TICKET, SUM(ventes.QUANTITE * article.PRIX_ACHAT ) * 1.15 AS total
FROM ventes
INNER JOIN  article
	ON article.ID_ARTICLE = ventes.ID_ARTICLE
GROUP BY ventes.ANNEE, ventes.NUMERO_TICKET;
```

## Exercice 18

```sql
SELECT ventes.ID_ARTICLE, ventes.ANNEE, SUM(ventes.QUANTITE) 
FROM ventes
INNER JOIN article
	ON article.ID_ARTICLE = ventes.ID_ARTICLE
WHERE ventes.ANNEE LIKE '2016'
GROUP BY ventes.ID_ARTICLE, ventes.ANNEE, article.NOM_ARTICLE
ORDER BY ventes.ID_ARTICLE;
```

## Exercice 19

```sql
SELECT ventes.ID_ARTICLE, ventes.ANNEE, SUM(ventes.QUANTITE) 
FROM ventes
INNER JOIN article
	ON article.ID_ARTICLE = ventes.ID_ARTICLE
WHERE ventes.ANNEE IN ('2014', '2015', '2016')
GROUP BY ventes.ID_ARTICLE, ventes.ANNEE, article.NOM_ARTICLE
ORDER BY ventes.ID_ARTICLE;
```

## Exercice 20

```sql
SELECT article.ID_ARTICLE, article.NOM_ARTICLE
FROM article
WHERE (
SELECT SUM(ventes.QUANTITE) 
FROM ventes 
WHERE ID_ARTICLE = article.ID_ARTICLE AND ANNEE = 2014) IS NULL;
```

## Exercice 21

```sql
SELECT pays.NOM_PAYS
FROM pays
INNER JOIN marque
ON marque.ID_PAYS = pays.ID_PAYS
INNER JOIN article
ON article.ID_MARQUE = marque.ID_MARQUE
INNER JOIN type
ON type.ID_TYPE = article.ID_TYPE
WHERE type.NOM_TYPE LIKE 'Trappiste'
GROUP BY NOM_PAYS;

# Autre solution en utilisant les sous-requêtes

SELECT pays.NOM_PAYS
FROM pays
WHERE pays.ID_PAYS IN (
SELECT marque.ID_PAYS
FROM marque
WHERE marque.ID_MARQUE IN (
SELECT article.ID_MARQUE
FROM article
WHERE article.ID_TYPE IN (
SELECT type.ID_TYPE
FROM type
WHERE type.NOM_TYPE LIKE 'Trappiste')));

# Autre solution en utilisant les DISTINCT

SELECT DISTINCT pays.NOM_PAYS
FROM pays
INNER JOIN marque
ON marque.ID_PAYS = pays.ID_PAYS
INNER JOIN article
ON article.ID_MARQUE = marque.ID_MARQUE
INNER JOIN type
ON type.ID_TYPE = article.ID_TYPE
WHERE type.NOM_TYPE LIKE 'Trappiste';
```

## Exercice 22

```sql

SELECT DISTINCT ventes.NUMERO_TICKET, ventes.ANNEE
FROM ventes
WHERE ventes.ID_ARTICLE IN (
SELECT ventes.ID_ARTICLE
FROM ventes
WHERE ventes.NUMERO_TICKET LIKE '856' AND ventes.ANNEE LIKE '2014')
```

## Exercice 23

```sql

SELECT article.NOM_ARTICLE
FROM article
WHERE article.TITRAGE > (
SELECT MAX(article.TITRAGE)
FROM article
INNER JOIN type
ON type.ID_TYPE = article.ID_TYPE
WHERE type.NOM_TYPE LIKE 'Trappiste');
```

## Exercice 24

```sql
