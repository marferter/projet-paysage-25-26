from gturtle import *
from math import sqrt, degrees, atan


def eglise(largeur, couleur_nef, couleur_clocher, couleur_toit, couleur_horloge="white"):
    setPenWidth(1)
    setPenColor('black')
    hideTurtle()

    def rectangle(hauteur, base, couleur):
        setFillColor(couleur)
        startPath()
        penDown()
        for _ in range(2):
            forward(hauteur)
            right(90)
            forward(base)
            right(90)
        fillPath()
        penUp()

    def demi_carre(cote, couleur):
        penDown()
        hypotenuse = sqrt(cote ** 2 + cote ** 2)
        setFillColor(couleur)
        startPath()
        forward(hypotenuse)
        right(180 - 45)
        forward(cote)
        right(90)
        forward(cote)
        fillPath()
        penUp()
    
    def fleche(base,hauteur,couleur) :
        angle_base = degrees(atan(hauteur / (base * 0.5)))
        angle_sommet = 180 - 2 * angle_base
        hypotenuse = sqrt((base / 2) ** 2 + hauteur ** 2)

        penDown()
        setFillColor(couleur)
        startPath()
        right(90 - angle_base)
        forward(hypotenuse)
        right(180 - angle_sommet)
        forward(hypotenuse)
        right(180 - angle_base)
        forward(base)
        fillPath()
        penUp()
        
    #nef
    hauteur_nef = 3 / 8 * largeur
    base_nef = 3 / 4 * largeur
    rectangle(hauteur_nef,base_nef,couleur_nef)
    
    #toit nef
    hauteur_toit = 2 / 3 * hauteur_nef
    largeur_toit = base_nef - hauteur_toit
    forward(hauteur_nef)
    right(45)
    demi_carre(hauteur_toit,couleur_toit)
    back(hauteur_toit)
    right(90)
    rectangle(hauteur_toit, largeur_toit,couleur_toit)
    
    #clocher
    hauteur_clocher = 3 / 4 * largeur
    base_clocher = largeur / 4
    back(hauteur_nef)
    right(90)
    forward(largeur / 2)
    left(90)
    rectangle(hauteur_clocher,base_clocher,couleur_clocher)

    #flèche
    hauteur_fleche = 2 * base_clocher
    forward(hauteur_clocher)
    fleche(base_clocher,hauteur_fleche,couleur_toit)
    
    #horloge
    back(base_clocher * 0.5)
    left(90)
    forward(1 / 2 * base_clocher)
    setPenColor(couleur_horloge)
    dot(2 / 5 * base_clocher)

if __name__ == '__main__':
    eglise(120, 'lightGrey', 'grey', 'darkRed')

"""
eglise(largeur, couleur_nef, couleur_clocher, couleur_toit,
       couleur_horloge='white')

Dessine une église vue de face, composée d'une nef rectangulaire avec
son toit triangulaire, d'un clocher surmonté d'une flèche et d'une
horloge circulaire.

Paramètres :
    largeur         : largeur totale de l'église (en pixels).
                      La hauteur de la nef (3/8 de la largeur), la base
                      de la nef (3/4 de la largeur), la hauteur du clocher
                      (3/4 de la largeur) et toutes les autres dimensions
                      en découlent.
    couleur_nef     : couleur des murs de la nef (corps principal).
    couleur_clocher : couleur des murs du clocher (tour).
    couleur_toit    : couleur du toit de la nef et de la flèche du clocher.
    couleur_horloge : couleur de l'horloge sur le clocher (blanc par défaut).

Position initiale de la tortue :
    La tortue part depuis la position par défaut (origine), au coin
    inférieur gauche de la nef, orientée vers le haut (nord).
"""
