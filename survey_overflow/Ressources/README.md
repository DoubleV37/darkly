# Integer overflow

## Comment j'ai exploité cette faille ?

Dans la partie survey du site, avec la console d'inspection, on peut modifier les valeurs du formulaire. Ainsi si on peut modifier une valeur pour qu'une fois sélectionnée elle provoque un overflow.

## Qu'est ce que cette faille ?

Si la valeur modifiée est utilisée dans des opérations mathématiques, un dépassement de type "integer overflow" peut entraîner un comportement imprévisible, comme l'accès à des zones de mémoire non prévues.

Ce type de vulnérabilité peut être utilisé en combinaison avec d'autres failles pour exploiter davantage le système.

## Comment résoudre cette faille ?

Validation côté serveur : Il est essentiel de valider toutes les données envoyées par le client. Assurez-vous que le serveur ne traite que les valeurs légitimes et attendues. Par exemple, vérifier que la valeur du <select> correspond bien à une des options définies.

Limiter la taille des entrées : Vous devez limiter la taille des valeurs qui peuvent être envoyées via un formulaire. Cela peut être fait à la fois côté client (pour l'expérience utilisateur) et surtout côté serveur pour éviter les abus.

Utiliser des mécanismes de sécurité appropriés : Si l'application utilise des nombres ou des entiers pour les options du <select>, assurez-vous que les valeurs sont correctement gérées et que des mécanismes de protection contre les dépassements (comme le type casting ou la vérification des plages de valeurs) sont en place.

Éviter la confiance dans les données client : Ne faites jamais confiance aux données envoyées par le client, car elles peuvent facilement être modifiées. Cela inclut les valeurs des formulaires et même les cookies et headers HTTP.

Contrôle strict des types et des formats : Imposer des contraintes strictes sur le format des données. Par exemple, si une valeur de select est censée être un entier entre 1 et 3, vérifiez cela explicitement avant d'utiliser la valeur.
