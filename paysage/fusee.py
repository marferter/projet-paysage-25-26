from gturtle import *
from math import atan, degrees
from math import sqrt


def fusee(taille, couleur_base, couleur_aile, rapport_feu, couleur_feu):
    setPenWidth(2)
    setPenColor('black')
    hideTurtle()
    petite_base = taille
    grande_base = taille * 4
    largeur_rectangle = taille * 2
    longueur_rectangle = taille * 3.3333333
    base_triangle = taille * 1.66666666
    hauteur_trapeze = taille * 1.3333333
    hauteur_trapeze2 = taille * 0.666666666
    diametre_fenetre = taille * 1.2
    longueur_feu = rapport_feu * taille
    epaisseur_feu = grande_base / 3

    def trapeze(petite_base, grande_base, hauteur):
        alpha = degrees(atan(3 / 4))
        beta = 90 - alpha
        mini_cote = (grande_base - petite_base) / 2
        hypothenuse = sqrt(mini_cote ** 2 + hauteur ** 2)
        penDown()
        right(alpha)
        forward(hypothenuse)
        right(beta)
        forward(petite_base)
        right(beta)
        forward(hypothenuse)
        right(alpha + 90)
        forward(petite_base + 2 * mini_cote)
        right(90 + alpha)
        forward(hypothenuse)
        left(alpha)
        penUp()

    def rectangle(petite_base, longueur_rectangle, couleur):
        penDown()
        setFillColor(couleur)
        startPath()
        for _ in range(2):
            forward(longueur_rectangle)
            right(90)
            forward(petite_base)
            right(90)
        fillPath()
        penUp()

    def triangle(base):
        angle1 = 26.6
        angle2 = 63.4
        demi_base = base / 2
        hypotenuse = sqrt(demi_base ** 2 + base ** 2)
        penDown()
        right(angle1)
        forward(hypotenuse)
        right(180 - 2 * angle1)
        forward(hypotenuse)
        right(180 - angle2)
        forward(base)
        penUp()

    def fenetre(diametre, couleur):
        penDown()
        setPenColor(couleur)
        dot(diametre)

    def feu(largeur, longueur, couleur):
        penDown()
        setPenColor(couleur)
        setPenWidth(taille)
        forward(longueur)
        back(longueur)
        setPenWidth(1)
        setPenColor('black')
    right(180)
    feu(taille, longueur_feu, couleur_feu)
    right(90)
    forward(grande_base / 2)
    right(90)
    setFillColor(couleur_base)
    startPath()
    trapeze(largeur_rectangle, grande_base, hauteur_trapeze)
    fillPath()
    rectangle(largeur_rectangle, longueur_rectangle, 'light blue')
    forward(longueur_rectangle / 4)
    left(90)
    setFillColor(couleur_aile)
    startPath()
    triangle(base_triangle)
    fillPath()
    forward(longueur_rectangle / 4)
    left(90)
    forward(largeur_rectangle)
    left(90)
    forward(longueur_rectangle)
    left(180)
    forward(longueur_rectangle / 4)
    left(90)
    setFillColor(couleur_aile)
    startPath()
    triangle(base_triangle)
    fillPath()
    forward(longueur_rectangle / 4)
    left(90)
    forward(largeur_rectangle)
    right(90)
    setFillColor(couleur_base)
    startPath()
    trapeze(petite_base, largeur_rectangle, hauteur_trapeze2)
    fillPath()
    setFillColor(couleur_aile)
    startPath()
    triangle(petite_base)
    fillPath()
    left(180)
    forward(petite_base / 2)
    right(90)
    forward(largeur_rectangle)
    fenetre(diametre_fenetre, 'white')


if __name__ == '__main__':
    fusee(50, 'grey', 'blue', 1, 'orange')