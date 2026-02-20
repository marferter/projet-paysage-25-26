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
