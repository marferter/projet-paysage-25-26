from gturtle import *
from math import atan, degrees, pi, sqrt

def soleil_a_lunettes(diametre, couleur_petits_rayons,
    couleur_grands_rayons, couleur_transition_soleil):
    setPenWidth(1)
    setPenColor('black')
    hideTurtle()

    def centre_soleil(diametre, couleur):
        penUp()
        setPenColor(couleur)
        dot(diametre)

    def triangle(cote1, cote2, couleur):
        angle = 180 - degrees(atan(cote2 / cote1))
        setFillColor(couleur)
        startPath()
        forward(cote1)
        right(angle)
        forward(sqrt(cote1 ** 2 + cote2 ** 2))
        right(180 - (angle - 90))
        forward(cote2)
        right(90)
        fillPath()

    def rayon_soleil(cote1, cote2, couleur):
        penDown()
        left(90)
        triangle(cote1, cote2, couleur)
        right(90)
        triangle(cote2, cote1, couleur)
        penUp()

    def rectangle(cote, couleur):
        setFillColor(couleur)
        startPath()
        for loop in range(2):
            forward(cote / 3)
            right(90)
            forward(cote)
            right(90)
        fillPath()

    def demi_cercle(cote, couleur):
        pas = pi * cote / 360
        setFillColor(couleur)
        startPath()
        for loop in range(360 // 2):
            forward(pas)
            right(360 / 360)
        right(90)
        fillPath()

    def branche_lunettes(longueur, epaisseur):
        setPenWidth(epaisseur)
        forward(longueur)

    def verre_lunettes(cote, couleur):
        rectangle(cote, couleur)
        right(270)
        back(cote)
        left(90)
        demi_cercle(cote, couleur)
        forward(cote)

    def lunettes(cote, couleur, epaisseur):
        penDown()
        angle_branche = 110
        setPenColor(couleur)
        right(angle_branche)
        branche_lunettes(cote / 2.5, epaisseur)
        left(angle_branche)
        verre_lunettes(cote, couleur)
        branche_lunettes(cote / 3, epaisseur)
        left(90)
        verre_lunettes(cote, couleur)
        left(angle_branche - 90)
        branche_lunettes(cote / 2.5, epaisseur)
        penUp()
    for loop in range(8):
        rayon_soleil(diametre * 2 / 5, diametre * 3.5 / 5,
            couleur_petits_rayons)
        right(360 / 16)
        rayon_soleil(diametre * 2 / 5, diametre * 4.18 / 5,
            couleur_grands_rayons)
        right(360 / 16)
    centre_soleil(diametre, 'orangered')
    centre_soleil(diametre - diametre * 0.1 / 5, 'darkorange')
    centre_soleil(diametre - diametre * 0.3 / 5, 'orange')
    centre_soleil(diametre - diametre * 0.7 / 5, couleur_transition_soleil)
    centre_soleil(diametre - diametre * 1.5 / 5, couleur_grands_rayons)
    angle_placement = 67.5
    left(angle_placement)
    forward(diametre / 2)
    right(angle_placement)
    lunettes(diametre * 3 / 10, 'black', diametre * 1 / 20)

if __name__ == '__main__':
    soleil_a_lunettes(100, "yellow", "gold", "darkOrange")

"""
soleil_a_lunettes(diametre, couleur_petits_rayons, couleur_grands_rayons,
                  couleur_transition_soleil)

Dessine un soleil avec des lunettes de soleil, composé de rayons
triangulaires alternés (petits et grands) autour d'un disque central
avec dégradé de couleur, surmonté d'une paire de lunettes.

Paramètres :
    diametre                 : diamètre du disque central du soleil
                               (en pixels). La longueur des rayons
                               est proportionnelle au diamètre
                               (petits : ~2/5 + 3.5/5, grands : ~2/5 + 4.18/5).
    couleur_petits_rayons    : couleur des rayons courts (alternés).
    couleur_grands_rayons    : couleur des rayons longs (alternés) et
                               du centre intérieur du soleil.
    couleur_transition_soleil: couleur intermédiaire du dégradé au centre
                               du soleil.

Position initiale de la tortue :
    La tortue part depuis la position par défaut (origine), au centre
    du soleil. Les rayons s'étendent depuis ce centre, puis la tortue
    revient au centre pour tracer les disques concentriques et les lunettes.
"""
