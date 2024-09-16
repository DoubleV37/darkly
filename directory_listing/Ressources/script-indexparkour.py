#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse


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

    for a_tag in soup.find_all('a', href=True):
        href = a_tag['href']
        full_url = urljoin(base_url, href)
        # Éviter les boucles infinies
        if full_url in visited_urls:
            continue
        visited_urls.add(full_url)

        # Vérifier si c'est un fichier README
        if 'README' in href: 
            cpt+=1
            response = requests.head(full_url)
            size = response.headers.get('Content-Length')
            print("\r", cpt, end="", flush=True)
            if int(size) != 34:
                print("\r", cpt, "\n", get_html_content(full_url))
                return True
        elif href.endswith('/'):  # Si c'est un sous-dossier
            dir_content = get_html_content(full_url)
            if dir_content:
                # Parcourir récursivement les sous-dossiers
                if (find_readme_links(full_url, dir_content, visited_urls)):
                    return True
    return False

def main(start_url):
    global cpt
    cpt = 0
    visited_urls = set()
    index_content = get_html_content(start_url)
    if not index_content:
        return
    
    find_readme_links(start_url, index_content, visited_urls)
    print("Ça fait beaucoup là, non ???")

if __name__ == "__main__":
    start_url = 'http://192.168.0.97/.hidden/'
    main(start_url)

