from gturtle import *
from math import sqrt

def dessine_bateau(Gbase_bateau, couleur_coque, couleur_cabine,
    couleur_fenetre, couleur_toit, couleur_base_cheminee, couleur_haut_cheminee
    ):
    setPenWidth(1)
    setPenColor('black')
    hideTurtle()
    hauteur_coque = Gbase_bateau / 4
    base_bateau = Gbase_bateau - hauteur_coque
    Phauteur = hauteur_coque / 4 * 3
    diagonale = sqrt(hauteur_coque ** 2 + Phauteur ** 2)
    diametre_hublot = Gbase_bateau / 12
    hauteur_cabine = diametre_hublot * 1.5
    longueur_cabine = Gbase_bateau * 2 / 3
    longueur_fenetre = Gbase_bateau / 12
    hauteur_fenetre = hauteur_cabine / 3
    hauteur_toit = hauteur_cabine / 4
    longueur_toit = longueur_cabine * 8 / 6
    hauteur_cheminee1 = longueur_toit / 8
    longueur_cheminee = hauteur_toit * 3
    hauteur_cheminee2 = hauteur_cheminee1 / 4

    def coque_bateau():
        setFillColor(couleur_coque)
        startPath()
        Phauteur = hauteur_coque / 4 * 3
        diagonale = sqrt(hauteur_coque ** 2 + Phauteur ** 2)
        penDown()
        right(90)
        forward(base_bateau)
        left(53.13)
        forward(diagonale)
        left(126.87)
        forward(Gbase_bateau + Phauteur - Phauteur / 3)
        left(126.87)
        forward(diagonale)
        fillPath()
        penUp()

    def hublot():
        for _ in range(6):
            penDown()
            dot(diametre_hublot)
            setPenColor('light blue')
            dot(diametre_hublot - diametre_hublot / 6)
            setPenColor('black')
            penUp()
            forward(2 * diametre_hublot)
        Phauteur = hauteur_coque / 4 * 3
        diagonale = sqrt(hauteur_coque ** 2 + Phauteur ** 2)
        penDown()
        right(90)
        forward(base_bateau)
        left(53.13)
        forward(diagonale)
        left(126.87)
        forward(Gbase_bateau + Phauteur - Phauteur / 3)
        left(126.87)
        forward(diagonale)
        penUp()

    def hublot():
        for _ in range(6):
            penDown()
            dot(diametre_hublot)
            setPenColor('light blue')
            dot(diametre_hublot - diametre_hublot // 6)
            setPenColor('black')
            penUp()
            forward(1.85 * diametre_hublot)

    def cabine():
        for _ in range(2):
            penDown()
            setFillColor(couleur_cabine)
            startPath()
            right(90)
            forward(longueur_cabine)
            right(90)
            forward(hauteur_cabine)
            fillPath()
        penUp()

    def fenetre():
        for _ in range(5):
            for _ in range(2):
                setFillColor(couleur_fenetre)
                startPath()
                penDown()
                right(90)
                forward(longueur_fenetre)
                right(90)
                forward(hauteur_fenetre)
                fillPath()
                penUp()
            right(90)
            forward(1.52 * longueur_fenetre)
            left(90)

    def toit_cabine():
        penDown()
        setFillColor(couleur_toit)
        startPath()
        for _ in range(2):
            right(90)
            forward(longueur_toit)
            right(90)
            forward(hauteur_toit)
        fillPath()
        penUp()

    def cheminee():
        for _ in range(3):
            penDown()
            setFillColor(couleur_base_cheminee)
            startPath()
            for loop in range(2):
                right(90)
                forward(longueur_cheminee)
                right(90)
                forward(hauteur_cheminee1)
            fillPath()
            penUp()
            forward(hauteur_cheminee2)
            penDown()
            setFillColor(couleur_haut_cheminee)
            startPath()
            for loop in range(2):
                right(90)
                forward(longueur_cheminee)
                right(90)
                forward(hauteur_cheminee2)
            fillPath()
            penUp()
            right(90)
            forward(longueur_cheminee)
            right(90)
            forward(hauteur_cheminee1 + hauteur_cheminee2)
            left(90)
            forward(longueur_cabine * 0.2)
            left(90)
            forward(hauteur_cheminee1)
    coque_bateau()
    back(diagonale / 2)
    left(53.13)
    forward(diametre_hublot)
    hublot()
    left(90)
    forward(hauteur_coque / 2)
    right(90)
    forward(Gbase_bateau / 35)
    left(180)
    forward(Gbase_bateau * 1 / 3 / 1.5 + longueur_cabine)
    right(90)
    forward(hauteur_cabine)
    cabine()
    right(180)
    forward(0.9 * hauteur_fenetre)
    left(90)
    forward(0.52 * longueur_fenetre)
    left(90)
    fenetre()
    forward(0.52 * longueur_fenetre)
    left(90)
    forward(longueur_cabine + (longueur_toit - longueur_cabine) / 2)
    right(90)
    toit_cabine()
    forward(hauteur_cheminee1)
    right(90)
    forward((longueur_toit - longueur_cabine) / 2 + hauteur_toit * 2)
    left(90)
    cheminee()

if __name__ == "__main__":
    dessine_bateau(200, 'lightgrey', 'grey', 'lightblue', 'lightgrey', 200, 'red')