# Open redirection

## Comment j'ai exploité cette faille ?

En mode inspection sur la page principale, on peut modifier l'url de la redirection d'instagram dans le pied de page, et ainsi mettre une autre url.

## Qu'est ce que cette faille ?

Une redirection ouverte se produit lorsqu'un site web accepte une URL externe dans un paramètre (comme ici avec site=instagram) et redirige l'utilisateur vers cette URL sans vérifier sa validité. Cela peut être exploité par des attaquants pour rediriger les utilisateurs vers des sites malveillants, phishing, ou d'autres destinations dangereuses.

## Comment résoudre cette faille ?

Plusieurs solutions :

Valider les URLs : Assurez-vous que seules des URLs autorisées peuvent être utilisées dans le paramètre site. Une solution consiste à utiliser une liste blanche (whitelist) de domaines vers lesquels la redirection est permise.

Utiliser des redirections internes : Si possible, au lieu de rediriger vers des URLs externes directement, redirigez vers une page interne et gérez la redirection en interne sur le serveur.

Encodage et validation des paramètres : Utilisez l'encodage pour éviter les manipulations des paramètres URL, et validez rigoureusement toutes les entrées de l'utilisateur.

## Sources

<https://cheatsheetseries.owasp.org/cheatsheets/Unvalidated_Redirects_and_Forwards_Cheat_Sheet.html>
