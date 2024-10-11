# Faille liée à l'Origine et à l'User-Agent

Dans ce challenge de CTF, la vulnérabilité repose sur une vérification des en-têtes HTTP envoyés par le client. Le site impose deux conditions spécifiques pour accéder à certaines fonctionnalités :

- L'origine de la requête doit provenir de **`https://www.nsa.gov/`**.
- Le navigateur utilisé doit avoir comme **`User-Agent`** "ft_bornToSec".

Ces conditions sont visibles dans le code source de la page, mais ne sont pas contrôlées côté serveur de manière sécurisée. Nous pouvons donc les contourner en manipulant les en-têtes HTTP.

## Détails de l'attaque

### Extrait du code source de la page

```html
<!-- Extrait du code source -->
You must come from : "https://www.nsa.gov/".
...
Let's use this browser : "ft_bornToSec". It will help you a lot.
```

Ce texte suggère que le site vérifie les en-têtes HTTP `Referer` et `User-Agent`. Nous pouvons donc manipuler ces en-têtes pour contourner la protection.

## Exploitation

### Méthode 1 : Utilisation de `curl`

Nous pouvons utiliser l'outil en ligne de commande `curl` pour manipuler les en-têtes HTTP et satisfaire les conditions imposées par le serveur. Voici la commande pour réaliser cela :

```bash
curl -H "Referer: https://www.nsa.gov/" -H "User-Agent: ft_bornToSec" 'http://10.11.249.37/?page=login#'
```

#### Explication de la commande

- **`-H "Referer: https://www.nsa.gov/"`** : Ce paramètre permet de définir l'en-tête `Referer` afin de simuler une provenance depuis le site de la NSA.
- **`-H "User-Agent: ft_bornToSec"`** : Cet en-tête simule un navigateur avec l'User-Agent "ft_bornToSec", comme demandé dans le code source de la page.
- **`'http://10.11.249.37/?page=login#'`** : L'URL cible où les en-têtes doivent être envoyés.

Cette méthode fonctionne, car le serveur ne vérifie pas réellement la provenance ou le type de navigateur, mais se fie aux en-têtes envoyés par le client.

### Méthode 2 : Utilisation de la console du navigateur

Une autre méthode consiste à utiliser la console JavaScript du navigateur pour modifier l'en-tête `Referer` ou `User-Agent` de manière dynamique. Cependant, cette approche peut être limitée en fonction des restrictions imposées par les navigateurs modernes. Voici un exemple de script qui pourrait être exécuté dans la console du navigateur pour modifier l'User-Agent :

```javascript
Object.defineProperty(navigator, 'userAgent', {
    get: function () { return "ft_bornToSec"; }
});
```

Cela pourrait fonctionner pour modifier temporairement l'User-Agent, mais la modification de l'en-tête `Referer` n'est généralement pas autorisée via JavaScript pour des raisons de sécurité.

### Méthode 3 : Utilisation d'une extension Firefox

Finalement, l'utilisation d'une extension pour manipuler les en-têtes HTTP est une approche simple et efficace. Une extension comme **"Modify Header Value"** ou **"Tamper Data"** dans Firefox permet de modifier les en-têtes envoyés lors des requêtes HTTP.

#### Étapes pour utiliser une extension

1. Installer une extension de modification d'en-têtes HTTP dans Firefox (par exemple, **"Modify Header Value"**).
2. Configurer l'extension pour ajouter ou modifier les en-têtes suivants lors des requêtes vers le site cible :
   - **Referer** : `https://www.nsa.gov/`
   - **User-Agent** : `ft_bornToSec`
3. Charger la page cible après avoir activé ces en-têtes dans l'extension.

Cette méthode a l'avantage d'être facile à utiliser sans avoir à manipuler le terminal ou la console du navigateur.

## Conclusion

Cette vulnérabilité exploite la confiance du serveur envers les en-têtes HTTP `Referer` et `User-Agent` fournis par le client. En manipulant ces en-têtes via `curl`, la console du navigateur, ou une extension Firefox, nous pouvons contourner la protection et accéder aux fonctionnalités restreintes du site. Cela montre l'importance de ne pas se fier uniquement aux informations envoyées par le client pour des contrôles critiques de sécurité.
