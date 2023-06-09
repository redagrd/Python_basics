import requests
from bs4 import BeautifulSoup
from scrapy import Selector
from selenium import webdriver
import time
import pandas as pd
import csv
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# API TMDB
api_key = '5849fbb34bea488bb2d73d4d6638ff36'

def get_the_most_popular_movies_id(api_key):
    # Cette fonction retourne la liste des identifiants des films les plus populaires de l'API TMDB
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



# Obtenir les identifiants des films populaires

movies_ids = get_the_most_popular_movies_id(api_key)

id = movies_ids[0]

url = f'https://api.themoviedb.org/3/movie/{id}'
params = {'api_key': api_key}
response = requests.get(url, params=params)
data = response.json()
imdb_id = data['imdb_id']

# Configurer Selenium pour le scraping
driver = webdriver.Chrome()  # Remplacez '/path/to/chromedriver' par le chemin vers votre chromedriver
driver.implicitly_wait(10)

# Fonction pour cliquer sur le bouton "Voir plus" pour étendre le commentaire complet
def cliquer_voir_plus(element):
    try:
        voir_plus = element.find_element(By.CLASS_NAME, "ipl-expander")
        if voir_plus.is_displayed():
            voir_plus.click()
            time.sleep(1)  # Attendre un court instant pour que le texte étendu se charge
    except:
        pass

reviews = []
# Récupérer les reviews des films populaires sur IMDb
for movie_id in movies_ids:
    url = f'https://www.imdb.com/title/{imdb_id}/reviews'
    driver.get(url)
    time.sleep(3)  # Attendre que la page se charge complètement (ajustez le délai si nécessaire)

    # Extraire les données des reviews avec Scrapy
    html = driver.page_source
    selector = Selector(text=html)
    reviews = selector.css('.review-container')

    # Traiter les données des reviews
    for review in reviews:
        review_text = review.css('.text.show-more__control::text').get()
        rating = review.css('.rating-other-user-rating span::text').get()

        # Stocker les données dans un dictionnaire
        review_dict = { 'review_text': review_text,
                        'rating': rating}
        
        # Ajouter le dictionnaire à la liste
        reviews.append(review_dict)
        
# Fermer le navigateur Selenium
driver.quit()
