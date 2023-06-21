# import des librairies

from bs4 import BeautifulSoup
import requests
import csv
import re


def recupData(nb):
    """methode demo pour recuperer
    des données d'un site demo construit expres pour ça
    """
    url = f"https://www.barreaudenice.com/annuaire/avocats/?fwp_paged={nb}"
    
    response = requests.get(url)
    
    print(response)
    return response.content

def scrapBs(i):
    """
    This function scrapes data from a webpage using BeautifulSoup and writes it to a CSV file.
    
    :param i: The parameter "i" is likely a variable that represents the URL or webpage that is being
    scraped for data. It is passed as an argument to the "recupData" function, which retrieves the HTML
    content of the webpage
    """
    ma_page = recupData(i)
    soup = BeautifulSoup(ma_page, "html.parser")
    
    listAvocats = soup.find_all("div", class_="callout secondary annuaire-single")
    
    for avocat in listAvocats:
        # nom prenom
        nom = avocat.find("h3", class_="nom-prenom").text.strip()
        # adresse
        adresse_temp = avocat.find("span", class_="adresse").text.strip()
        adresse = re.sub(r"\s+", " " , adresse_temp)
        # email
        try:
            email = avocat.find("span", class_="email").text.strip()
        except AttributeError:
            email="Introuvable"
        # telehone
        try:
            tel = avocat.find("span", class_="telephone").text.strip()
        except AttributeError:
            tel="Introuvable"
        # spacialité
        try:
            specialite = avocat.find("span", class_="intitule-droit").text.strip()
        except AttributeError:
            specialite="Introuvable"
        
        with open('avocats_data.csv', 'a', newline='',encoding='utf-8') as file:
            writer = csv.writer(file, delimiter=';')
            row = [nom, adresse, email, tel, specialite]
            writer.writerow(row)
    
def createFile():   
    """
    This function creates a new CSV file named "avocats_data.csv" and writes headers for columns in the
    file.
    """
    with open('avocats_data.csv', 'w', newline='') as file :
        writer = csv.writer(file)
        headers = [ "Nom", "adresse", "email","telephone","spaecialite"]
        writer.writerow(headers)
          
def main():
    """
    The main function creates a file and scrapes data using the scrapBs function for a range of numbers
    from 1 to 50.
    """
    createFile()
    for i in range (1,51):
        scrapBs(i)      
        
if __name__ == '__main__':
    # recupData()
    main()