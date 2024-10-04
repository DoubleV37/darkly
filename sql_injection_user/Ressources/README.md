# SQL Injection user

## Comment j'ai exploité cette faille ?

`1 or 1 = 1`

Nous donne la liste de tous les users.

`1 UNION select table_name, column_name FROM information_schema.columns`

Cela nous permet de savoir les colonnes de la tables users notamment, ce qui nous permet de faire ensuite :

`1 UNION SELECT Commentaire, countersign from users`

On obtienbt une consigne qui nous dit de décoder une chaine de caractère en md5 puis de passer la chaine obtenue en minuscule et enfin l'encoder en sha256 pour obtenir le flag.

## Qu'est ce que cette faille ?

Les injections SQL consiste à intégrer une requête SQL dans un champ mal protégé. En partant d'une requête toujours vrai (ex : 1) on peut joindre la requête voulu pour obtenir les informations désirées. Cela constitue donc une faille de sécurité importante, puisqu'on peut accéder aux informations de la base de données sans authentfication, et récupérer des informations sensibles comme des mots de passe ou des informations personnelles.

## Comment résoudre cette faille ?

Il y a plusieurs façon d'éviter les injections SQL, en voici quelques une. On peut utiliser des requêtes préparées où on ajoute les élements dans le modèle de requête, et ainsi éviter les requêtes détournées. L'utilisation d'un ORM (Object-Relational Mapping) ajoute une couche d'abstraction entre l'application et la base de données et permet de se protéger. L'ajout d'un WAF (web application firewall) peut détecter et bloquer les attaques par injection SQL.

## Source

<https://owasp.org/www-community/attacks/SQL_Injection>
