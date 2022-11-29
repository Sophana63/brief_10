INSERT INTO user (username, password)
VALUES
  ('test', 'pbkdf2:sha256:50000$TCI4GzcX$0de171a4f4dac32e3364c7ddc7c14f3e2fa61f2d17574483f7ffbb431b4acb2f'),
  ('other', 'pbkdf2:sha256:50000$kJPKsz6N$d2d4784f1b030a9761f5ccaeeaca413f27f2ecb76d6168407af962ddce849f79');

INSERT INTO post (title, body, author_id, created)
VALUES
  ('test title', 'test' || x'0a' || 'body', 1, '2018-01-01 00:00:00');

INSERT INTO gear (name, desc, img) VALUES
("cylindriques à denture droite", "test 1", "b074cca3f97f8b5d56083c3561aad95c.jpg" ),
("gearTest", "test 2", "engrenage_hélicoïdale_cannelée_long-768x1024.jpg");

INSERT INTO argument (type, content) VALUES
(1, "Simple et économique"),
(2, "Pas d’efforts axiaux");

INSERT INTO gear_arg VALUES
(1, 1),
(1, 2);

