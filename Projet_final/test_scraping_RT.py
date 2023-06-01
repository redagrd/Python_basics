import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

# Initialiser le pilote WebDriver
driver = webdriver.Chrome()

# Accéder à la page de Rotten Tomatoes des commentaires d'un film
options = Options()
options.add_argument('--ignore-certificate-errors')
film_url = "https://www.rottentomatoes.com/m/big_george_foreman_the_miraculous_story_of_the_once_and_future_heavyweight_champion_of_the_world/reviews?type=user"
driver.get(film_url)

# Attendre que les commentaires se chargent
WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "audience-review-row")))

# Récupérer les éléments des commentaires
commentaires = driver.find_elements(By.CLASS_NAME, "audience-review-row")

# Liste pour stocker les données
donnees_commentaires = []


# Parcourir les commentaires et extraire les données
for commentaire in commentaires:
            utilisateur = commentaire.find_element(By.CLASS_NAME, "audience-reviews__name-wrap").text
            texte_commentaire = commentaire.find_element(By.CLASS_NAME, "audience-reviews__review.js-review-text").text
            for note in commentaire:
                if commentaire.find_element(By.CLASS_NAME, "star-display__half").is_displayed() :
                    note = 0.5
                elif commentaire.find_element(By.CLASS_NAME, "star-display__filled").is_displayed():
                    note = 1
                elif commentaire.find_element(By.CLASS_NAME, "star-display__filled").is_displayed() and commentaire.find_element(By.CLASS_NAME, "star-display__half").is_displayed():
                    note = 1.5
                elif commentaire.find_element(By.CLASS_NAME, "star-display__filled").is_displayed() and commentaire.find_element(By.CLASS_NAME, "star-display__filled").is_displayed():
                    note = 2
                elif commentaire.find_element(By.CLASS_NAME, "star-display__filled").is_displayed() and commentaire.find_element(By.CLASS_NAME, "star-display__filled").is_displayed() and commentaire.find_element(By.CLASS_NAME, "star-display__half").is_displayed():
                    note = 2.5
                elif commentaire.find_element(By.CLASS_NAME, "star-display__filled").is_displayed() and commentaire.find_element(By.CLASS_NAME, "star-display__filled").is_displayed() and commentaire.find_element(By.CLASS_NAME, "star-display__filled").is_displayed():
                    note = 3
                elif commentaire.find_element(By.CLASS_NAME, "star-display__filled").is_displayed() and commentaire.find_element(By.CLASS_NAME, "star-display__filled").is_displayed() and commentaire.find_element(By.CLASS_NAME, "star-display__filled").is_displayed() and commentaire.find_element(By.CLASS_NAME, "star-display__half").is_displayed():
                    note = 3.5
                elif commentaire.find_element(By.CLASS_NAME, "star-display__filled").is_displayed() and commentaire.find_element(By.CLASS_NAME, "star-display__filled").is_displayed() and commentaire.find_element(By.CLASS_NAME, "star-display__filled").is_displayed() and commentaire.find_element(By.CLASS_NAME, "star-display__filled").is_displayed():
                    note = 4
                elif commentaire.find_element(By.CLASS_NAME, "star-display__filled").is_displayed() and commentaire.find_element(By.CLASS_NAME, "star-display__filled").is_displayed() and commentaire.find_element(By.CLASS_NAME, "star-display__filled").is_displayed() and commentaire.find_element(By.CLASS_NAME, "star-display__filled").is_displayed() and commentaire.find_element(By.CLASS_NAME, "star-display__half").is_displayed(): 
                    note = 4.5
                elif commentaire.find_element(By.CLASS_NAME, "star-display__filled").is_displayed() and commentaire.find_element(By.CLASS_NAME, "star-display__filled").is_displayed() and commentaire.find_element(By.CLASS_NAME, "star-display__filled").is_displayed() and commentaire.find_element(By.CLASS_NAME, "star-display__filled").is_displayed() and commentaire.find_element(By.CLASS_NAME, "star-display__filled").is_displayed():
                    note = 5
                else:
                    note = 0
        # calculer la note de l'utilisateur en multipliant la note par 5
            note_utilisateur = note
        
    # Stocker les données dans un dictionnaire
            donnees = {
        'Utilisateur': utilisateur,
        'Commentaire': texte_commentaire,
        'Note de l\'utilisateur': note_utilisateur
    }
    
    # Ajouter le dictionnaire à la liste
            donnees_commentaires.append(donnees)


