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

## 4. Overflow du form Survey

### Explication de la faille

Lorsqu'un utilisateur modifie manuellement la valeur d'un `<select>` dans un formulaire (par exemple via les outils de développement du navigateur), et que le serveur ne valide pas correctement les valeurs envoyées, cela peut entraîner un buffer overflow, un integer overflow, ou d'autres types de dépassement de capacité.

### Cela peut se produire si :

    La valeur envoyée dépasse la longueur attendue par le serveur ou le système (buffer overflow).
    La valeur est un entier plus grand que prévu et provoque un dépassement dans les calculs (integer overflow).
    L'application ne vérifie pas que la valeur du <select> correspond bien aux options prédéfinies.

### Risques associés

    Buffer Overflow : Un dépassement de tampon peut être exploité pour exécuter du code arbitraire ou planter l'application. Dans des cas extrêmes, un attaquant pourrait utiliser cette vulnérabilité pour injecter du code malveillant, compromettant ainsi le serveur ou l'application.

    Integer Overflow : Si la valeur modifiée est utilisée dans des opérations mathématiques, un dépassement de type "integer overflow" peut entraîner un comportement imprévisible, comme l'accès à des zones de mémoire non prévues.

    Bypass de la logique applicative : En modifiant la valeur d'une option <select>, un attaquant pourrait contourner des contrôles ou obtenir un accès à des options qui ne devraient pas être disponibles, par exemple en modifiant des choix comme des rôles utilisateurs (admin/user) ou des produits/services qui ne sont normalement pas sélectionnables.

    Attaques ultérieures : Ce type de vulnérabilité peut être utilisé en combinaison avec d'autres failles pour exploiter davantage le système.

### Exemple de scénario

Imaginons un formulaire avec une liste déroulante `<select>` pour choisir un produit ou une option d'abonnement :

```html
<form action="submit.php" method="post">
  <label for="subscription">Choose a subscription plan:</label>
  <select name="subscription" id="subscription">
    <option value="1">Basic</option>
    <option value="2">Pro</option>
    <option value="3">Premium</option>
  </select>
  <input type="submit" value="Submit">
</form>
```

Un utilisateur malveillant pourrait utiliser les outils de développement de son navigateur pour modifier l'option à une valeur non prévue, comme "9999999999999999" ou un texte arbitraire, et ainsi provoquer un overflow dans le traitement des données.

### Comment corriger la faille

    Validation côté serveur : Il est essentiel de valider toutes les données envoyées par le client. Assurez-vous que le serveur ne traite que les valeurs légitimes et attendues. Par exemple, vérifier que la valeur du <select> correspond bien à une des options définies.

    Limiter la taille des entrées : Vous devez limiter la taille des valeurs qui peuvent être envoyées via un formulaire. Cela peut être fait à la fois côté client (pour l'expérience utilisateur) et surtout côté serveur pour éviter les abus.

    Utiliser des mécanismes de sécurité appropriés : Si l'application utilise des nombres ou des entiers pour les options du <select>, assurez-vous que les valeurs sont correctement gérées et que des mécanismes de protection contre les dépassements (comme le type casting ou la vérification des plages de valeurs) sont en place.

    Éviter la confiance dans les données client : Ne faites jamais confiance aux données envoyées par le client, car elles peuvent facilement être modifiées. Cela inclut les valeurs des formulaires et même les cookies et headers HTTP.

    Contrôle strict des types et des formats : Imposer des contraintes strictes sur le format des données. Par exemple, si une valeur de select est censée être un entier entre 1 et 3, vérifiez cela explicitement avant d'utiliser la valeur.

## 5. Redirection ouverte (modif de l'url redirect d'insta)

### Explication de la vulnérabilité

Une redirection ouverte se produit lorsqu'un site web accepte une URL externe dans un paramètre (comme ici avec site=instagram) et redirige l'utilisateur vers cette URL sans vérifier sa validité. Cela peut être exploité par des attaquants pour rediriger les utilisateurs vers des sites malveillants, phishing, ou d'autres destinations dangereuses.

Dans votre exemple, l'URL est construite avec un paramètre site=instagram. Si la page index.php utilise ce paramètre pour rediriger les utilisateurs sans validation adéquate, cela pourrait être exploité ainsi :

```html
<a href="index.php?page=redirect&site=http://malicious-site.com" class="icon fa-instagram"></a>
```

Un utilisateur pourrait penser qu'il va être redirigé vers Instagram, mais au lieu de cela, il serait redirigé vers un site malveillant.

### Risques associés

    Phishing : Les attaquants peuvent rediriger les utilisateurs vers des pages de phishing qui ressemblent à des sites légitimes.
    Vol d'informations personnelles : Si les utilisateurs sont redirigés vers des sites malveillants, leurs informations sensibles (identifiants, mots de passe, données bancaires) peuvent être volées.
    Atteinte à la réputation : Si un site légitime est utilisé pour rediriger vers des sites dangereux, cela peut nuire à sa réputation.

### Comment corriger la faille

    Valider les URLs : Assurez-vous que seules des URLs autorisées peuvent être utilisées dans le paramètre site. Une solution consiste à utiliser une liste blanche (whitelist) de domaines vers lesquels la redirection est permise, comme dans cet exemple :

```php
$allowed_sites = ['instagram', 'facebook', 'twitter'];

if (in_array($_GET['site'], $allowed_sites)) {
    header("Location: https://www." . $_GET['site'] . ".com");
} else {
    // Afficher un message d'erreur ou rediriger vers une page par défaut
    echo "Site non autorisé";
}
```

Utiliser des redirections internes : Si possible, au lieu de rediriger vers des URLs externes directement, redirigez vers une page interne et gérez la redirection en interne sur le serveur.

Encodage et validation des paramètres : Utilisez l'encodage pour éviter les manipulations des paramètres URL, et validez rigoureusement toutes les entrées de l'utilisateur.

Informer les utilisateurs : Si vous devez absolument rediriger vers un site externe, informez les utilisateurs clairement où ils sont redirigés avant qu'ils ne quittent votre site.

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
