from gturtle import *

def arriere_plan(base,hauteur_1,hauteur_2, couleur_1, couleur_2) :
    hideTurtle()
    penDown()
    setPos(- (base / 2 - hauteur_1 / 2),- hauteur_1 / 2)
    setHeading(90)
    setPenColor(couleur_1)
    setPenWidth(hauteur_1)
    forward(base - hauteur_1)

    setPos(- (base / 2 - hauteur_2 / 2), hauteur_2 / 2)
    setHeading(90)
    setPenColor(couleur_2)
    setPenWidth(hauteur_2)
    forward(base - hauteur_2)
    penUp()



if __name__ == "__main__":
    arriere_plan(600,200,150, "SeaGreen", "LightCyan")

"""
arriere_plan(base, hauteur_1, hauteur_2, couleur_1, couleur_2)

Dessine un arrière-plan composé de deux bandes horizontales superposées,
représentant typiquement le sol (en bas) et le ciel (en haut).

Paramètres :
    base      : largeur totale de l'arrière-plan (en pixels).
    hauteur_1 : épaisseur de la bande inférieure (sol, mer, prairie...).
                C'est la taille verticale de la zone basse du décor.
    hauteur_2 : épaisseur de la bande supérieure (ciel, fond...).
                C'est la taille verticale de la zone haute du décor.
    couleur_1 : couleur de la bande inférieure (ex. 'SeaGreen' pour un sol).
    couleur_2 : couleur de la bande supérieure (ex. 'LightCyan' pour le ciel).

Position initiale de la tortue :
    La tortue utilise setPos() pour se positionner directement ; son point
    de départ correspond au bord gauche de la bande inférieure, centré
    verticalement sur cette bande.
"""