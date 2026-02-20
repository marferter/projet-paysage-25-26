from gturtle import *
from math import atan, degrees

def moulin(largeur, angle, couleur_toit, couleur_pan, couleur_fenetre,
    couleur_bat, couleur_porte):
    setPenWidth(1)
    setPenColor('black')
    hideTurtle()

    def toit(couleur_toit, largeur):
        penDown()
        right(90)
        setFillColor(couleur_toit)
        startPath()
        for _ in range(3):
            forward(largeur)
            left(120)
        left(90)
        fillPath()
        penUp()

    def pan(couleur_pan, largeur):
        angle = 360 / 12
        setFillColor(couleur_pan)
        startPath()
        penDown()
        for _ in range(4):
            right(angle)
            forward(largeur * 1.5)
            right(90 + angle / 2)
            forward(largeur * 0.78)
            right(90 + angle / 2)
            forward(largeur * 1.5)
            left(180 - angle)
        fillPath()
        penUp()
        

    def fenetre(couleur_fenetre, diametre):
        penDown()
        setPenColor(couleur_fenetre)
        dot(diametre)
        setPenColor("black")
        penUp()

    def batiment(couleur_bat, largeur):
        penDown()
        setFillColor(couleur_bat)
        startPath()
        right(90 - alpha)
        forward(hypo_tri_rec)
        right(alpha)
        forward(petite_largeur)
        right(alpha)
        forward(hypo_tri_rec)
        right(180 - alpha)
        forward(largeur)
        fillPath()
        penUp()



    def porte(couleur_porte, largeur):
        setFillColor(couleur_porte)
        startPath()
        penDown()
        hauteur = largeur * 2
        for _ in range(2):
            forward(hauteur)
            right(90)
            forward(largeur)
            right(90)
        fillPath()
        penUp()


    petite_largeur = 0.6 * largeur
    hauteur = 1.5 * largeur
    base_tri_rec = (largeur - petite_largeur) / 2
    alpha = degrees(atan(hauteur / base_tri_rec))
    hypo_tri_rec = sqrt(base_tri_rec ** 2 + hauteur ** 2)
    batiment(couleur_bat, largeur)

    #porte
    largeur_porte = largeur / 3
    back((largeur - largeur_porte) / 2 )
    right(90)
    porte(couleur_porte,largeur_porte)
    
    #fenêtre
    left(90)
    back(largeur_porte / 2)
    right(90)
    forward(hauteur * 3 / 4)
    fenetre(couleur_fenetre, largeur / 4)

    #toit
    forward(hauteur * 1 /4)
    left(90)
    forward(petite_largeur / 2)
    right(90)
    toit(couleur_toit,petite_largeur)

    #helice
    hauteur_toit = sqrt(petite_largeur ** 2 - (petite_largeur / 2) ** 2)
    right(90 - 30)
    forward(2 / 3 * hauteur_toit)

    setHeading(angle)
    longueur_pan = largeur * 0.8
    pan(couleur_pan,longueur_pan)
    

if __name__ == '__main__':
    moulin(100, 80, 'red', 'grey', 'lightBlue', 'gold', 'brown')

