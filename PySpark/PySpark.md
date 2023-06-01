# PySpark introduction

Moteur d'execution DAG utilisé par Spark = accelère le traitement des données parallèlisées

worker = slave
cluster manager = master (contient le driver, le contexte, la session, le scheduler et le job tracker)
ressource manager = surveille les ressources du cluster
session = ce qui permet de se connecter au cluster manager (possible de créer plusieurs sessions)
contexte = etabli ce qui est possible de faire avec Spark
driver = processus qui lance le contexte Spark (interface entre le code et le cluster manager)
scheduler = planifie les tâches sur les workers (job)
job tracker = repère et identifie les différentes tâches des workers