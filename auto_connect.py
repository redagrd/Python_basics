from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Ouvrir le navigateur
driver = webdriver.Chrome()

# Charger la page de login
driver.get("https://sign.m2iformation.fr/signin")

# Récupérer les champs de saisie de login et de mot de passe
username_field = driver.find_element_by_name("0000180872")
password_field = driver.find_element_by_name("75110")

# Remplir les champs de login et de mot de passe
username_field.send_keys("0000180872")
password_field.send_keys("75110")

# Cliquer sur le bouton de connexion
driver.find_element_by_css_selector(".login-btn").click()

# Attendre que la page se charge
time.sleep(5)

# Cliquer sur le bouton pour signer la présence
driver.find_element_by_css_selector(".presence-sign-btn").click()

# Fermer le navigateur
driver.quit()