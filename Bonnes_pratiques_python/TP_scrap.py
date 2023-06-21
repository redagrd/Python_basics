# scraping sur https://www.barreaudenice.com/annuaire/avocats/?fwp_paged=

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

def recupData(numeroPage:int):
    """récupérer les données des pages
    """
    url = chargementEnv("AVOCAT") + str(numeroPage)
    response = get(url)
    response = response.content

    return response    

def scrapBs():
    """scraping sur les 50 premières pages de : https://www.barreaudenice.com/annuaire/avocats/?fwp_paged=
    """
    with open('save_data_lawyers.csv', 'w', newline='') as file :
            writer = csv.writer(file)
            headers = [ "Nom", "Adresse", "Telephone", "Email" ]
            writer.writerow(headers)
    for i in range(1, 51):
        mes_page = recupData(i)
        soup = BeautifulSoup(mes_page, 'html.parser')
        div = soup.find("div")
        avocats = div.find_all('div', class_ = 'callout secondary annuaire-single')
        for avocat in avocats:
            # nom
            try:
                nom = avocat.find(class_ = 'nom-prenom').text
                print("nom : ", nom)
            except:
                print("Introuvable")
            # adresse
            try: 
                adresse = avocat.find(class_ = 'adresse').text
                adresse = " ".join(adresse.split())
                print("adresse : ", adresse)

            except:
                print("Introuvable")
            # téléphone
            try:
                tel = avocat.find(class_ = 'telephone').text
                print("téléphone : ", tel)
            except:
                print("Introuvable")
            # email
            try:
                mail = avocat.find(class_ = 'email').text
                print("email : ", mail)
            except:
                print("Introuvable")
            
            with open('save_data_lawyers.csv', 'a', newline='', encoding = 'utf8') as file:
                writer = csv.writer(file, delimiter = ',')
                headers = [ nom, adresse, tel, mail ]
                writer.writerow(headers)

if __name__ == "__main__":
    #recupData()
    scrapBs()    
