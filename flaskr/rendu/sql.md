Dans la database flsakr.sql nous créons 5 tables : 

-user, contient :
    . les id  sous forme d'INTEGER PRIMARY KEY AUTOINCREMENT,
    . les username  sous forme de TEXT il doivent être UNIQUE NOT NULL,
    . les password sous forme deTEXT NOT NULL

-post, contient : 
    . les id sous forme d'INTEGER PRIMARY KEY AUTOINCREMENT,
    . les author_id sous forme d'INTEGER NOT NULL,
    . les dates de parution (= created) sous forme de TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    . le title sous forme de TEXT NOT NULL,
    . le corps de texte (=body) sous forme de TEXT NOT NULL,
    . la clé étrangère (=FOREIGN KEY), elle lie author_id à user (id)

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

![fig 1 image du MCD](flaskr/rendu/images/schéma db engrenages.png)