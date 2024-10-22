# Utilise une image Ubuntu légère comme base
FROM ubuntu:latest

# Met à jour le système et installe Zsh, Hydra et Curl
RUN apt-get update && apt-get install -y \
    zsh \
    hydra \
    curl

# Définit le shell par défaut sur Zsh
SHELL ["/bin/zsh", "-c"]

# Copie ton script dans le conteneur
COPY script.sh /usr/local/bin/script.sh

# Copie la liste des mots de passe dans le conteneur
COPY 10000-most-common-passwords.txt /usr/local/bin/10000-most-common-passwords.txt

# Rend le script exécutable
RUN chmod +x /usr/local/bin/script.sh

# Définit le point d'entrée du conteneur sur le script
ENTRYPOINT ["/usr/local/bin/script.sh"]

