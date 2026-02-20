from gturtle import *
setPenColor('white')


def sapin(taille):
    setPenWidth(2)
    setPenColor('black')
    hideTurtle()

    def tronc(base):
        hauteur = base * 2
        setFillColor('brown')
        startPath()
        forward(hauteur)
        right(90)
        forward(base)
        right(90)
        forward(hauteur)
        right(90)
        forward(base)
        right(90)
        forward(hauteur)
        fillPath()

    def triangle(cote):
        setFillColor('green')
        startPath()
        right(30)
        for _ in range(3):
            forward(cote / 2)
            forward(cote / 2)
            setPenColor('red')
            dot(10)
            setPenColor('green')
            right(360 / 3)
        fillPath()

    def positionement(taille):
        forward(taille / 2)
        penUp()
        left(120)
        forward(taille / 4)
        right(90)
        penDown()

    def branche(largeur):
        triangle(largeur)
        positionement(largeur)
        triangle(largeur)
        positionement(largeur)
        triangle(largeur)
        positionement(largeur)

    def arbre(taille):
        branche(taille)

    def dessine_etoile(cote):
        forward(cote)
        setFillColor('gold')
        startPath()
        for _ in range(3):
            forward(cote)
            right(120)
        fillPath()
        left(30)
        forward(cote / 2)
        right(90)
        startPath()
        for _ in range(3):
            forward(cote)
            right(120)
        fillPath()
        

    tronc(taille / 5)
    left(90)
    forward(2 * taille / 5)
    right(90)
    arbre(taille)
    right(90)
    penUp()
    forward(taille / 4 - taille / 12)
    forward(taille / 4 - taille / 12)
    left(90)
    back(taille / 8)
    penUp()
    dessine_etoile(taille / 2)
    right(30)
    penUp()
    back(taille / 5)

if __name__ == '__main__':
    sapin(100)
