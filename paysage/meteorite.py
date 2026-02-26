from gturtle import *
from math import pi, atan, degrees, sin

def final_meteorite(diametre_meteorite, couleurflamme_ext, couleurflamme_int):
    setPenWidth(1)
    setPenColor('black')
    hideTurtle()
    n = 36

    def arc_cercle(diametre, angle, couleur,n):
        penDown()
        setPenColor(couleur)
        for _ in range(int(angle / 360 * n) + 1):
            forward(pi * diametre / n)
            left(360 / n)
        penUp()


    def flamme(base, hauteur):
        penDown()
        demi_base = base / 2
        alpha = atan(hauteur / demi_base)
        alpha_degrees = degrees(alpha)
        beta_degrees = 180 - 2 * alpha_degrees
        hyp = hauteur / sin(alpha)
        left(90 - alpha_degrees)
        forward(hyp)
        left(180 - beta_degrees)
        forward(hyp)
        left(180 - alpha_degrees)
        forward(base)
        penUp()

    def flammes(diametre, couleur) :
        #demi_cercle
        setFillColor(couleur)
        startPath()
        right(90)
        forward(diametre / 2)
        left(90)
        arc_cercle(diametre, 180, couleur,n)
        left(90 - 360 / n)
        forward(diametre)
        fillPath()
        #flamme centrale
        hauteur_flamme_centre = diametre * 2
        base_flamme_centre = diametre / 2
        back(diametre - (diametre - base_flamme_centre) / 2)
        right(90)
        startPath()
        flamme(base_flamme_centre,hauteur_flamme_centre)
        fillPath()
        #flamme gauche
        forward((diametre - base_flamme_centre) / 2)
        hauteur_flamme_gauche = diametre * 1.3
        base_flamme_gauche = diametre / 2.5
        left(90)
        startPath()
        flamme(base_flamme_gauche,hauteur_flamme_gauche)
        fillPath()
        #flamme droite
        hauteur_flamme_droite = diametre * 1.4
        base_flamme_droite = diametre / 2
        back(diametre - base_flamme_droite)
        left(90)
        startPath()
        flamme(base_flamme_droite,hauteur_flamme_droite)
        fillPath()

        forward(diametre / 2 - base_flamme_droite)
        
    def meteorite(diametre_meteorite,couleur_ext):
        setPenColor(couleur_ext)
        dot(diametre_meteorite * 1.15)
        setPenColor('black')
        dot(diametre_meteorite * 1.05)
        setPenColor('grey')
        dot(diametre_meteorite)

    diametre = diametre_meteorite * 1.15
    flammes(diametre, couleurflamme_ext)
    diametre_petites_flammes = diametre * 0.85
    right(90)
    forward(diametre_meteorite * 0.03)
    flammes(diametre_petites_flammes,couleurflamme_int)
    right(90)
    forward(diametre_meteorite * 0.03)
    meteorite(diametre_meteorite,couleurflamme_ext)
    #crateres
    setPenColor("black")
    left(30)
    forward(diametre_meteorite * 0.3)
    dot(diametre_meteorite * 0.2)
    back(diametre_meteorite * 0.3)
    right(90)
    forward(diametre_meteorite * 0.3)
    dot(diametre_meteorite * 0.3)
    back(diametre_meteorite * 0.3)
    right(150)
    forward(diametre_meteorite * 0.3)
    dot(diametre_meteorite * 0.25)
    back(diametre_meteorite * 0.3)

    

if __name__ == '__main__':
    final_meteorite(150, 'firebrick1', 'darkOrange')
