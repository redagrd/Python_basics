import requests
import pandas as pd

# API TMDB
api_key = '5849fbb34bea488bb2d73d4d6638ff36'

def get_the_most_popular_movies_id(api_key):
    """_summary_ : This function returns the list of the most popular movies id from the TMDB API

    Returns:
        list_of_popular_movies_id: List of the most popular movies id from the TMDB API
    """

    # Number of pages of results, there is 20 movies per page
    total_pages = 5
    list_of_popular_movies_id = []
    for page in range(1,total_pages+1):

        url = 'https://api.themoviedb.org/3/movie/popular'
        params = {'api_key': api_key, 'page': page}
        response = requests.get(url, params=params)
        data = response.json()
        total_pages = data['total_pages']
        #print(data.keys())
        for popular_film in data['results']:
            list_of_popular_movies_id.append(popular_film['id'])
        
    return list_of_popular_movies_id







movies_ids = get_the_most_popular_movies_id(api_key)


id = movies_ids[0]

url = f'https://api.themoviedb.org/3/movie/{id}'
params = {'api_key': api_key}
response = requests.get(url, params=params)
data = response.json()

# for key in data.keys():
#     print('|||',key,'|||')
#     print(data[key])
    
    
# Stocker les données dans un dictionnaire
data_to_save = {
    'id_movie': data['id'],
    'id_imdb': data['imdb_id'],
    'title': data['original_title'],
    'synopsis': data['overview'],
    'popularity': data['popularity'],
    'production_companies': data['production_companies'],
    'spoken_languages': data['spoken_languages'],
    'countries': data['production_countries'],
    'revenue': data['revenue'],
    'budget': data['budget'],
    'genres': data['genres'],
    'release_date': data['release_date'],
    'runtime': data['runtime'],
    'review_score': data['vote_average'],
}

print(data)
# films[film] = data['results']

# # Stocker les films  dans un tableau de données pandas
# reviews_df = pd.DataFrame({'film': [], 'author': [], 'content': []})
# for film in reviews:
#     for review in reviews[film]:
#         reviews_df = reviews_df._append({'film': film, 'author': review['author'], 'content': review['content']}, ignore_index=True)

# # Écrire le tableau de données pandas dans un fichier CSV
# reviews_df.to_csv('critiques_films.csv', index=False)

# j'ai fait ce code permettant de se connecter à l'api de tmdb et de récupérer les données des films populaires. J'ai remarqué qu'il était possible d'obtenir les identifiants imdb pour chaque films. j'aimerrais utiliser ces identifiants imdb obtenu via l'api tmdb pour récupérer les reviews des films populaire obtenu en allant scraper ces reviews via scrapy et selenium sur imdb.