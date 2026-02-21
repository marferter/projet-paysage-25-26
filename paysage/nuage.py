from gturtle import *

def nuage(taille, couleur):
    hideTurtle()
    rayon = taille * 0.5
    penUp()
    setPenColor(couleur)
    dot(taille)
    right(80)
    forward(rayon)
    dot(taille * 0.7)
    back(rayon)
    left(80)
    left(60)
    forward(rayon)
    dot(taille * 0.4)
    back(rayon)
    right(60)
    left(100)
    forward(rayon * 1.1)
    dot(taille * 0.6)
    
if __name__ == '__main__':
    nuage(200, 'darkGrey')

"""
nuage(taille, couleur)

Dessine un nuage composé de plusieurs disques (cercles pleins) de
tailles décroissantes disposés autour d'un disque central.

Paramètres :
    taille  : diamètre du disque central du nuage (en pixels).
              Les disques satellites ont des diamètres proportionnels
              au disque central (0.7×taille, 0.6×taille, 0.4×taille).
    couleur : couleur du nuage (tous les disques ont la même couleur).

Position initiale de la tortue :
    La tortue part depuis la position par défaut (origine), au centre
    du disque principal du nuage. Le premier cercle est tracé à cet
    endroit, puis la tortue se déplace pour tracer les cercles satellites.
"""
