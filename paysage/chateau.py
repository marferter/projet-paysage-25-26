from gturtle import *
from math import pi


def dessiner_chateau(taille=1, couleur_tours='gray', couleur_fenetre='lightblue'):
    setPenWidth(1)
    setPenColor('black')
    hideTurtle()

    def tour(hauteur, largeur_creneaux, nbr_creneaux):
        fd(hauteur * taille)
        lt(90)
        for _ in range(nbr_creneaux):
            fd(largeur_creneaux * taille)
            lt(90)
            fd(largeur_creneaux * taille)
            rt(90)
            fd(largeur_creneaux * taille)
            rt(90)
            fd(largeur_creneaux * taille)
            lt(90)
        fd(largeur_creneaux * taille)
        lt(90)
        fd(hauteur * taille)

    def fenetre_triangle(longueur=15):
        for _ in range(3):
            fd(longueur * taille)
            lt(120)

    def fenetre_tour(nombre_de_fenetre, distance=30, couleur='lightblue'):
        for _ in range(nombre_de_fenetre):
            setFillColor(couleur)
            startPath()
            fenetre_triangle()
            fillPath()
            pu()
            fd(7.5 * taille)
            lt(90)
            fd(distance * taille)
            lt(90)
            fd(7.5 * taille)
            rt(180)
            pd()

    def porte_chateau(hauteur, largeur):
        fd(largeur * taille)
        lt(90)
        fd(hauteur * taille)
        for _ in range(18):
            fd(largeur * pi / 36 * taille)
            rt(10)
        fd(hauteur * taille)
        lt(90)
        
    setFillColor(couleur_tours)
    startPath()
    tour(125, 10, 3)
    rt(180)
    tour(75, 10, 5)
    rt(180)
    tour(125, 10, 3)
    fillPath()
    lt(90)
    fd(250 * taille)
    pu()
    bk(45 * taille)
    lt(90)
    fd(30 * taille)
    rt(90)
    pd()
    fenetre_tour(3,30,couleur_fenetre)
    lt(90)
    pu()
    lt(180)
    fd(120 * taille)
    rt(90)
    fd(180 * taille)
    rt(180)
    lt(90)
    fd(30 * taille)
    rt(90)
    pd()
    fenetre_tour(3,30,couleur_fenetre)
    pu()
    rt(90)
    fd(120 * taille)
    lt(90)
    fd(70 * taille)
    pd()
    setPenColor('saddlebrown')
    setFillColor('saddlebrown')
    startPath()
    porte_chateau(35, 20)
    fillPath()
    
if __name__ == '__main__':
    dessiner_chateau(1, 'grey', 'black')

"""
dessiner_chateau(taille=1, couleur_tours='gray', couleur_fenetre='lightblue')

Dessine un château médiéval vu de face, composé de deux grandes tours
latérales avec créneaux, d'une tour centrale plus petite, de fenêtres
triangulaires et d'une porte en arc.

Paramètres :
    taille          : facteur d'échelle global du château.
                      taille=1 correspond à une hauteur des grandes tours
                      de 125 pixels et une largeur de créneau de 10 pixels.
                      Toutes les longueurs sont multipliées par ce facteur.
    couleur_tours   : couleur des tours, murs et créneaux.
    couleur_fenetre : couleur des fenêtres triangulaires des tours.

Position initiale de la tortue :
    La tortue part depuis la position par défaut (origine), à la base
    du coin inférieur gauche de la tour gauche, orientée vers le haut
    (nord). Le dessin débute par la montée de cette première tour.
"""