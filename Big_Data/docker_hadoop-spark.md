# Docker Hadoop

commande a rentrer dans le terminal pour se connecter à une image contenant hadoop, spark etc:

```bash
docker pull liliasfaxi/spark-hadoop:hv-2.7.2
```

commande pour créer un réseau:

```bash
docker network create --driver=bridge hadoopnet
```

commande pour créer un container et lancer l'image d'une machine hadoop:

```bash
docker run -itd --net=hadoopnet -p 60070:60070 -p 8088:8088 -p 7077:7077 -p 16010:16010 --name hadoop-master --hostname hadoop-master liliasfaxi/spark-hadoop:hv-2.7.2
```

la commande ci dessus permet de créer un container avec un nom et un hostname, et de le connecter au réseau hadoopnet. On spécifie les ports à ouvrir et on spécifie l'image à utiliser.

commande pour créer une deuxième machine (1er worker):

```bash
docker run -itd --net=hadoopnet -p 8040:8042 --name hadoop-slave1 --hostname hadoop-slave1 liliasfaxi/spark-hadoop:hv-2.7.2
#ici on choisi deux ports différents car si on utilise le même port (expemple 8040:8040), la machine redirigera vers la même machine
```

commande pour créer une troisième machine (2eme worker):

```bash
docker run -itd --net=hadoopnet -p 8041:8042 --name hadoop-slave2 --hostname hadoop-slave2 liliasfaxi/spark-hadoop:hv-2.7.2
```

commande pour se connecter à la machine master et ouvrir un terminal bash dessus:

```bash
docker exec -it hadoop-master bash
```

commande pour démarrer hadoop dans la machine:

```bash
./start-hadoop.sh
```

commande hadoop pour crée un dossier dans le hdfs:

```bash
hadoop fs -mkdir -p input
```

commandes hdfs:

```bash
hadoop fs -ls cible # affiche le contenu du dossier cible
hadoop fs -put /chemin/jusqu'à/cible # envoie le fichier dans le hdfs
hadoop fs -get /chemin/jusqu'à/cible # récupère le fichier dans le hdfs
hadoop fs -cat mon fichier | head # affiche les 10 premières lignes
hadoop fs -tail mon fichier # affiche les 10 dernières lignes
hadoop fs -mv old_name.txt new_name.txt # renomme le fichier
hadoop fs -mkdir mon_dossier # crée un dossier
créer un fichier texte dans le hdfs: hadoop fs -put exemple.txt input
hadoop fs -rm mon_fichier # supprime le fichier
```

commande pour copier le fichier WordCount.jar dans le hdfs hadoop-master (à noter dans un autre terminal de notre ordinateur, pas celui de la machine docker hadoop-master):

```bash
docker cp .\WordCount.jar hadoop-master:/root/WordCount.jar
```

créer un fichier texte dans le hdfs:

```bash
hadoop fs -put purchases.txt input
```

déplacer le fichier .jar dans le dossier input (et le placer dans un dossier output qu'on crée en même temps):

```bash
hadoop jar WordCount.jar WordCount input output # WordCount est le nom de la classe java
```

pour ouvrir spark:

```bash
spark-shell
```

Pour lire un fichier dans spark:

```bash
val lines = sc.textFile("input/purchases.txt")
```

Commandes SCALA:

```bash
val lines = sc.textFile("input/purchases.txt") # lire un fichier
val words = lines.flatMap(line => line.split("\\s+")) # séparer les mots
val counts = words.map(word => (word.toLowerCase(),1)).reduceByKey(_+_) # compter les mots
counts.saveAsTextFile("output/result") # sauvegarder le résultat dans result
```
