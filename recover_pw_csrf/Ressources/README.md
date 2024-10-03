# Recover password

## Comment j'ai exploité cette faille ?

Quand on va sur la page Sign in, puis sur "I forgot my password", on arrive sur un bouton pour envoyer une demande. Avec la console d'inspection on peut voir un champ caché qui contient le mail de destination des demandes. Pour obtenir le flag il suffit de modifer le mail.

## Qu'est ce que cette faille ?

Cette faille nous donne accès à un mail qui pourrait être mal utilisé ou détourné.

## Comment résoudre cette faille ?

Validation côté serveur : Ne faites jamais confiance aux données provenant du client. Validez toujours les données côté serveur. En l'occurrence, vous devriez vérifier si l'adresse e-mail soumise correspond bien à celle attendue (webmaster@borntosec.com), et rejeter toute soumission qui contient des valeurs modifiées.

Utiliser des jetons de sécurité (CSRF tokens) : Ajoutez un token unique et généré dynamiquement dans les formulaires pour s'assurer que les soumissions proviennent de sources légitimes et pour protéger contre les attaques de falsification de requêtes (CSRF).
