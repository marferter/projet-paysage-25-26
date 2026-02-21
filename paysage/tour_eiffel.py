from math import pi
from gturtle import *

def tour_eiffel(Base, couleur_lumiere, couleur):
    setPenWidth(2)
    setPenColor('black')
    hideTurtle()

    def arc_de_cercle(diametre, couleur):
        penDown()
        setFillColor(couleur)
        startPath()
        perimetre = diametre / 2 * 2 * pi
        un_degre = perimetre / 360
        for loop in range(180):
            forward(un_degre)
            right(1)

    def trapeze1(base):
        penDown()
        hypothenuse = sqrt((base / 4) ** 2 + (base / 2 + base / 6) ** 2)
        left(90)
        forward(base / 4)
        left(180 - 70)
        forward(hypothenuse)
        left(180 - 110)
        forward(base)
        left(180 - 110)
        forward(hypothenuse)
        left(180 - 70)
        forward(base / 4)
        fillPath()
        penUp()
        back(base / 4)
        left(70)
        forward(hypothenuse)
        left(20)

    def rectangle(longueur, couleur):
        penDown()
        setFillColor(couleur)
        startPath()
        largeur = longueur // 10
        for loop in range(2):
            forward(largeur)
            right(90)
            forward(longueur)
            right(90)
        fillPath()
        penUp()
        forward(largeur)

    def barrieres(Base, couleur):
        startPath()
        base = Base / 10 * 8
        hauteur = Base // 10
        cote = sqrt(hauteur ** 2 + (Base // 10) ** 2)
        fillPath()
        penUp()
        right(90)
        forward((Base - base) / 2)
        penDown()
        setFillColor(couleur)
        startPath()
        forward(base)
        left(45)
        forward(cote)
        left(180 - 45)
        forward(Base)
        left(180 - 45)
        forward(cote)
        fillPath()
        penUp()
        back(cote)
        left(135)

    def trapeze2(Base, couleur):
        penDown()
        Base_trapeze = Base - 2 * Base / 10
        base = Base_trapeze / 10 * 2
        hauteur = Base_trapeze * 2
        hypothenuse = sqrt((Base_trapeze / 10) ** 2 + hauteur ** 2)
        penUp()
        right(90)
        forward(Base / 10)
        left(90)
        penDown()
        setFillColor(couleur)
        startPath()
        right(90 - 78.5)
        forward(hypothenuse)
        right(180 - 101.5)
        forward(base)
        right(180 - 101.5)
        forward(hypothenuse)
        right(180 - 78.5)
        forward(Base_trapeze)
        fillPath()
        penUp()
        right(180 - 78.5)
        forward(hypothenuse)
        left(90 - 78.5)

    def socle_pointe(Base, couleur):
        penDown()
        setFillColor(couleur)
        startPath()
        Base_trapeze = Base - 2 * Base / 10
        base = Base_trapeze / 10 * 2
        hauteur = base / 3 * 4
        left(45)
        for loop in range(2):
            forward(hauteur // 8)
            right(45)
            forward(hauteur - hauteur // 4)
            right(45)
            forward(hauteur // 8)
            right(45)
            forward(base)
            right(45)
        fillPath()
        penUp()
        forward(hauteur // 8)
        right(45)
        forward(hauteur - hauteur // 4)
        right(45)
        forward(hauteur // 8)
        left(45)

    def pointe(Base, couleur):
        penDown()
        setFillColor(couleur)
        startPath()
        Base_trapeze = Base - 2 * Base / 10
        Base = Base_trapeze / 10 * 2
        hauteur = Base / 3 * 4
        base1 = hauteur - hauteur // 4
        hauteur1 = base1 * 2
        hypothenuse = sqrt(base1 ** 2)
        right(90 - 60)
        forward(hypothenuse)
        right(180 - 60)
        forward(hypothenuse)
        right(180 - 60)
        forward(base1)
        fillPath()
        penUp()
        right(90 + 30)
        forward(hypothenuse)
        left(30)

    def lumiere(couleur_lumiere, Base):
        penDown()
        diametre = Base // 10
        setPenColor(couleur_lumiere)
        dot(diametre)
        penUp()
    arc_de_cercle(Base, couleur)
    trapeze1(Base)
    rectangle(Base, couleur)
    barrieres(Base, couleur)
    trapeze2(Base, couleur)
    socle_pointe(Base, couleur)
    pointe(Base, couleur)
    lumiere(couleur_lumiere, Base)


if __name__ == '__main__':
    tour_eiffel(100, 'yellow', 'grey')

"""
tour_eiffel(Base, couleur_lumiere, couleur)

Dessine la Tour Eiffel vue de face, composée d'un arc de cercle formant
les pieds, d'un grand trapèze, d'une plateforme rectangulaire, de
barrières inclinées, d'un second trapèze, d'un socle de flèche et d'une
pointe, avec une lumière au sommet.

Paramètres :
    Base            : largeur de la base de la Tour Eiffel (en pixels).
                      Toutes les hauteurs et largeurs des différentes
                      sections (trapèzes, rectangle de plateforme,
                      barrières, flèche) sont calculées proportionnellement
                      à cette valeur.
    couleur_lumiere : couleur de la lumière (point lumineux) au sommet
                      de la tour.
    couleur         : couleur de la structure de la tour (piliers,
                      trapèzes, plateforme, pointe).

Position initiale de la tortue :
    La tortue part depuis la position par défaut (origine), au centre
    de la base de la Tour Eiffel (entre les deux pieds), orientée vers
    le haut (nord). Le premier élément dessiné est l'arc de cercle
    formant les pieds de la tour.
"""
