
# import requests
# import pandas as pd

# # Votre clé API TMDB
# api_key = '5849fbb34bea488bb2d73d4d6638ff36'

# # Liste de films à récupérer les critiques et les commentaires
# films = []

# # Créer un dictionnaire pour stocker les critiques et les commentaires de chaque film
# reviews = {}

# # Envoyer une requête GET pour chaque film dans la liste
# for film in films:
#     # Obtenir l'ID du film en envoyant une requête de recherche à l'API TMDB
#     url = 'https://api.themoviedb.org/3/search/movie'
#     params = {'api_key': api_key, 'query': film}
#     response = requests.get(url, params=params)
#     data = response.json()
#     film_id = data['results'][0]['id']

#     # Envoyer une requête GET pour les critiques et les commentaires du film
#     url = f'https://api.themoviedb.org/3/movie/{film_id}/reviews'
#     params = {'api_key': api_key}
#     response = requests.get(url, params=params)
#     data = response.json()
#     reviews[film] = data['results']

# # Stocker les critiques et les commentaires dans un tableau de données pandas
# reviews_df = pd.DataFrame({'film': [], 'author': [], 'content': []})
# for film in reviews:
#     for review in reviews[film]:
#         reviews_df = reviews_df._append({'film': film, 'author': review['author'], 'content': review['content']}, ignore_index=True)

# # Écrire le tableau de données pandas dans un fichier CSV
# reviews_df.to_csv('critiques_films.csv', index=False)


# import requests
# import pandas as pd

# # Votre clé API TMDB
# api_key = '5849fbb34bea488bb2d73d4d6638ff36'

# # Nombre total de pages de résultats
# total_pages = 1

# # Récupérer le nombre total de pages de résultats
# url = 'https://api.themoviedb.org/3/movie/popular'
# params = {'api_key': api_key, 'page': 1}
# response = requests.get(url, params=params)
# data = response.json()
# total_pages = data['total_pages']

# # Créer un dictionnaire pour stocker les critiques et les commentaires de chaque film
# reviews = {}

# # Envoyer une requête GET pour chaque page de résultats
# for page in range(1, total_pages+1):
#     url = 'https://api.themoviedb.org/3/movie/popular'
#     params = {'api_key': api_key, 'page': page}
#     response = requests.get(url, params=params)
#     data = response.json()
#     for film in data['results']:
#         # Envoyer une requête GET pour les critiques et les commentaires du film
#         url = f'https://api.themoviedb.org/3/movie/{film["id"]}/reviews'
#         params = {'api_key': api_key}
#         response = requests.get(url, params=params)
#         data = response.json()
#         reviews[film['id']] = data['results']

# # Stocker les critiques et les commentaires dans un tableau de données pandas
# reviews_df = pd.DataFrame({'film_id': [], 'author': [], 'content': []})
# for film_id in reviews:
#     for review in reviews[film_id]:
#         reviews_df = reviews_df.append({'film_id': film_id, 'author': review['author'], 'content': review['content']}, ignore_index=True)

# # Écrire le tableau de données pandas dans un fichier CSV
# reviews_df.to_csv('critiques_films.csv', index=False)
