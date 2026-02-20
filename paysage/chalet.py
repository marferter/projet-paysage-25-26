from gturtle import *

def chalet(base_chalet, couleur_toit, couleur_facade,couleur_fenetre):
    setPenWidth(1)
    setPenColor('black')
    hideTurtle()

    def rectangle(base, hauteur, couleur):
        penDown()
        setFillColor(couleur)
        startPath()
        for _ in range(2):
            forward(hauteur)
            right(90)
            forward(base)
            right(90)
        fillPath()
        penUp()

    def demi_carre(base, couleur):
        cote = sqrt(base ** 2 / 2)
        penDown()
        setFillColor(couleur)
        startPath()
        right(45)
        forward(cote)
        right(90)
        forward(cote)
        right(135)
        forward(base)
        penUp()
        fillPath()
    hauteur_chalet = base_chalet * 3 / 5
    cote_fenetre = base_chalet * 1 / 5
    base_porte = cote_fenetre
    hauteur_porte = base_porte * 2
    base_toit = base_chalet * 12 / 10
    rectangle(base_chalet, hauteur_chalet, couleur_facade)
    forward(hauteur_chalet * 1 / 3)
    right(90)
    forward(base_chalet * 1 / 5)
    left(90)
    rectangle(cote_fenetre, cote_fenetre, couleur_fenetre)
    back(hauteur_chalet * 1 / 3)
    right(90)
    back(base_chalet * 1 / 5)
    forward(base_chalet * 3 / 5)
    left(90)
    rectangle(base_porte, hauteur_porte, 'brown')
    right(90)
    back(base_chalet * 3 / 5)
    left(90)
    forward(hauteur_chalet)
    left(90)
    forward(base_chalet * 1 / 10)
    right(90)
    demi_carre(base_toit, couleur_toit)

if __name__ == '__main__':
    chalet(100, 'darkRed', 'olive', 'lightBlue')

