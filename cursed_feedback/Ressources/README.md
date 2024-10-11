# Cursed Feedback

Comme indiqué dans le nom, ce flag est "buggé". Il se déclenche avec certaines lettres sans raison particulière. Par exemple, il suffit de taper la lettre `e` pour déclencher le flag. De même, des mots comme `script` fonctionnent aussi, ce qui rend difficile de ne **pas** déclencher le flag.

Ce comportement anormal indique une mauvaise gestion des entrées dans le formulaire de feedback, probablement en raison d'une absence de validation ou d'une logique incorrecte dans le code côté serveur.

# Patch

Pour sécuriser le feedback et empêcher ces déclenchements involontaires, il est essentiel de :

1. **Vérifier le contenu des entrées :** Implémenter une validation stricte des entrées utilisateur. Cela inclut la vérification du type de contenu (texte, chiffres, etc.) et l'utilisation d'expressions régulières pour ne permettre que des caractères autorisés.

2. **Échapper correctement les caractères spéciaux :** Il est crucial d'échapper tout caractère potentiellement dangereux (comme `<`, `>`, ou `"`) pour éviter tout risque d'injection, que ce soit du HTML ou du JavaScript.

3. **Limiter les caractères acceptés :** Restreindre le type de caractères que le champ de feedback peut accepter. Par exemple, interdire les balises HTML et autres chaînes susceptibles de provoquer des comportements indésirables.

4. **Mettre en place des tests automatisés :** Tester régulièrement les entrées et les réponses du système avec différentes combinaisons de caractères afin d'assurer que le comportement attendu est respecté et qu'aucune vulnérabilité n'a été introduite.

Avec ces mesures, la logique du formulaire de feedback sera sécurisée, et les flags ne seront plus déclenchés de manière aléatoire ou involontaire.
