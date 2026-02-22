from gturtle import *
from math import sqrt


def dameuse(longueur, couleur_1, couleur_2, couleur_6):
    setPenWidth(2)
    setPenColor('black')
    hideTurtle()

    def cabine(longueur, largeur, couleur_1):
        penDown()
        setPenColor(couleur_1)
        setFillColor(couleur_1)
        startPath()
        for loop in range(2):
            forward(longueur)
            right(90)
            forward(largeur)
            right(90)
        fillPath()
        penUp()

    def deplacement_1(longueur, largeur):
        forward(longueur / 2.5)
        right(90)
        forward(largeur / 2.85)

    def vitre(longeur, largeur, couleur, cathete_1):
        hypothenuse = sqrt(cathete_1 ** 2 + largeur ** 2)
        penDown()
        setPenColor(couleur_2)
        setFillColor(couleur_2)
        startPath()
        for loop in range(2):
            forward(largeur)
            left(90)
            forward(longeur)
            left(90)
        right(36.87)
        forward(hypothenuse)
        left(126.87)
        forward(cathete_1)
        fillPath()
        penUp()

    def deplacement_2(longueur, hauteur, couleur_2):
        left(90)
        forward(longueur)
        right(90)
        forward(hauteur)
        left(90)
        setPenColor(couleur_2)
        penDown()

    def cache_moteur(longueur, largeur, couleur_2, cathete_1):
        hypothenuse = sqrt(cathete_1 ** 2 + largeur ** 2)
        setFillColor(couleur_1)
        startPath()
        for loop in range(2):
            forward(longueur)
            left(90)
            forward(largeur)
            left(90)
        penUp()
        forward(longueur)
        left(90)
        right(36.87)
        forward(hypothenuse)
        left(126.87)
        forward(cathete_1)
        fillPath()
        penUp()
        fillPath()

    def deplacement_3(largeur, longueur, width):
        penDown()
        setPenColor('black')
        setPenWidth(width)
        backward(largeur)
        forward(longueur)
        backward(longueur)

    def fraise_lisseur(D_fraise, longueur_lisseur, couleur_3, couleur_4,
        width, x, y):
        setPenColor('black')
        right(180)
        setPenWidth(width)
        forward(x)
        left(45)
        forward(y)
        right(45)
        setPenColor(couleur_3)
        setPenWidth(1)
        dot(D_fraise)
        left(90)
        forward(D_fraise / 2.2)
        right(90)
        setPenWidth(width)
        setPenColor(couleur_4)
        forward(longueur_lisseur)
        setPenColor('black')

    def deplacement_4(deplacement):
        penUp()
        backward(deplacement)

    def rectangle(longueur, diametre, width):
        setPenWidth(width)
        penDown()
        for loop in range(2):
            forward(longueur)
            right(90)
            penUp()
            forward(diametre)
            right(90)
            penDown()

    def demi_arc_de_cerle(diametre):
        pas = diametre / 115
        for loop in range(180):
            forward(pas)
            left(180 / 180)

    def chenille(longueur, largeur, diametre, width):
        rectangle(longueur, largeur, width)
        right(180)
        demi_arc_de_cerle(diametre)
        penUp()
        forward(longueur)
        penDown()
        demi_arc_de_cerle(diametre)
        penUp()

    def roue(deplacement, D_roue, espace):
        penUp()
        right(270)
        forward(deplacement)
        right(90)
        for loop in range(5):
            dot(D_roue)
            forward(espace)

    def chenille_entiere(longueur, largeur, deplacement, D_roue, espace,
        diametre, width):
        chenille(longueur, largeur, diametre, width)
        roue(deplacement, D_roue, espace)

    def pelle(longueur, largeur, couleur_5, cathete_1, deplacement,
        L_rectangle, x, L_piston_1, L_piston_2, y, width):
        hypothenuse = sqrt(cathete_1 ** 2 + largeur ** 2)
        setPenWidth(1)
        backward(deplacement)
        right(90)
        forward(cathete_1)
        left(180)
        setPenColor(couleur_5)
        setFillColor(couleur_5)
        startPath()
        for loop in range(2):
            forward(longueur)
            right(90)
            forward(largeur)
            right(90)
        forward(L_rectangle)
        right(126.87)
        forward(hypothenuse)
        right(36.87)
        penUp()
        fillPath()
        setPenWidth(width)
        right(110)
        forward(x)
        penDown()
        forward(L_piston_1)
        backward(L_piston_1)
        left(90)
        forward(y)
        right(105)
        forward(L_piston_2)

    def deplacement_5(hauteur, largeur):
        penUp()
        right(75)
        forward(hauteur)
        left(90)
        forward(largeur)

    def gyrophare(hauteur, couleur_6):
        setPenWidth(1)
        penDown()
        setPenColor(couleur_6)
        setFillColor(couleur_6)
        startPath()
        for loop in range(4):
            forward(hauteur)
            right(90)
        fillPath()
        right(90)
        forward(hauteur)
        left(90)
        forward(hauteur / 2)
        dot(hauteur + 1)
    cabine(longueur / 2, longueur / (8 / 3), couleur_1)
    deplacement_1(longueur / (8 / 3), longueur / 2)
    vitre(longueur / 4, longueur / (16 / 3), couleur_2, longueur / (64 / 9))
    deplacement_2(longueur / (400 / 145), longueur / (80 / 3), couleur_1)
    cache_moteur(longueur / 4, longueur / (16 / 3), couleur_1, longueur / (
        64 / 9))
    deplacement_3(longueur / (8 / 3), longueur, longueur / 80)
    fraise_lisseur(longueur / 8, longueur / 6.5, 'red', 'yellow', longueur /
        (400 / 7), longueur / 20, longueur / (40 / 9))
    deplacement_4(longueur / (80 / 111))
    chenille_entiere(longueur, longueur / (16 / 3), longueur / (119 / 11), 
        longueur / (200 / 33), longueur / 4, longueur / (16 / 3), longueur /
        (200 / 3))
    pelle(longueur / (20 / 3), longueur / (32 / 3), 'black', longueur / 10,
        longueur / (40 / 3), longueur / (40 / 9), longueur / 40, longueur /
        (400 / 70), longueur / (200 / 33), longueur / 10, longueur / (200 / 3))
    deplacement_5(longueur / (80 / 49), longueur / 4)
    left(4)
    gyrophare(longueur / (80 / 3), couleur_6)


if __name__ == '__main__':
    dameuse(100, 'green', 'blue', 'red')

"""
dameuse(longueur, couleur_1, couleur_2, couleur_6)

Dessine une dameuse (engin de damage des pistes de ski) vue de côté,
avec sa cabine, sa vitre, son cache-moteur, sa chenille, sa fraise
de damage, sa pelle et son gyrophare.

Paramètres :
    longueur  : longueur totale de la dameuse (en pixels).
                C'est la dimension de référence ; toutes les autres
                proportions (hauteur de la cabine, taille de la fraise,
                diamètre des roues, longueur de la chenille, etc.)
                en sont dérivées.
    couleur_1 : couleur principale du corps de la dameuse (cabine et
                cache-moteur).
    couleur_2 : couleur de la vitre/pare-brise de la cabine.
    couleur_6 : couleur du gyrophare situé sur le toit de la cabine.

Position initiale de la tortue :
    La tortue part depuis la position par défaut (origine), au coin
    inférieur gauche de la cabine, orientée vers le haut (nord).
"""
