from gturtle import *
makeTurtle()
penWidth(3)


def fusee2(taille_base, couleur_primaire, couleur_secondaire,
    couleur_flammes, longueur_flammes):
    setPenWidth(1)
    setPenColor('black')
    hideTurtle()

    def rectangle(longueur, largeur_fusee, couleur='white', tourner_droite=True
        ):
        penDown()
        setFillColor(couleur)
        startPath()
        if tourner_droite:
            for _ in range(2):
                fd(longueur)
                rt(90)
                fd(largeur_fusee)
                rt(90)
        else:
            for _ in range(2):
                fd(longueur)
                lt(90)
                fd(largeur_fusee)
                lt(90)
        fillPath()
        penUp()

    def triangle(cote, couleur):
        penDown()
        setFillColor(couleur)
        startPath()
        for _ in range(3):
            fd(cote)
            lt(120)
        fillPath()
        penUp()
        
    largeur_fusee = taille_base * 1.5

    #corps fusée
    rectangle(taille_base, largeur_fusee, couleur_secondaire)
    fd(taille_base)
    rectangle(taille_base * 2, largeur_fusee, couleur_primaire)
    fd(taille_base * 2)
    rectangle(taille_base / 3, largeur_fusee, couleur_secondaire)
    fd(taille_base / 3)
    rt(90)
    triangle(taille_base * 1.5, couleur_primaire)
    
    #flammes
    lt(90)
    bk(taille_base + taille_base * 2 + taille_base / 3)
    rt(180)
    rectangle(longueur_flammes, largeur_fusee / 4, couleur_flammes, False)
    lt(90)
    fd(taille_base * 1.5 / 3 + largeur_fusee / 4 / 3 / 2)
    rt(90)
    rectangle(longueur_flammes * 1.3, largeur_fusee / 4, couleur_flammes, False)
    lt(90)
    fd(taille_base * 1.5 / 3 + largeur_fusee / 4 / 3 / 2)
    rt(90)
    rectangle(longueur_flammes, largeur_fusee / 4, couleur_flammes, False)

    #ailerons
    lt(90)
    bk(taille_base + taille_base / 8)
    lt(90)
    triangle(taille_base, couleur_primaire)
    rt(90)
    fd(largeur_fusee)
    lt(90)
    fd(taille_base)
    rt(180)
    triangle(taille_base, couleur_primaire)

    #hublot
    lt(90)
    bk(largeur_fusee / 2)
    lt(90)
    penUp()
    fd(taille_base)
    dot(taille_base)
    setPenColor('aqua')
    dot(taille_base - taille_base / 100 * 8)
    setPenColor('black')
    bk(taille_base)
    rt(90)

if __name__ == "__main__":
    fusee2(100, 'lightGrey', 'red', 'orange', 100)


