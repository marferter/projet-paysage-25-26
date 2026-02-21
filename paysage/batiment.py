from gturtle import *

def batiment(nombre_etage, nombre_de_fenetre, couleur_porte, couleur_fenetre, couleur_batiment, taille):
    hideTurtle()
    setPenColor("black")
    setPenWidth(1)
    
    def fenetre(couleur_fenetre, taille_fenetre) :
        setFillColor(couleur_fenetre)
        startPath()
        for _ in range (2) :
            fd(taille_fenetre*1.5)
            rt(90)
            fd(taille_fenetre)
            rt(90)
        fillPath()
        
    def mur(hauteur) :
        penUp()
        fd(hauteur)
        bk(hauteur - 15 * taille)
        rt(90)
        fd(15 * taille)
        lt(90)
        
    def etage(nombre_etage, nombre_de_fenetre, couleur_fenetre,largeur_entre_fenetre, couleur_batiment, hauteur):
        for _ in range (nombre_etage) :         
            mur(75* taille)
            for _ in range (nombre_de_fenetre) :
                fenetre(couleur_fenetre, taille_fenetre)
                #espace entre les fenêtres
                penUp()
                rt(90)
                fd(taille_fenetre*2.5)
                lt(90)
                
            
            #retour pour faire le mur
            penUp()
            lt(90)
            fd(taille_fenetre*2.5)
            bk(taille_fenetre + 15*taille )
            rt(90)
            bk(15*taille)
            
            mur(hauteur)
            #retour pour faire un étage suivant
            penUp()
            lt(90)
            fd(20* taille + nombre_de_fenetre * taille_fenetre * 5/2 - taille_fenetre*6/9)
            rt(90)
            fd(60*taille)
            penDown()
       
    
    
    def porte(longueur, largeur, couleur_porte) :
        penUp()
        setFillColor(couleur_porte)
        startPath()
        fd(largeur/2)
        rt(90)
        fd(longueur)
        rt(90)
        fd(largeur)
        rt(90)
        fd(longueur)
        
        fillPath()
        bk(70* taille/2)
        rt(90)
        fd(5*taille)
        dot(5*taille)
        bk(5*taille)
        lt(90)
        fd(70* taille/2)
        rt(90)
        fd(largeur/2)
        rt(90)
        penDown()
    
    def rez_de_chaussee(nombre_de_fenetre, couleur_porte, hauteur) :
        penUp()
        mur(hauteur)
        penUp()
        rt(90)
        fd(20*taille + nombre_de_fenetre * taille_fenetre * 5/2 - taille_fenetre * 7/6)
        bk(15*taille)
        lt(90)
        bk(15*taille)
        mur(hauteur)
        #retour pour faire un étage suivant
        penUp()
        bk(15*taille)
        lt(90)
        fd(15*taille)
        fd((20*taille + nombre_de_fenetre * taille_fenetre * 5/2 - taille_fenetre * 7/6)/2)
        porte(70* taille, 40* taille, couleur_porte)
        penUp()
        lt(90)
        fd((20*taille + nombre_de_fenetre * taille_fenetre * 5/2 - taille_fenetre * 7/6)/2)
        rt(90)
        fd(75*taille)
        penDown()
        
    def toit(nombre_de_fenetre,taille_fenetre):
        penUp()
        rt(90)
        fd(20*taille + nombre_de_fenetre * taille_fenetre * 5/2 - taille_fenetre * 7/6)   
        lt(90)
        
    def coloriage_batiment(couleur_batiment, taille_fenetre, nombre_de_fenetre, nombre_etage, hauteur): 
        penUp()
        setFillColor(couleur_batiment)
        startPath()
        rt(90)
        fd(20*taille + nombre_de_fenetre * taille_fenetre * 5/2 - taille_fenetre * 7/6)
        rt(90)
        fd(hauteur*(nombre_etage+1))
        rt(90)
        fd(20*taille + nombre_de_fenetre * taille_fenetre * 5/2 - taille_fenetre * 7/6)
        rt(90)
        fd(hauteur*(nombre_etage+1))
        rt(90)
        lt(90)
        fillPath()
        bk(hauteur*(nombre_etage+1))
        penDown()

    #parametrage de la taille du batiment
    taille_fenetre = 30
    taille_fenetre *=taille
    hauteur = 75
    hauteur *= taille
    
    largeur_entre_fenetre = taille_fenetre*2.5
    
    coloriage_batiment(couleur_batiment, taille_fenetre, nombre_de_fenetre, nombre_etage, hauteur)
    rez_de_chaussee(nombre_de_fenetre, couleur_porte, hauteur)
    etage(nombre_etage, nombre_de_fenetre, couleur_fenetre, largeur_entre_fenetre, couleur_batiment, hauteur)
    toit(nombre_de_fenetre, taille_fenetre)

if __name__ == "__main__":
    batiment(4, 7, "brown", "lightblue", "grey", 1)

"""
batiment(nombre_etage, nombre_de_fenetre, couleur_porte, couleur_fenetre,
         couleur_batiment, taille)

Dessine un immeuble résidentiel vu de face, avec un rez-de-chaussée
(porte centrale), plusieurs étages garnis de fenêtres, et un toit plat.

Paramètres :
    nombre_etage      : nombre d'étages au-dessus du rez-de-chaussée.
    nombre_de_fenetre : nombre de fenêtres par rangée (par étage).
    couleur_porte     : couleur de la porte d'entrée.
    couleur_fenetre   : couleur des fenêtres.
    couleur_batiment  : couleur de la facade du bâtiment.
    taille            : facteur d'échelle global du bâtiment.
                        taille=1 correspond à une fenêtre de 30 pixels de
                        côté et un étage de 75 pixels de hauteur. Toutes
                        les dimensions sont multipliées par ce facteur.

Position initiale de la tortue :
    La tortue part depuis la position par défaut (origine), en bas à gauche
    du bâtiment, orientée vers le haut (nord).
"""
