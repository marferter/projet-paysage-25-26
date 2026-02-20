from math import cos, tan, atan, radians, degrees
from gturtle import *


def eolienne(hauteur, couleur_base, couleur_helice, orientation):
    setPenWidth(1)
    setPenColor('black')
    hideTurtle()

    def pale(taille, couleur):
        penDown()
        petit_angle = degrees(atan(3 / 4))
        grand_angle = 90 - petit_angle
        setPenColor(couleur)
        setFillColor(couleur)
        startPath()
        forward(taille)
        right(180 - grand_angle)
        forward(0.6 * taille)
        right(90)
        forward(0.8 * taille)
        right(180 - petit_angle)
        fillPath()
        penUp()

    def helice(taille, couleur, orientation):
        setHeading(orientation)
        for _ in range(4):
            pale(taille, couleur)
            right(90)
    alpha = 5
    longueur_grand_cote = hauteur / cos(radians(5))
    longueur_petit_cote = tan(radians(5)) * hauteur
    right(5)
    setFillColor(couleur_base)
    startPath()
    forward(longueur_grand_cote)
    right(170)
    forward(longueur_grand_cote)
    right(95)
    forward(2 * longueur_petit_cote)
    fillPath()
    right(95)
    penUp()
    forward(longueur_grand_cote)
    helice(hauteur / 2, couleur_helice, orientation)
    setHeading(0)

if __name__ == '__main__':
    eolienne(100,'grey','lightGrey',100)



