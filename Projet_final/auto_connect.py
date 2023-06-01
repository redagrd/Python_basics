from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time
import threading

# Ouvrir le navigateur
driver = webdriver.Chrome(ChromeDriverManager().install())


# Charger la page de login
driver.get("https://sign.m2iformation.fr/signin")

# Récupérer les champs de saisie de login et de mot de passe
username_field = driver.find_element_by_name("0000180872")
password_field = driver.find_element_by_name("75110")

# Remplir les champs de login et de mot de passe
username_field.send_keys("0000180872")
password_field.send_keys("75110")

# Cliquer sur le bouton de connexion
driver.find_element_by_css_selector("connexion.btn w-50 mt-3").click()

# Attendre que la page se charge
time.sleep(5000)
driver.quit()
# Cliquer sur le bouton pour signer la présence
#driver.find_element_by_css_selector("<a href="/timesheet"><span style="border:0.10rem solid;border-radius: 0.75rem;" class="m-2 small badge">2</span>Feuille de présence</a>").click()

# Signer la colonne correspondant à la date du jour


# Fermer le navigateur
