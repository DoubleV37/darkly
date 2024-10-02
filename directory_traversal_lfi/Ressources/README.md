# Directory/Path Traversal

## Comment j'ai exploité cette faille ?

En jouant avec l'url, on peut se déplacer dans les fichiers du serveur, ainsi en allant http://ip_server/?page=/../../../../../../../etc/passwd on accède au fichier etc passwd

## Qu'est ce que cette faille ?

Le Path Traversal permet à un attaquant de manipuler l'URL ou les paramètres d'une application web pour accéder à des fichiers en dehors du répertoire racine du serveur web. En exploitant cette vulnérabilité, un attaquant peut naviguer dans l'arborescence des fichiers du serveur et accéder à des fichiers sensibles comme /etc/passwd.

Dans une URL vulnérable, un attaquant pourrait utiliser des séquences comme ../ (signifiant "remonter d'un répertoire") pour sortir du répertoire prévu et accéder à d'autres parties du système de fichiers du serveur.

## Comment résoudre cette faille ?

- Validation des entrées : Vérifiez et nettoyez toutes les entrées utilisateur. Assurez-vous que les paramètres d'URL n'autorisent pas de caractères spéciaux comme ../.

- Contrôler les accès aux fichiers : Limitez l'accès aux fichiers en définissant des permissions strictes et en utilisant des listes blanches pour spécifier quels fichiers peuvent être accessibles via l'application.

- Utiliser des chemins absolus : Dans l'application, utilisez des chemins absolus pour les fichiers et assurez-vous que les utilisateurs ne peuvent pas les modifier.

## Sources

<https://owasp.org/www-community/attacks/Path_Traversal>
