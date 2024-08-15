import requests, time
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import re


def get_html_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Erreur lors de la récupération de {url}: {e}")
        return None

def find_readme_links(base_url, html_content, visited_urls):
    global cpt
    soup = BeautifulSoup(html_content, 'html.parser')
    links = []

    for a_tag in soup.find_all('a', href=True):
        href = a_tag['href']
        full_url = urljoin(base_url, href)
        if cpt % 53000 == 0:
            print("slip = ", cpt)
            time.sleep(10)
        cpt+=1
        # Éviter les boucles infinies
        if full_url in visited_urls:
            continue
        visited_urls.add(full_url)

        # Vérifier si c'est un fichier README
        if 'README' in href: 
            links.append(full_url)
        elif href.endswith('/'):  # Si c'est un sous-dossier
            dir_content = get_html_content(full_url)
            if dir_content:
                # Parcourir récursivement les sous-dossiers
                links.extend(find_readme_links(full_url, dir_content, visited_urls))
    return links

def fetch_readme_contents(readme_links):
    readme_contents = []
    for link in readme_links:
        content = get_html_content(link)
        if content:
            readme_contents.append(f"### Contenu de {link}\n")
            readme_contents.append(content)
            readme_contents.append("\n\n")
    return readme_contents

def main(start_url, output_file):
    global cpt
    cpt = 0
    visited_urls = set()
    index_content = get_html_content(start_url)
    if not index_content:
        return
    
    readme_links = find_readme_links(start_url, index_content, visited_urls)
    readme_contents = fetch_readme_contents(readme_links)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.writelines(readme_contents)
    
    print(f"Tous les README ont été sauvegardés dans {output_file}")

if __name__ == "__main__":
    start_url = 'http://10.11.249.37/.hidden/'  # Remplacez par l'URL de votre index
    output_file = 'tous_les_readme.txt'
    main(start_url, output_file)

