from gturtle import *
from math import sqrt


def sapin(base_grand_triangle, nb_etages, couleur_sapin, couleur_boules, couleur_etoile):
    setPenWidth(1)
    setPenColor('black')
    hideTurtle()

    def tronc(base_tronc, hauteur_tronc, couleur_tronc):
        penDown()
        setFillColor('brown')
        startPath()
        lt(90)
        fd(base_tronc / 2)
        rt(90)
        fd(hauteur_tronc)
        rt(90)
        fd(base_tronc)
        rt(90)
        fd(hauteur_tronc)
        rt(90)
        fd(base_tronc / 2)
        rt(90)
        fd(hauteur_tronc)
        fillPath()
        penUp()

    def triangle(base, couleur):
        penDown()
        lt(90)
        setFillColor(couleur)
        startPath()
        fd(base / 2)
        rt(120)
        fd(base)
        rt(120)
        fd(base)
        rt(120)
        fd(base / 2)
        fillPath()
        penUp()

    def boules(nb_etages, base):
        penDown()
        for loop in range(nb_etages):
            penUp()
            back(base / 3.5 * 3)
            setPenColor('red')
            dot(base / 6)
            penUp()
            rt(90)
            fd(base / 4)
            dot(base / 6)
            penUp()
            back(base / 2)
            dot(base / 6)
            penUp()
            fd(base / 4)
            penDown()
            lt(90)
            base = base * 7 / 5
        penUp()
        fd(base / 3)
        penDown()
        for loop in range(nb_etages):
            setPenColor('red')
            dot(base / 9)
            penUp()
            fd(base / 2)
            penDown()
            base = base * 5 / 7
        penUp()

    def étoile(base,couleur):
        penDown()
        setPenColor(couleur)
        fd(base / 1.5)
        back(base / 3)
        for loop in range(8):
            rt(45)
            fd(base / 3)
            back(base / 3)
        penUp()
        
    base_tronc = base_grand_triangle / 6
    hauteur_tronc = base_tronc * 2
    tronc(base_tronc, hauteur_tronc, 'brown')

    base = base_grand_triangle
    for loop in range(nb_etages):
        triangle(base, couleur_sapin)
        rt(90)
        fd(base / 1.5)
        base = base / 7 * 5
    étoile(base,couleur_etoile)
    boules(nb_etages, base)


if __name__ == '__main__':
    sapin(100, 3, 'green','red','orange')

"""
sapin(base_grand_triangle, nb_etages, couleur_sapin, couleur_boules,
      couleur_etoile)

Dessine un sapin décoré vu de face, composé d'un tronc, de plusieurs
niveaux de triangles (étages de branches), de boules de décoration et
d'une étoile au sommet.

Paramètres :
    base_grand_triangle : largeur de la base du plus grand triangle
                          (étage inférieur) du sapin (en pixels).
                          C'est la dimension de référence ; les triangles
                          des étages supérieurs sont progressivement plus
                          petits (chaque étage vaut 5/7 du précédent).
    nb_etages           : nombre de niveaux de branches triangulaires.
    couleur_sapin       : couleur de remplissage des triangles de branches.
    couleur_boules      : couleur des boules de décoration.
    couleur_etoile      : couleur de l'étoile au sommet du sapin.

Position initiale de la tortue :
    La tortue part depuis la position par défaut (origine), au bas du
    tronc, orientée vers le haut (nord). Le dessin débute par le tronc,
    puis les étages de branches sont construits de bas en haut.
"""