# Vérifier si le bouton "next" est présent et cliquer dessus pour passer à la page suivante
while True:
    next_button = driver.find_element(By.CLASS_NAME, "next")
    if next_button.is_displayed():
        next_button.click()
        time.sleep(2)  # Attendre un court instant pour que la page se charge
        commentaires = driver.find_elements(By.CLASS_NAME, "audience-review-row")
        for commentaire in commentaires:
            utilisateur = commentaire.find_element(By.CLASS_NAME, "audience-reviews__name-wrap").text
            texte_commentaire = commentaire.find_element(By.CLASS_NAME, "audience-reviews__review.js-review-text").text
            for note in commentaire:
                if commentaire.find_element(By.CLASS_NAME, "star-display__half").is_displayed() :
                    note = 0.5
                elif commentaire.find_element(By.CLASS_NAME, "star-display__filled").is_displayed():
                    note = 1
                elif commentaire.find_element(By.CLASS_NAME, "star-display__filled").is_displayed() and commentaire.find_element(By.CLASS_NAME, "star-display__half").is_displayed():
                    note = 1.5
                elif commentaire.find_element(By.CLASS_NAME, "star-display__filled").is_displayed() and commentaire.find_element(By.CLASS_NAME, "star-display__filled").is_displayed():
                    note = 2
                elif commentaire.find_element(By.CLASS_NAME, "star-display__filled").is_displayed() and commentaire.find_element(By.CLASS_NAME, "star-display__filled").is_displayed() and commentaire.find_element(By.CLASS_NAME, "star-display__half").is_displayed():
                    note = 2.5
                elif commentaire.find_element(By.CLASS_NAME, "star-display__filled").is_displayed() and commentaire.find_element(By.CLASS_NAME, "star-display__filled").is_displayed() and commentaire.find_element(By.CLASS_NAME, "star-display__filled").is_displayed():
                    note = 3
                elif commentaire.find_element(By.CLASS_NAME, "star-display__filled").is_displayed() and commentaire.find_element(By.CLASS_NAME, "star-display__filled").is_displayed() and commentaire.find_element(By.CLASS_NAME, "star-display__filled").is_displayed() and commentaire.find_element(By.CLASS_NAME, "star-display__half").is_displayed():
                    note = 3.5
                elif commentaire.find_element(By.CLASS_NAME, "star-display__filled").is_displayed() and commentaire.find_element(By.CLASS_NAME, "star-display__filled").is_displayed() and commentaire.find_element(By.CLASS_NAME, "star-display__filled").is_displayed() and commentaire.find_element(By.CLASS_NAME, "star-display__filled").is_displayed():
                    note = 4
                elif commentaire.find_element(By.CLASS_NAME, "star-display__filled").is_displayed() and commentaire.find_element(By.CLASS_NAME, "star-display__filled").is_displayed() and commentaire.find_element(By.CLASS_NAME, "star-display__filled").is_displayed() and commentaire.find_element(By.CLASS_NAME, "star-display__filled").is_displayed() and commentaire.find_element(By.CLASS_NAME, "star-display__half").is_displayed(): 
                    note = 4.5
                elif commentaire.find_element(By.CLASS_NAME, "star-display__filled").is_displayed() and commentaire.find_element(By.CLASS_NAME, "star-display__filled").is_displayed() and commentaire.find_element(By.CLASS_NAME, "star-display__filled").is_displayed() and commentaire.find_element(By.CLASS_NAME, "star-display__filled").is_displayed() and commentaire.find_element(By.CLASS_NAME, "star-display__filled").is_displayed():
                    note = 5
                else:
                    note = 0
        # calculer la note de l'utilisateur en multipliant la note par 5
        note_utilisateur = note

            # Stocker les données dans un dictionnaire
        donnees = {
                'Utilisateur': utilisateur,
                'Commentaire': texte_commentaire,
                'Note de l\'utilisateur': note_utilisateur
            }
            
            # Ajouter le dictionnaire à la liste
        donnees_commentaires.append(donnees)
    else:
        break

# Chemin du fichier CSV de destination
chemin_fichier_csv = 'test_commentaires_rotten_tomatoes.csv'

# Écriture des données dans le fichier CSV
with open(chemin_fichier_csv, mode='w', newline='', encoding='utf-8') as fichier_csv:
    fieldnames = ['Utilisateur', 'Commentaire', 'Note de l\'utilisateur']
    writer = csv.DictWriter(fichier_csv, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(donnees_commentaires)

print("Les données des commentaires de Rotten Tomatoes ont été stockées dans le fichier CSV.")

# Fermer le navigateur
driver.quit()
