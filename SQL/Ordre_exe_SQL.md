# Commande

SQL interprète les requêtes dans l'ordre suivant :
	
FROM: SQL va d'abord chercher les tables à partir desquelles les données seront récupérées. Cela peut impliquer l'ouverture de fichiers de données ou l'accès à des données stockées en mémoire.
	
WHERE: une fois que les tables sont sélectionnées, SQL applique les conditions de filtre spécifiées dans la clause WHERE pour sélectionner les enregistrements qui répondent aux exigences de la requête. Cela peut impliquer l'utilisation d'opérateurs logiques tels que AND et OR, ainsi que des opérateurs de comparaison tels que =, <, >, etc.
	
GROUP BY: si la requête inclut une clause GROUP BY, SQL regroupe les enregistrements en fonction des valeurs communes dans les colonnes spécifiées.
	
HAVING: si la requête inclut une clause HAVING, SQL filtre les groupes résultants en fonction des conditions spécifiées pour sélectionner uniquement les groupes qui répondent à certaines exigences.
	
SELECT: une fois que les enregistrements sont sélectionnés et regroupés (si nécessaire), SQL récupère les colonnes de données spécifiées dans la clause SELECT.
	
ORDER BY: si la requête inclut une clause ORDER BY, SQL trie les résultats en fonction des valeurs des colonnes spécifiées.
	
LIMIT: si la requête inclut une clause LIMIT, SQL limite le nombre d'enregistrements renvoyés dans les résultats.


Il est important de noter que toutes les clauses ne sont pas nécessaires pour chaque requête SQL et que l'ordre exact peut varier en fonction de la requête spécifique. Cependant, cet ordre général est généralement suivi pour garantir que les résultats de la requête sont cohérents et précis.

Sous requête:

- quand appelé après le SELECT = renvoit 1 résultat (une cellule)
- quand appelé aprrès le FROM = renvoit une table
- quand appelé a^rès une condition, renvoie une colonne