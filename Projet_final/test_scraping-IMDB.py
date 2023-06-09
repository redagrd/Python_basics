import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialiser le pilote WebDriver
driver = webdriver.Chrome()

# Accéder à la page de Rotten Tomatoes des commentaires d'un film
film_url = "https://www.imdb.com/title/tt24268454/reviews/?ref_=ttrt_sa_3"
driver.get(film_url)

# Attendre que les commentaires se chargent
WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "review-container")))

# Liste pour stocker les données
donnees_commentaires = []

# Fonction pour cliquer sur le bouton "Voir plus" pour étendre le commentaire complet
def cliquer_voir_plus(element):
    try:
        voir_plus = element.find_element(By.CLASS_NAME, "ipl-expander")
        if voir_plus.is_displayed():
            voir_plus.click()
    except:
        pass

# Parcourir les commentaires et extraire les données
while True:
    commentaires = driver.find_elements(By.CLASS_NAME, "review-container")

    for commentaire in commentaires:
        cliquer_voir_plus(commentaire)
        utilisateur = commentaire.find_element(By.CLASS_NAME, "display-name-link").text
        texte_commentaire = commentaire.find_element(By.CLASS_NAME, "text.show-more__control").text
        wait = WebDriverWait(driver, 10)
        user_elements = commentaire.find_elements(By.CLASS_NAME, "display-name-link")
        user_elements2 = user_elements.find_element(By.TAG_NAME, "a")
        if user_elements2:
            user_url = user_elements2[0].get_attribute('href')
    # Utilisez user_url comme vous le souhaitez
        else:
            print("Aucun élément avec la classe 'display-name-link' n'a été trouvé.")


        review_date = commentaire.find_element(By.CLASS_NAME, "review-date").text.replace('\n','')
        try:
            review_score = commentaire.find_element(By.CLASS_NAME, "rating-other-user-rating").text.replace('\n','')
        except:
            review_score = "Pas de note"

#        note_utilisateur = commentaire.find_element(By.CLASS_NAME, "rating-other-user-rating").text    
        # Stocker les données dans un dictionnaire
        donnees = {
            'Utilisateur': utilisateur,
            'Commentaire': texte_commentaire,
            'url_utilisateur': user_url,
            'Date': review_date,
            'Note': review_score
        }

        # Ajouter le dictionnaire à la liste
        donnees_commentaires.append(donnees)

    # Cliquer sur le bouton "Load More" pour passer à la page suivante
    load_button = driver.find_element(By.CLASS_NAME, "ipl-load-more__button")
    if load_button.is_displayed():
        cliquer_voir_plus(load_button)
        load_button.click()
        time.sleep(1)  # Attendre un court instant pour que la page se charge complètement
    else:
        break

# Chemin du fichier CSV de destination
chemin_fichier_csv = 'test_commentaires_IMDB.csv'

# Écriture des données dans le fichier CSV
with open(chemin_fichier_csv, mode='w', newline='', encoding='utf-8') as fichier_csv:
    fieldnames = ['Utilisateur', 'Commentaire', 'url_utilisateur', 'Date', 'Note']
    writer = csv.DictWriter(fichier_csv, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(donnees_commentaires)

print("Les données des commentaires de IMDB ont été stockées dans le fichier CSV.")

# Fermer le navigateur
driver.quit()