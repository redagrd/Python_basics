import csv
import requests
import pandas as pd

# Remplacez "YOUR_ACCESS_TOKEN" par votre propre jeton d'accès personnel
access_token = "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"

# URL de l'API GitHub pour les dépôts les plus tendance
url = "https://api.github.com/search/repositories?q=stars:%3E1&sort=stars&order=desc"

# En-tête de requête avec le jeton d'accès
headers = {
    "Authorization": f"Token {access_token}",
    "Accept": "application/vnd.github.v3+json"
}

données = []
# Envoi de la requête GET à l'API GitHub
response = requests.get(url, headers=headers)

# Vérification du code d'état de la réponse

if response.status_code == 200:
    # Récupération des données JSON de la réponse
    data = response.json()

    # Parcours des dépôts
    for repo in data["items"]:
    # Récupération des informations du dépôt
        name = repo["name"]
        description = repo["description"]
        stars = repo["stargazers_count"]
        forks = repo["forks_count"]

        # stockage des informations du dépôt
        donnees2 = {
        'name': name,
        'description': description,
        'stars': stars,
        'forks': forks
    }
        données.append(donnees2)
    else:
        print("Une erreur s'est produite lors de la requête.")

chemin_fichier_csv = 'test_github.csv'

# Écriture des données dans le fichier CSV
with open(chemin_fichier_csv, mode='w', newline='', encoding='utf-8') as fichier_csv:
    fieldnames = ['name', 'description', 'stars', 'forks']
    writer = csv.DictWriter(fichier_csv, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(données)

print("Les données ont été stockées dans le fichier CSV.")
