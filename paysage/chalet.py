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

"""
chalet(base_chalet, couleur_toit, couleur_facade, couleur_fenetre)

Dessine un chalet de montagne vu de face, avec une façade rectangulaire,
une fenêtre carrée, une porte en bois et un toit en demi-carré (45°).

Paramètres :
    base_chalet     : largeur de la façade du chalet (en pixels).
                      La hauteur de la façade (3/5 de la base), la taille
                      de la fenêtre (1/5 de la base), la taille de la porte
                      et la base du toit (12/10 de la base) en découlent.
    couleur_toit    : couleur du toit triangulaire.
    couleur_facade  : couleur des murs de la façade.
    couleur_fenetre : couleur de la fenêtre carrée.

Position initiale de la tortue :
    La tortue part depuis la position par défaut (origine), au coin
    inférieur gauche de la façade, orientée vers le haut (nord).
"""
