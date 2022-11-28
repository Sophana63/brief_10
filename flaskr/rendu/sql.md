Dans la database flsakr.sql nous créons 5 tables : 

-user, contient :
    

-post

-gear, contient : 
    . les id sous forme de INTEGER PRIMARY KEY AUTOINCREMENT,
    . les noms des engrenages (= name) sous forme de VARCHAR(32),
    . une description (= desc), elle est vide pour le moment mai speut être implémentée, sous forme de TEXT,
    . les images (= img ), on utilise le nom de l'image rangé dans le dossier assets/ images sous forme de  VARCHAR(64)

-argument, conyient :
    . les id sous forme d'INTEGER PRIMARY KEY AUTOINCREMENT,
    . les types BOOLEAN,
  content VARCHAR(32)