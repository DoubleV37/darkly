# Darkly

## 3. Brute-force mot de passe admin

### Explication de la faille
Le brute-forcing est une méthode d'attaque où un attaquant tente systématiquement toutes les combinaisons possibles de mots de passe jusqu'à trouver la bonne. Cela peut être effectué manuellement, mais est généralement automatisé à l'aide de scripts ou d'outils spécialisés.

Si vous avez pu brute-forcer un mot de passe, cela signifie probablement que la page de login ne dispose pas de mesures de sécurité suffisantes pour prévenir ce type d'attaque.

### Facteurs facilitant l'attaque
- Absence de limitation de tentatives : Si la page de connexion ne limite pas le nombre de tentatives de connexion par minute ou par IP, un attaquant peut essayer un grand nombre de combinaisons en peu de temps.

- Absence de captchas : Sans captchas, il est facile pour un script automatisé de tester de nombreuses combinaisons.

- Mot de passe faible : Si le mot de passe de l'utilisateur admin est faible (court, basé sur des mots courants, etc.), il est plus facile à brute-forcer.

- Pas de délai entre les tentatives : Si le serveur ne met pas en place un délai ou un mécanisme de verrouillage après plusieurs tentatives échouées, cela facilite les attaques par force brute.

### Risques associés

- Accès non autorisé à des comptes sensibles : L'attaquant pourrait obtenir l'accès complet à l'interface d'administration du site.
- Exécution de commandes malveillantes : Avec les droits d'administration, l'attaquant pourrait exécuter des scripts, installer des logiciels malveillants, voler des données sensibles, etc.
- Déni de service : Une fois en possession des droits d'administration, l'attaquant pourrait modifier ou supprimer des fichiers, rendant le site inutilisable.

### Comment corriger la faille
- Implémenter des limitations de tentatives de connexion :

  - Bloquer l'accès après un certain nombre de tentatives échouées (par exemple, 3 à 5).
  - Imposer un délai entre les tentatives après plusieurs échecs (par exemple, 30 secondes, puis 1 minute, etc.).
- Utiliser des captchas : Pour se protéger contre les attaques automatisées, utilisez des captchas après un certain nombre de tentatives échouées.

- Imposer des règles de complexité pour les mots de passe : Exiger que les mots de passe soient longs (au moins 12 caractères) et complexes (mélange de majuscules, minuscules, chiffres, et caractères spéciaux).

- Utiliser l'authentification multi-facteurs (MFA) : Ajouter un second facteur de vérification, comme un code envoyé par SMS ou une application d'authentification, pour renforcer la sécurité des comptes.

- Surveiller les tentatives de connexion : Implémenter des mécanismes de journalisation pour surveiller les tentatives de connexion suspectes et alerter les administrateurs.

- Vérification des mots de passe contre des listes de mots de passe compromis : Utiliser des services ou des bases de données pour vérifier que les mots de passe choisis ne figurent pas sur des listes de mots de passe ayant déjà été compromis.


## 6.hidden dans le form de forget password

### Explication de la faille potentielle

Dans votre exemple, la balise suivante est utilisée pour envoyer une adresse e-mail :

```html
<input type="hidden" name="mail" value="webmaster@borntosec.com" maxlength="15">
```

Bien que cette valeur ne soit pas visible à l'utilisateur, elle peut facilement être modifiée. Un attaquant pourrait changer cette valeur avec des outils comme l'inspecteur d'éléments du navigateur et la remplacer par une autre adresse e-mail avant de soumettre le formulaire.

### Risques associés

    Modification des données : Comme les champs hidden sont modifiables, un utilisateur malveillant pourrait remplacer webmaster@borntosec.com par une autre adresse e-mail. Cela pourrait entraîner des envois de données sensibles à des adresses non prévues.

    Usurpation d'identité : Si cette adresse e-mail est utilisée pour des opérations d'authentification ou de gestion d'accès, un attaquant pourrait utiliser cette faille pour usurper l'identité d'un autre utilisateur ou d'un administrateur.

    Exfiltration de données : Si le champ caché contient des informations sensibles (comme des identifiants ou des informations d'accès), un attaquant pourrait récupérer ou modifier ces données.

### Comment corriger la faille

    Validation côté serveur : Ne faites jamais confiance aux données provenant du client. Validez toujours les données côté serveur. En l'occurrence, vous devriez vérifier si l'adresse e-mail soumise correspond bien à celle attendue (webmaster@borntosec.com), et rejeter toute soumission qui contient des valeurs modifiées.

    Exemple de vérification côté serveur (PHP) :

```php
if ($_POST['mail'] !== 'webmaster@borntosec.com') {
    die("Tentative de soumission invalide.");
}
```

Éviter les champs hidden pour des données critiques : Les informations sensibles ne devraient pas être stockées dans des champs cachés du formulaire. Si des données sensibles doivent être transmises, utilisez des méthodes sécurisées comme les sessions serveur pour stocker ces informations.

Utiliser des jetons de sécurité (CSRF tokens) : Ajoutez un token unique et généré dynamiquement dans les formulaires pour s'assurer que les soumissions proviennent de sources légitimes et pour protéger contre les attaques de falsification de requêtes (CSRF).

Exemple de champ CSRF caché :

```html
<input type="hidden" name="csrf_token" value="GENERATED_TOKEN">
```

Puis, vérifiez ce jeton côté serveur avant d'accepter la soumission.

Limiter la longueur de l'input : Bien que la propriété maxlength soit définie dans l'input, cela n'est pas suffisant pour protéger contre la modification des données. Validez également la longueur des données côté serveur.



#

#

**Darkly** (adverbe) :

1. En français : **sombrement**
2. Utilisation :
   - Dans un contexte littéral, "darkly" peut décrire quelque chose qui est sombre ou obscur. Par exemple : "He looked at her darkly," pourrait se traduire par "Il la regarda sombrement."
   - Dans un contexte figuré, "darkly" peut aussi signifier de manière menaçante ou inquiétante. Par exemple : "She spoke darkly of the future," pourrait se traduire par "Elle parla sombrement de l'avenir."
