# Exploitation du cookie IAM admin

## Étapes de l'exploitation

1. **Analyse du cookie :**
   - Nous avons constaté que le site se base sur une valeur MD5 pour déterminer les privilèges administratifs. Le cookie `I_am_admin` contenant la valeur MD5 de `false` signifie que l'utilisateur est considéré comme non-administrateur.

2. **Modification du cookie :**
   - Si nous remplaçons la valeur du cookie par le hash MD5 de `true`, soit `b326b5062b2f0e69046810717534cb09`, nous pouvons tromper le site en lui faisant croire que nous sommes un administrateur.

3. **Résultat de la modification :**
   - Après avoir modifié le cookie avec la valeur MD5 de `true`, le site nous accorde les privilèges administratifs et nous dévoile le flag suivant :

```plaintext
df2eb4ba34ed059a1e3e89ff4dfc13445f104a1a52295214def1c4fb1693a5c3
```

## Analyse de la faille

La vulnérabilité repose sur une mauvaise implémentation de la gestion des sessions utilisateurs. En utilisant des valeurs codées en MD5 pour vérifier les privilèges, le site devient vulnérable à une modification simple de cookie.

## Solution

Pour corriger cette faille de sécurité, plusieurs solutions peuvent être envisagées :

1. **Utiliser un algorithme de hachage plus sécurisé :** Le MD5 ne doit plus être utilisé pour la vérification de l'authentification ou de privilèges. SHA-256 ou des algorithmes plus récents doivent être privilégiés.

2. **Signer les cookies :** Utiliser des cookies signés permettrait de garantir que les utilisateurs ne puissent pas les modifier sans être détectés par le serveur.

3. **Vérifier côté serveur :** Les privilèges des utilisateurs doivent être vérifiés à partir d'une base de données ou d'une session serveur, et non à partir des informations modifiables par l'utilisateur comme les cookies.

## Conclusion

Cette faille de sécurité montre l'importance de ne pas se fier aux valeurs envoyées par le client, surtout lorsqu'il s'agit de gérer des privilèges administratifs. En modifiant simplement un cookie MD5, nous avons pu obtenir un accès administrateur et découvrir le flag.
