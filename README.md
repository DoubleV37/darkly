# Darkly

## 1. Directory Listing (/.hidden/)

### Explication de la faille

Lorsqu'un serveur web n'est pas configuré correctement, il peut permettre aux utilisateurs d'accéder à un répertoire en affichant tout son contenu (fichiers et sous-répertoires). Par exemple, si vous accédez à https://example.com/.hidden/, et que le serveur n'a pas de fichier d'index (comme index.html) ou n'a pas été configuré pour bloquer l'accès à ce répertoire, le serveur affichera une liste de tous les fichiers et répertoires contenus dans .hidden.

### Risques associés

- Accès non autorisé à des fichiers sensibles : Certains fichiers peuvent contenir des informations sensibles, comme des configurations de serveur, des données utilisateurs, des backups, etc.
- Exploration de l'arborescence du site : Un attaquant pourrait cartographier la structure du site et découvrir des chemins d'accès à d'autres ressources sensibles.
- Attaques supplémentaires : Une fois que l'attaquant a découvert des fichiers sensibles, il pourrait les utiliser pour lancer d'autres attaques (par exemple, injection de code, récupération de mots de passe, etc.).

### Comment corriger la faille

Désactiver l'indexation des répertoires : Configurer le serveur web pour qu'il ne génère pas automatiquement de liste des fichiers d'un répertoire.

- Pour Apache, vous pouvez désactiver cela en ajoutant Options -Indexes dans le fichier de configuration du serveur ou dans un fichier .htaccess.
- Pour Nginx, vous devez vous assurer que l'option autoindex est désactivée dans la configuration du serveur.
Restreindre l'accès aux répertoires sensibles : Utiliser des fichiers .htaccess (sur Apache) ou configurer Nginx pour restreindre l'accès à certains répertoires.

Placer un fichier d'index (index.html) dans les répertoires critiques pour éviter l'affichage de la liste de fichiers.

Contrôler les permissions des fichiers et répertoires : Assurez-vous que les permissions des fichiers et des répertoires sont correctement définies, de manière à ce que seuls les utilisateurs autorisés puissent y accéder.

## 2. Path Traversal ou Directory Traversal ([url de la faille](http://10.11.249.37/?page=/../../../../../../../etc/passwd))

### Explication de la faille
Le Path Traversal permet à un attaquant de manipuler l'URL ou les paramètres d'une application web pour accéder à des fichiers en dehors du répertoire racine du serveur web. En exploitant cette vulnérabilité, un attaquant peut naviguer dans l'arborescence des fichiers du serveur et accéder à des fichiers sensibles comme /etc/passwd.

Dans une URL vulnérable, un attaquant pourrait utiliser des séquences comme ../ (signifiant "remonter d'un répertoire") pour sortir du répertoire prévu et accéder à d'autres parties du système de fichiers du serveur.

### Risques associés
- Accès à des informations sensibles : Le fichier /etc/passwd contient des informations sur les utilisateurs du système. Même si les mots de passe ne sont plus stockés directement dans ce fichier (ils sont dans /etc/shadow), il reste une source précieuse pour des attaques ultérieures.
- Escalade des privilèges : Un attaquant peut obtenir des informations qui l'aideront à escalader ses privilèges sur le serveur.
- Accès à d'autres fichiers critiques : Le même principe peut être utilisé pour accéder à d'autres fichiers sensibles, comme des configurations de serveurs, des bases de données, etc.

### Comment corriger la faille
- Validation des entrées : Vérifiez et nettoyez toutes les entrées utilisateur. Assurez-vous que les paramètres d'URL n'autorisent pas de caractères spéciaux comme ../.

- Contrôler les accès aux fichiers : Limitez l'accès aux fichiers en définissant des permissions strictes et en utilisant des listes blanches pour spécifier quels fichiers peuvent être accessibles via l'application.

- Utiliser des chemins absolus : Dans l'application, utilisez des chemins absolus pour les fichiers et assurez-vous que les utilisateurs ne peuvent pas les modifier.

- Configuration du serveur : Assurez-vous que le serveur web est correctement configuré pour éviter que l'application ne puisse accéder à des fichiers en dehors de son répertoire autorisé.

- Audit de sécurité : Effectuez un audit de sécurité pour identifier et corriger toute autre vulnérabilité potentielle.

## 3. Brute-force mot de passe admin

### Explication de la faille
Le brute-forcing est une méthode d'attaque où un attaquant tente systématiquement toutes les combinaisons possibles de mots de passe jusqu'à trouver la bonne. Cela peut être effectué manuellement, mais est généralement automatisé à l'aide de scripts ou d'outils spécialisés.

Si vous avez pu brute-forcer un mot de passe, cela signifie probablement que la page de login ne dispose pas de mesures de sécurité suffisantes pour prévenir ce type d'attaque.

### Facteurs facilitant l'attaque
- Absence de limitation de tentatives : Si la page de connexion ne limite pas le nombre de tentatives de connexion par minute ou par IP, un attaquant peut essayer un grand nombre de combinaisons en peu de temps.

- Absence de captchas : Sans captchas, il est facile pour un script automatisé de tester de nombreuses combinaisons.

- Mot de passe faible : Si le mot de passe de l'utilisateur admin est faible (court, basé sur des mots courants, etc.), il est plus facile à brute-forcer.

- Pas de délai entre les tentatives : Si le serveur ne met pas en place un délai ou un mécanisme de verrouillage après plusieurs tentatives échouées, cela facilite les attaques par force brute.

### Risques associés

- Accès non autorisé à des comptes sensibles : L'attaquant pourrait obtenir l'accès complet à l'interface d'administration du site.
- Exécution de commandes malveillantes : Avec les droits d'administration, l'attaquant pourrait exécuter des scripts, installer des logiciels malveillants, voler des données sensibles, etc.
- Déni de service : Une fois en possession des droits d'administration, l'attaquant pourrait modifier ou supprimer des fichiers, rendant le site inutilisable.

### Comment corriger la faille
- Implémenter des limitations de tentatives de connexion :

  - Bloquer l'accès après un certain nombre de tentatives échouées (par exemple, 3 à 5).
  - Imposer un délai entre les tentatives après plusieurs échecs (par exemple, 30 secondes, puis 1 minute, etc.).
- Utiliser des captchas : Pour se protéger contre les attaques automatisées, utilisez des captchas après un certain nombre de tentatives échouées.

- Imposer des règles de complexité pour les mots de passe : Exiger que les mots de passe soient longs (au moins 12 caractères) et complexes (mélange de majuscules, minuscules, chiffres, et caractères spéciaux).

- Utiliser l'authentification multi-facteurs (MFA) : Ajouter un second facteur de vérification, comme un code envoyé par SMS ou une application d'authentification, pour renforcer la sécurité des comptes.

- Surveiller les tentatives de connexion : Implémenter des mécanismes de journalisation pour surveiller les tentatives de connexion suspectes et alerter les administrateurs.

- Vérification des mots de passe contre des listes de mots de passe compromis : Utiliser des services ou des bases de données pour vérifier que les mots de passe choisis ne figurent pas sur des listes de mots de passe ayant déjà été compromis.

## 4. 

#

**Darkly** (adverbe) :

1. En français : **sombrement**
2. Utilisation :
   - Dans un contexte littéral, "darkly" peut décrire quelque chose qui est sombre ou obscur. Par exemple : "He looked at her darkly," pourrait se traduire par "Il la regarda sombrement."
   - Dans un contexte figuré, "darkly" peut aussi signifier de manière menaçante ou inquiétante. Par exemple : "She spoke darkly of the future," pourrait se traduire par "Elle parla sombrement de l'avenir."
