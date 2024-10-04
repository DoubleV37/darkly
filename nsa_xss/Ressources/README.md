# Cross-Site Scripting (XSS)

## Comment j'ai exploité cette faille ?

Sur la page principale on peut trouver une image de la nsa où l'on peut cliquer.

Si on remplace "nsa" à la fin de l'url par :

`data:text/html;base64,PHNjcmlwdD5hbGVydCgndGVzdDMnKTwvc2NyaXB0Pg`

PHNjcmlwdD5hbGVydCgndGVzdDMnKTwvc2NyaXB0Pg correspondant décodé de la base 64 à :

`<script>alert('test3')</script>`

## Qu'est ce que cette faille ?

Ce type d'url `?page=media&src=` permet de charger un contenu sur la page, mal sécurisé il peut permettre de charger du javascript (faille XSS), des fichiers distants ou locaux (failles LFI/RFI) ou encore de permettre des injections SQL.

Les failles XSS peuvent notamment permettre de récupérer des cookies et des informations sensibles, comme les identifiants de session de l'utilisateur et ainsi contrôler son compte.

## Comment résoudre cette faille ?

On peut éviter cette faille en encodant les paramètres de l'url avant de faire le rendu de la page, restreindre les types attendus en paramètre dans l'url, utiliser des en-têtes HTTP sécurisés (Content Security Policy - CSP) qui bloque l'exécution de script extérieur non approuvé.

## Source

<https://owasp.org/www-community/attacks/xss/>
