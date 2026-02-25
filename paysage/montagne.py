from gturtle import *
from math import radians, sqrt, tan


def montagne(hauteur, hauteur_neige, angle, couleur, couleur_neige):
    setPenWidth(1)
    setPenColor('black')
    hideTurtle()
    angle_exterieur = 180 - angle
    neige = hauteur - hauteur_neige
    demi_basse_neige = neige * tan(radians(angle / 2))

    def triangle(hauteur, angle, couleur):
        demi_basse = hauteur * tan(radians(angle / 2))
        penDown()
        setFillColor(couleur)
        startPath()
        for loop in range(2):
            forward(sqrt(hauteur ** 2 + demi_basse ** 2))
            right(angle_exterieur)
        fillPath()
        penUp()
    demi_basse = hauteur * tan(radians(angle / 2))
    right((180 - angle_exterieur) / 2)
    triangle(hauteur, angle, couleur)
    right(angle)
    forward(sqrt(hauteur ** 2 + demi_basse ** 2))
    left(angle_exterieur)
    forward(sqrt(neige ** 2 + demi_basse_neige ** 2))
    left(180)
    triangle(neige, angle, couleur_neige)
    left(angle_exterieur)
    forward(sqrt(hauteur ** 2 + demi_basse ** 2) - sqrt(neige ** 2 + 
        demi_basse_neige ** 2))
    right((180 - angle_exterieur) / 2)
    left(180)

if __name__ == '__main__':
    montagne(100, 70, 100, 'bisque', 'snow2')

"""
Docstring – fonction montagne(hauteur, hauteur_neige, angle, couleur, couleur_neige)

Paramètres
----------
hauteur : (int | float)
    Hauteur totale de la montagne (grand triangle), exprimée en pixels (unités gturtle).
    Plus la valeur est grande, plus le triangle dessiné est haut.

hauteur_neige : (int | float)
    Hauteur de la partie de montagne qui reste visible (non enneigée), mesurée depuis la base.
    La hauteur effective de la calotte de neige est calculée comme :
        neige = hauteur - hauteur_neige
    Donc :
    - si hauteur_neige est proche de hauteur, il reste peu de neige (petit triangle blanc),
    - si hauteur_neige est petit, la neige occupe une grande partie du sommet.

angle : (int | float)
    Angle au sommet (en degrés) du triangle isocèle représentant la montagne (et la neige).
    Cet angle contrôle “l’ouverture” de la montagne :
    - angle petit -> montagne pointue (pentes raides),
    - angle grand -> montagne plus large (pentes douces).
    Doit être compris strictement entre 0 et 180 degrés pour que la trigonométrie (tan(angle/2))
    reste cohérente.

couleur : (str)
    Couleur de remplissage de la montagne (grand triangle).
    Doit être un nom de couleur reconnu par gturtle (ex. 'bisque', 'red', 'gray', etc.).

couleur_neige : (str)
    Couleur de remplissage de la neige (petit triangle au sommet).
    Doit être un nom de couleur reconnu par gturtle (ex. 'snow2', 'white', etc.).
"""
