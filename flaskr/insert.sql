INSERT INTO gear (name, desc, img) VALUES
("cylindriques à denture droite", "", "b074cca3f97f8b5d56083c3561aad95c.jpg" ),
("cylindriques à denture hélicoïdale", "", "engrenage_hélicoïdale_cannelée_long-768x1024.jpg"),
("coniques", "", "pignon_droit_avec_entrée_de_dent-1024x768.jpg"),
("roue et vis sans fin", "", "roue_a_vis_en_cours_de-taillage-1024x768.jpg");

INSERT INTO argument (type, content) VALUES
(0, "Simple et économique"),
(0, "Pas d’efforts axiaux"),
(0, "Transmission plus souple et moins bruyante"),
(0, "Transmission d’efforts et de vitesses plus importants"),
(0,"Possibilités d’entraxes infinis"), 
(0, "Possibilité de choisir le sens de rotation de la roue menée"),
(0, "Arbres quelconques (Très souvent orthogonaux)"),
(0, "Rapport de réduction élevés"),
(1, "Vitesses de rotation limitées"),
(1, "Bruyant"),
(1, "Entraxes prenant des valeurs finies"),
(1, "Effort axial supplémentaire"),
(1, "Solution moins économique"),
(1, "Rendement moins bon"),
(1, "Solution moins économique"),
(1, "Nécessité d’un réglage des roues au montage"),
(1, "Rendement faible"),
(1, "Parfois non réversible (peut être un avantage)");


INSERT INTO gear_arg (id_gear, id_arg) VALUES
(1, 1),
(1, 2),
(1, 9),
(1, 10),
(1, 11),
(2, 3),
(2, 4),
(2, 5),
(2, 13),
(2, 14),
(3, 19 ),
(3, 6),
(3, 13 ),
(3, 16),
(4, 7 ),
(4, 8 ),
(4, 17),
(4, 18);
