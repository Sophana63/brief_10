Dans la database flsakr.sql nous créons 5 tables : 

-user, contient :
    .les id sous forme d'INTEGER PRIMARY KEY AUTOINCREMENT,
    .les username sous forme de TEXT UNIQUE NOT NULL,
    .et les password  sous forme de TEXT NOT NULL

-post, contient :
    .les id sous forme d'INTEGER PRIMARY KEY AUTOINCREMENT,
    .les author_id sous forme d'INTEGER NOT NULL en tant que clé étrangère, il correspondent aux id de la table user(cf*),
    ."created" correspond à la date de création de l'article sous forme de TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    . les title sous forme de TEXT NOT NULL,
    . le corps de texte (=body) sous forme de TEXT NOT NULL,

-gear, contient : 
    . les id sous forme de INTEGER PRIMARY KEY AUTOINCREMENT,
    . les noms des engrenages (= name) sous forme de VARCHAR(32),
    . une description (= desc), elle est vide pour le moment mai speut être implémentée, sous forme de TEXT,
    . les images (= img ), on utilise le nom de l'image rangé dans le dossier assets/ images sous forme de  VARCHAR(64)

-argument, contient :
    . les id sous forme d'INTEGER PRIMARY KEY AUTOINCREMENT,
      . les types sout forme de BOOLEAN, 0 correspond à un avantage et 1 à un inconvénient,
    . la description de l'avantage ou de l'inconvénient (= content) sous forme de VARCHAR(32)


Une table de liaison 'gear_arg ' lie gear et argument via gear(id) et argument(id), vous pouvez voir cette liaison via le mcd ci dessous : 

![fig 1 image du MCD](https://github.com/Sophana63/brief_10/blob/Charlie/flaskr/rendu/images/sch%C3%A9ma%20db%20engrenages.png)

* La table post utlise la colonne author_id pour prendre des informations de la table user via leurs id afin de savoir qui est le créateur pour chaque article de blog. 