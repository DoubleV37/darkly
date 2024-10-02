# Fichier Robots.txt

## Comment j'ai exploité cette faille ?

Quand on va sur /robots.txt, on peut voir 2 chemins : /whatever et /.hidden.

Si on va sur /whatever, on trouve un index qui nous permet d'accéder au fichier htpassswd qui contient les informations de connexion de l'utilisateur root. Son mot de passse est crypté en md5.

Quand on le décrypte on obtient le mot de passe qwerty123@.

On peut ensuite aller sur /admin pour entrer root et le mot de passe ci-dessus.

## Qu'est ce que cette faille ?

Le fichier robots.txt est un fichier pour contrôler l'accès des robots des moteurs de recherche à certaines parties d'un site web. Il sert principalement à indiquer aux crawlers (ou robots d'exploration) quelles pages ou sections du site ne doivent pas être explorées ou indexées.

## Comment résoudre cette faille ?

Ajouter un .htaccess pour restreindre l'accès ou changer la configuration du reverse proxy pour empecher l'accès aux fichiers de ce type.

## Sources

<https://developers.google.com/search/docs/crawling-indexing/robots/intro?hl=fr>


