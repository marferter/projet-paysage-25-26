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