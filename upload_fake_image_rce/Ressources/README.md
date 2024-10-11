# Faille d'Upload de Fichier

Dans ce challenge de CTF, nous avons découvert une vulnérabilité liée à l'upload de fichiers. Le site permet de téléverser des fichiers via un formulaire, mais il est possible d'exploiter cette fonctionnalité pour uploader des fichiers malveillants déguisés en images.

## Détails de l'attaque

Nous avons utilisé la commande suivante pour exploiter la faille d'upload :

```bash
curl -F "uploaded=@r.php;type=image/jpeg" -F "Upload=Upload" 'http://10.11.249.37/?page=upload#'
```

### Explication de la commande

- **`-F "uploaded=@r.php;type=image/jpeg"`** : Cette option simule l'upload d'un fichier via la méthode POST. Le fichier `r.php` est sélectionné, mais nous indiquons au serveur que son type est "image/jpeg" pour tromper le système. En réalité, il s'agit d'un fichier PHP malveillant.
- **`-F "Upload=Upload"`** : Simule l'envoi du formulaire d'upload, comme si un utilisateur soumettait le formulaire depuis une page web.
- **`'http://10.11.249.37/?page=upload#'`** : L'URL cible du formulaire d'upload du site web.

L'idée est de faire croire au serveur que le fichier uploadé est une image en utilisant le faux type MIME "image/jpeg", alors qu'il s'agit en réalité d'un script PHP que nous pourrions exécuter par la suite.

## Résultat de l'attaque

En soumettant cette requête, le fichier PHP est accepté par le serveur, même s'il ne s'agit pas d'une véritable image. Une fois téléversé, nous pouvons accéder à ce fichier via son URL sur le serveur, ce qui nous permet d'exécuter du code PHP.

### Conséquences

- **Exécution de code à distance (RCE)** : Le fichier PHP malveillant peut contenir du code permettant d'exécuter des commandes sur le serveur, compromettant ainsi l'ensemble du système.
- **Web Shell** : L'attaquant pourrait créer un shell interactif à partir du fichier PHP uploadé, lui permettant de contrôler le serveur à distance.

## Analyse de la faille

Cette faille repose sur la mauvaise validation des fichiers uploadés. Le serveur se base uniquement sur les informations fournies par le client, telles que le type MIME, pour déterminer s'il s'agit d'une image. Cependant, cela est facilement contourné car il est possible de falsifier cette information et d'uploader des fichiers exécutables comme des scripts PHP.

### Problèmes principaux

- **Validation insuffisante du type MIME** : Le serveur accepte les fichiers en se basant sur le type MIME fourni par l'utilisateur sans vérifier le contenu réel du fichier.
- **Pas de validation de l'extension** : Le serveur ne semble pas vérifier l'extension du fichier (ici, `.php`), ce qui permet l'upload de fichiers exécutables.

## Patch

Pour corriger cette faille de sécurité, plusieurs mesures doivent être mises en place :

1. **Validation du contenu des fichiers** : Ne pas se fier uniquement au type MIME fourni par l'utilisateur. Le serveur doit analyser le contenu réel du fichier uploadé pour s'assurer qu'il s'agit bien d'une image. Cela peut être fait à l'aide de bibliothèques de traitement d'images, comme **GD** ou **ImageMagick**, qui peuvent valider le format réel d'une image.

2. **Restreindre les extensions autorisées** : Le serveur doit uniquement accepter des fichiers avec des extensions spécifiques, comme `.jpg`, `.png`, et refuser tous les autres types, en particulier les fichiers `.php`, `.html`, ou tout fichier exécutable.

3. **Renommer les fichiers uploadés** : Pour éviter que des fichiers malveillants soient directement exécutables, tous les fichiers uploadés devraient être renommés avec des noms uniques générés de manière aléatoire. Cela permet aussi de prévenir les collisions de noms.

4. **Interdire l'exécution de fichiers dans les répertoires d'uploads** : Les répertoires où les fichiers sont téléversés ne devraient jamais permettre l'exécution de scripts. Par exemple, dans Apache, cela peut être configuré avec l'option `Options -ExecCGI` ou en désactivant l'exécution de PHP dans le répertoire d'uploads.

5. **Utiliser une sandbox pour tester les fichiers uploadés** : Avant de permettre à un fichier d'être pleinement accessible, il pourrait être testé dans un environnement isolé pour vérifier s'il contient des comportements malveillants ou des failles.

## Conclusion

Cette faille d'upload met en lumière l'importance de valider correctement les fichiers envoyés par les utilisateurs. En permettant l'upload de scripts PHP sous prétexte d'une image JPEG, le serveur devient vulnérable à des attaques critiques, telles que l'exécution de code à distance. Des mesures de validation plus strictes et une gestion plus rigoureuse des fichiers uploadés sont essentielles pour protéger les applications web contre ce type d'exploitation.
