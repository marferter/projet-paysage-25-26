from gturtle import *
from math import atan, degrees

def moulin(largeur, angle, couleur_toit, couleur_pan, couleur_fenetre,
    couleur_bat, couleur_porte):
    setPenWidth(1)
    setPenColor('black')
    hideTurtle()

    def toit(couleur_toit, largeur):
        penDown()
        right(90)
        setFillColor(couleur_toit)
        startPath()
        for _ in range(3):
            forward(largeur)
            left(120)
        left(90)
        fillPath()
        penUp()

    def pan(couleur_pan, largeur):
        angle = 360 / 12
        setFillColor(couleur_pan)
        startPath()
        penDown()
        for _ in range(4):
            right(angle)
            forward(largeur * 1.5)
            right(90 + angle / 2)
            forward(largeur * 0.78)
            right(90 + angle / 2)
            forward(largeur * 1.5)
            left(180 - angle)
        fillPath()
        penUp()

    def fenetre(couleur_fenetre, largeur):
        penDown()
        setPenColor(couleur_fenetre)
        dot(largeur / 2)
        penUp()

    def batiment(couleur_bat, largeur):
        gamma = atan(0.3 * largeur / (2.5 * largeur))
        alpha = degrees(gamma)
        longueur = sqrt((0.3 * largeur) ** 2 + (2.5 * largeur) ** 2)
        setFillColor(couleur_bat)
        startPath()
        left(180 - alpha)
        forward(longueur)
        left(90 + alpha)
        forward(largeur * 1.6)
        left(90 + alpha)
        forward(longueur)
        left(90 - alpha)
        forward(largeur)
        fillPath()

    def porte(couleur_porte, largeur):
        setFillColor(couleur_porte)
        startPath()
        penDown()
        for _ in range(2):
            forward(largeur)
            right(90)
            forward(largeur * 0.5)
            right(90)
        fillPath()
        penUp()

    gamma = atan(0.3 * largeur / (2.5 * largeur))
    alpha = degrees(gamma)
    longueur = sqrt((0.3 * largeur) ** 2 + (2.5 * largeur) ** 2)
    left(180 - alpha)
    forward(-longueur)
    setHeading(0)
    hauteura = sqrt(largeur ** 2 - (largeur / 2) ** 2) / 2.5
    hauteurb = sqrt((2.5 * largeur) ** 2 - (0.3 * largeur) ** 2)
    toit(couleur_toit, largeur)
    batiment(couleur_bat, largeur)
    right(180)
    
    forward(largeur / 2)
    left(90)
    forward(hauteura)
    back(hauteura + largeur / 2)
    fenetre(couleur_fenetre, largeur)
    forward(hauteura + largeur / 2)
    setHeading(angle)
    pan(couleur_pan, largeur)
    setHeading(0)
    
    back(hauteura + largeur / 2)
    back(hauteurb - largeur / 2)
    left(90)
    forward(largeur * 0.2)
    right(90)
    penDown()
    porte(couleur_porte, largeur)


if __name__ == '__main__':
    moulin(100, 60, 'red', 'grey', 'lightBlue', 'gold', 'brown')

