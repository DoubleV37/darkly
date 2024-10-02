# Directory Listing

## Comment j'ai exploité cette faille ?

Quand on va sur /.hidden, on se retrouve sur un index de fichiers. Pour le parcourir efficacement pour trouver un contenu pertinant dans ces fichiers on a utilisé un programme en python. Il parcourt tout les dossiers et ses sous-dossiers et regarde le contenu de chaque fichier.

## Qu'est ce que cette faille ?

Lorsqu'un serveur web n'est pas configuré correctement, il peut permettre aux utilisateurs d'accéder à un répertoire en affichant tout son contenu (fichiers et sous-répertoires). Par exemple, si vous accédez à https://example.com/.hidden/, et que le serveur n'a pas de fichier d'index (comme index.html) ou n'a pas été configuré pour bloquer l'accès à ce répertoire, le serveur affichera une liste de tous les fichiers et répertoires contenus dans .hidden.

## Comment résoudre cette faille ?

Désactiver l'indexation des répertoires : Configurer le serveur web pour qu'il ne génère pas automatiquement de liste des fichiers d'un répertoire.

- Pour Apache, vous pouvez désactiver cela en ajoutant Options -Indexes dans le fichier de configuration du serveur ou dans un fichier .htaccess.
- Pour Nginx, vous devez vous assurer que l'option autoindex est désactivée dans la configuration du serveur.
Restreindre l'accès aux répertoires sensibles : Utiliser des fichiers .htaccess (sur Apache) ou configurer Nginx pour restreindre l'accès à certains répertoires.

Placer un fichier d'index (index.html) dans les répertoires critiques pour éviter l'affichage de la liste de fichiers.

Contrôler les permissions des fichiers et répertoires : Assurez-vous que les permissions des fichiers et des répertoires sont correctement définies, de manière à ce que seuls les utilisateurs autorisés puissent y accéder.

## Sources

<https://www.it-connect.fr/quest-ce-que-le-directory-browsinglisting/>
