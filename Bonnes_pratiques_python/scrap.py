# scraping sur book.toscrape.com

#imports
from dotenv import load_dotenv
import os
from requests import get
from bs4 import BeautifulSoup
import csv

def chargementEnv(VARENV:str):
    """
    Charge les variables d'environnement depuis le fichier .env
    """
    load_dotenv()
    return os.getenv(VARENV)

def recupData():
    """méthode demo pour récupérer les données d'une page web
    """
    bookscrap = chargementEnv("BOOKSCRAP")
    url = bookscrap + 'catalogue/page-1.html'
    response = get(url)
    return response.content

def scrapBs():
    ma_page = recupData()
    soup = BeautifulSoup(ma_page, 'html.parser')
    ol = soup.find('ol')
    articles = ol.find_all('article', class_ = 'product_pod')
    with open('save_data.csv', 'w', newline='') as file :
        writer = csv.writer(file)
        headers = [ "Titre", "Note", "Prix" ]
        writer.writerow(headers)
    for article in articles:
        # titre
        image = article.find('img')
        title = image.attrs['alt']
        print("titre : ", title)
        # notes
        star = article.find('p')
        star = star['class'][1]
        print("notes du livre : ", star)
        # prix
        price = article.find('p', class_ = 'price_color').text
        print("prix (en {}) du livre : {} "\
            .format(price[:1],price[1:]))
        
        with open('save_data.csv', 'a', newline='', encoding = 'utf8') as file:
            writer = csv.writer(file, delimiter = ',')
            headers = [ title, star, price[1:] ]
            writer.writerow(headers)
            
if __name__ == "__main__":
    #recupData()
    scrapBs()
