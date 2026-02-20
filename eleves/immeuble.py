from gturtle import *

def immeuble(nb_colonnes, nb_etages, cote, couleur_fenetres,
    couleur_immeuble, couleur1, couleur2, couleur3):
    setPenWidth(2)
    setPenColor('black')
    hideTurtle()
    penDown()

    def fenetres(cote, couleur_fenetres):
        setFillColor(couleur_fenetres)
        startPath()
        for loop in range(4):
            forward(cote)
            right(90)
        fillPath()

    def colonnes_immeuble(nb_etages, cote, couleur_fenetres, couleur_immeuble):
        setPenColor(couleur_immeuble)
        setFillColor(couleur_immeuble)
        startPath()
        for loop in range(2):
            forward(cote * nb_etages + 0.5 * cote * nb_etages + 0.5 * cote)
            right(90)
            forward(cote + 2 * 0.5 * cote)
            right(90)
        fillPath()
        forward(0.5 * cote)
        right(90)
        forward(0.5 * cote)
        left(90)
        for loop in range(nb_etages):
            fenetres(cote, couleur_fenetres)
            penUp()
            forward(cote + 0.5 * cote)
        back(cote * nb_etages + 0.5 * cote * nb_etages + 0.5 * cote)
        right(90)
        forward(cote + 0.5 * cote)
        left(90)
    for loop in range(nb_colonnes):
        colonnes_immeuble(nb_etages, cote, couleur_fenetres, couleur_immeuble)
    penUp()
    left(90)
    forward(cote * 2 * nb_colonnes)
    right(90)
    forward(cote * nb_etages + 0.5 * cote * nb_etages + 0.5 * cote)

    def guirlande(couleur1, couleur2, couleur3, cote, nb_colonnes):
        right(90)
        for loop in range(nb_colonnes + 1):
            penDown()
            setPenColor(couleur1)
            dot(cote * 0.5)
            penUp()
            forward(cote * 2)
        back((nb_colonnes + 1) * 2 * cote)
        right(90)
        forward(cote)
        left(90)
        for loop in range(nb_colonnes):
            forward(0.5 * cote)
            penDown()
            setPenColor(couleur2)
            dot(cote * 0.5)
            penUp()
            forward(cote)
            penDown()
            setPenColor(couleur3)
            dot(cote * 0.5)
            penUp()
            forward(cote * 0.5)

    def fil_guirlande(nb_colonnes, cote):
        right(180)
        setPenColor('black')
        setPenWidth(0.05 * cote)
        penDown()
        for loop in range(nb_colonnes):
            left(math.degrees(math.atan(0.5)))
            forward(sqrt(cote ** 2 + (cote / 2) ** 2))
            left(90 - math.degrees(math.atan(0.5)))
            forward(cote)
            left(90 - math.degrees(math.atan(0.5)))
            forward(sqrt(cote ** 2 + (cote / 2) ** 2))
            left(math.degrees(math.atan(0.5)) + 180)
        penUp()
    fil_guirlande(nb_colonnes, cote)
    right(90)
    forward(cote * nb_colonnes * 2)
    right(90)
    guirlande(couleur1, couleur2, couleur3, cote, nb_colonnes)
    penUp()


if __name__ == '__main__':
    immeuble(5, 8, 20, 'lightBlue', 'lightGrey', 'blue', 'red', 'green')
