from gturtle import *


def montgolfiere(diametre_ballon, couleur_panier, couleur_ballon, couleur_sac):
    setPenWidth(2)
    setPenColor('black')
    hideTurtle()
    largeur_panier = diametre_ballon / 4
    longueur_corde = diametre_ballon / 3

    def panier(largeur_panier, couleur_panier):
        for loop in range(2):
            setPenColor(couleur_panier)
            setFillColor(couleur_panier)
            startPath()
            forward(largeur_panier)
            right(90)
            forward(2 * largeur_panier)
            right(90)
            fillPath()

    def faisceau_corde_gauche(longueur_corde):
        penDown()
        setPenColor('black')
        left(25)
        forward(longueur_corde)
        back(longueur_corde)
        right(25 + 90)
        penUp()

    def faisceau_corde_droite(longueur_corde):
        setPenColor('black')
        penDown()
        left(65)
        forward(longueur_corde)
        back(longueur_corde)
        right(65 + 90)
        penUp()

    def faisceau_corde_centre(longueur_corde):
        penDown()
        left(90)
        forward(longueur_corde * 0.9063)
        back(longueur_corde * 0.9063)
        right(90)
        penUp()

    def sac_montgolfiere(couleur_sac):
        forward(largeur_panier / 2)
        right(90)
        forward(largeur_panier / 4)
        left(90)
        penDown()
        setPenColor(couleur_sac)
        setFillColor(couleur_sac)
        startPath()
        forward(largeur_panier / 4)
        right(90)
        for loop in range(3):
            forward(largeur_panier / 2)
            right(90)
        forward(largeur_panier / 4)
        fillPath()
        penUp()

    def sac_montgolfiere_deux(couleur_sac):
        right(90)
        forward(largeur_panier)
        left(90)
        penDown()
        setPenColor(couleur_sac)
        setFillColor(couleur_sac)
        startPath()
        forward(largeur_panier / 4)
        right(90)
        for loop in range(3):
            forward(largeur_panier / 2)
            right(90)
        forward(largeur_panier / 4)
        fillPath()
        penUp()
    panier(largeur_panier, couleur_panier)
    sac_montgolfiere(couleur_sac)
    sac_montgolfiere_deux(couleur_sac)
    left(90)
    forward(diametre_ballon / 3.2)
    right(90)
    forward(largeur_panier / 2)
    faisceau_corde_gauche(longueur_corde)
    forward(largeur_panier)
    faisceau_corde_centre(longueur_corde)
    forward(largeur_panier)
    faisceau_corde_droite(longueur_corde)
    forward(largeur_panier)
    right(90)
    forward(2 * largeur_panier)
    right(90)
    forward(largeur_panier)
    right(90)
    forward(largeur_panier)
    left(90)
    forward(longueur_corde * 0.9063 * 2)
    setPenColor(couleur_ballon)
    dot(diametre_ballon)

if __name__ == '__main__':
    montgolfiere(100, 'brown', 'red', 'beige')

"""
montgolfiere(diametre_ballon, couleur_panier, couleur_ballon, couleur_sac)

Dessine une montgolfière vue de face, composée d'un panier rectangulaire
(nacelle), d'un brûleur (sac), de cordages en faisceau et d'un ballon
circulaire.

Paramètres :
    diametre_ballon : diamètre du ballon (en pixels).
                      Le panier a une largeur de 1/4 du diamètre et les
                      cordages une longueur de 1/3 du diamètre.
    couleur_panier  : couleur du panier (nacelle).
    couleur_ballon  : couleur du ballon.
    couleur_sac     : couleur du brûleur / sac à gaz relié au ballon.

Position initiale de la tortue :
    La tortue part depuis la position par défaut (origine), au coin
    inférieur gauche du panier, orientée vers le haut (nord).
    Le dessin commence par le panier, puis remonte vers le ballon.
"""
