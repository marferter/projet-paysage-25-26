# Auto-generated combined module
# Source folder: paysage
# Generated: 2026-02-20T02:36:15.736656Z
# NOTE: top-level calls have been skipped. Review warnings printed during generation.

# ---- imports (deduplicated) ----
from gturtle import *
from math import sqrt
from math import pi
from math import sqrt, degrees, atan
from math import cos, tan, atan, radians, degrees
from math import atan, degrees
from math import atan, degrees, pi, sqrt

# ---- collected definitions / assignments ----

# --- from arriere-plan.py ---
def arriere_plan(base,hauteur_1,hauteur_2, couleur_1, couleur_2) :
    hideTurtle()
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

# --- from bateau.py ---
def dessine_bateau(Gbase_bateau, couleur_coque, couleur_cabine,
    couleur_fenetre, couleur_toit, couleur_base_cheminee, couleur_haut_cheminee
    ):
    setPenWidth(1)
    setPenColor('black')
    hideTurtle()
    hauteur_coque = Gbase_bateau / 4
    base_bateau = Gbase_bateau - hauteur_coque
    Phauteur = hauteur_coque / 4 * 3
    diagonale = sqrt(hauteur_coque ** 2 + Phauteur ** 2)
    diametre_hublot = Gbase_bateau / 12
    hauteur_cabine = diametre_hublot * 1.5
    longueur_cabine = Gbase_bateau * 2 / 3
    longueur_fenetre = Gbase_bateau / 12
    hauteur_fenetre = hauteur_cabine / 3
    hauteur_toit = hauteur_cabine / 4
    longueur_toit = longueur_cabine * 8 / 6
    hauteur_cheminee1 = longueur_toit / 8
    longueur_cheminee = hauteur_toit * 3
    hauteur_cheminee2 = hauteur_cheminee1 / 4

    def coque_bateau():
        setFillColor(couleur_coque)
        startPath()
        Phauteur = hauteur_coque / 4 * 3
        diagonale = sqrt(hauteur_coque ** 2 + Phauteur ** 2)
        penDown()
        right(90)
        forward(base_bateau)
        left(53.13)
        forward(diagonale)
        left(126.87)
        forward(Gbase_bateau + Phauteur - Phauteur / 3)
        left(126.87)
        forward(diagonale)
        fillPath()
        penUp()

    def hublot():
        for _ in range(6):
            penDown()
            dot(diametre_hublot)
            setPenColor('light blue')
            dot(diametre_hublot - diametre_hublot / 6)
            setPenColor('black')
            penUp()
            forward(2 * diametre_hublot)
        Phauteur = hauteur_coque / 4 * 3
        diagonale = sqrt(hauteur_coque ** 2 + Phauteur ** 2)
        penDown()
        right(90)
        forward(base_bateau)
        left(53.13)
        forward(diagonale)
        left(126.87)
        forward(Gbase_bateau + Phauteur - Phauteur / 3)
        left(126.87)
        forward(diagonale)
        penUp()

    def hublot():
        for _ in range(6):
            penDown()
            dot(diametre_hublot)
            setPenColor('light blue')
            dot(diametre_hublot - diametre_hublot // 6)
            setPenColor('black')
            penUp()
            forward(1.85 * diametre_hublot)

    def cabine():
        for _ in range(2):
            penDown()
            setFillColor(couleur_cabine)
            startPath()
            right(90)
            forward(longueur_cabine)
            right(90)
            forward(hauteur_cabine)
            fillPath()
        penUp()

    def fenetre():
        for _ in range(5):
            for _ in range(2):
                setFillColor(couleur_fenetre)
                startPath()
                penDown()
                right(90)
                forward(longueur_fenetre)
                right(90)
                forward(hauteur_fenetre)
                fillPath()
                penUp()
            right(90)
            forward(1.52 * longueur_fenetre)
            left(90)

    def toit_cabine():
        penDown()
        setFillColor(couleur_toit)
        startPath()
        for _ in range(2):
            right(90)
            forward(longueur_toit)
            right(90)
            forward(hauteur_toit)
        fillPath()
        penUp()

    def cheminee():
        for _ in range(3):
            penDown()
            setFillColor(couleur_base_cheminee)
            startPath()
            for loop in range(2):
                right(90)
                forward(longueur_cheminee)
                right(90)
                forward(hauteur_cheminee1)
            fillPath()
            penUp()
            forward(hauteur_cheminee2)
            penDown()
            setFillColor(couleur_haut_cheminee)
            startPath()
            for loop in range(2):
                right(90)
                forward(longueur_cheminee)
                right(90)
                forward(hauteur_cheminee2)
            fillPath()
            penUp()
            right(90)
            forward(longueur_cheminee)
            right(90)
            forward(hauteur_cheminee1 + hauteur_cheminee2)
            left(90)
            forward(longueur_cabine * 0.2)
            left(90)
            forward(hauteur_cheminee1)
    coque_bateau()
    back(diagonale / 2)
    left(53.13)
    forward(diametre_hublot)
    hublot()
    left(90)
    forward(hauteur_coque / 2)
    right(90)
    forward(Gbase_bateau / 35)
    left(180)
    forward(Gbase_bateau * 1 / 3 / 1.5 + longueur_cabine)
    right(90)
    forward(hauteur_cabine)
    cabine()
    right(180)
    forward(0.9 * hauteur_fenetre)
    left(90)
    forward(0.52 * longueur_fenetre)
    left(90)
    fenetre()
    forward(0.52 * longueur_fenetre)
    left(90)
    forward(longueur_cabine + (longueur_toit - longueur_cabine) / 2)
    right(90)
    toit_cabine()
    forward(hauteur_cheminee1)
    right(90)
    forward((longueur_toit - longueur_cabine) / 2 + hauteur_toit * 2)
    left(90)
    cheminee()

# --- from batiment.py ---
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

# --- from chalet.py ---
def chalet(base_chalet, couleur_toit, couleur_facade,couleur_fenetre):
    setPenWidth(1)
    setPenColor('black')
    hideTurtle()

    def rectangle(base, hauteur, couleur):
        penDown()
        setFillColor(couleur)
        startPath()
        for _ in range(2):
            forward(hauteur)
            right(90)
            forward(base)
            right(90)
        fillPath()
        penUp()

    def demi_carre(base, couleur):
        cote = sqrt(base ** 2 / 2)
        penDown()
        setFillColor(couleur)
        startPath()
        right(45)
        forward(cote)
        right(90)
        forward(cote)
        right(135)
        forward(base)
        penUp()
        fillPath()
    hauteur_chalet = base_chalet * 3 / 5
    cote_fenetre = base_chalet * 1 / 5
    base_porte = cote_fenetre
    hauteur_porte = base_porte * 2
    base_toit = base_chalet * 12 / 10
    rectangle(base_chalet, hauteur_chalet, couleur_facade)
    forward(hauteur_chalet * 1 / 3)
    right(90)
    forward(base_chalet * 1 / 5)
    left(90)
    rectangle(cote_fenetre, cote_fenetre, couleur_fenetre)
    back(hauteur_chalet * 1 / 3)
    right(90)
    back(base_chalet * 1 / 5)
    forward(base_chalet * 3 / 5)
    left(90)
    rectangle(base_porte, hauteur_porte, 'brown')
    right(90)
    back(base_chalet * 3 / 5)
    left(90)
    forward(hauteur_chalet)
    left(90)
    forward(base_chalet * 1 / 10)
    right(90)
    demi_carre(base_toit, couleur_toit)

# --- from chateau.py ---
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

# --- from dameuse.py ---
def dessine_dameuse(longueur, couleur_1, couleur_2, couleur_6):
    setPenWidth(2)
    setPenColor('black')
    hideTurtle()

    def cabine(longueur, largeur, couleur_1):
        penDown()
        setPenColor(couleur_1)
        setFillColor(couleur_1)
        startPath()
        for loop in range(2):
            forward(longueur)
            right(90)
            forward(largeur)
            right(90)
        fillPath()
        penUp()

    def deplacement_1(longueur, largeur):
        forward(longueur / 2.5)
        right(90)
        forward(largeur / 2.85)

    def vitre(longeur, largeur, couleur, cathete_1):
        hypothenuse = sqrt(cathete_1 ** 2 + largeur ** 2)
        penDown()
        setPenColor(couleur_2)
        setFillColor(couleur_2)
        startPath()
        for loop in range(2):
            forward(largeur)
            left(90)
            forward(longeur)
            left(90)
        right(36.87)
        forward(hypothenuse)
        left(126.87)
        forward(cathete_1)
        fillPath()
        penUp()

    def deplacement_2(longueur, hauteur, couleur_2):
        left(90)
        forward(longueur)
        right(90)
        forward(hauteur)
        left(90)
        setPenColor(couleur_2)
        penDown()

    def cache_moteur(longueur, largeur, couleur_2, cathete_1):
        hypothenuse = sqrt(cathete_1 ** 2 + largeur ** 2)
        setFillColor(couleur_1)
        startPath()
        for loop in range(2):
            forward(longueur)
            left(90)
            forward(largeur)
            left(90)
        penUp()
        forward(longueur)
        left(90)
        right(36.87)
        forward(hypothenuse)
        left(126.87)
        forward(cathete_1)
        fillPath()
        penUp()
        fillPath()

    def deplacement_3(largeur, longueur, width):
        penDown()
        setPenColor('black')
        setPenWidth(width)
        backward(largeur)
        forward(longueur)
        backward(longueur)

    def fraise_lisseur(D_fraise, longueur_lisseur, couleur_3, couleur_4,
        width, x, y):
        setPenColor('black')
        right(180)
        setPenWidth(width)
        forward(x)
        left(45)
        forward(y)
        right(45)
        setPenColor(couleur_3)
        setPenWidth(1)
        dot(D_fraise)
        left(90)
        forward(D_fraise / 2.2)
        right(90)
        setPenWidth(width)
        setPenColor(couleur_4)
        forward(longueur_lisseur)
        setPenColor('black')

    def deplacement_4(deplacement):
        penUp()
        backward(deplacement)

    def rectangle(longueur, diametre, width):
        setPenWidth(width)
        penDown()
        for loop in range(2):
            forward(longueur)
            right(90)
            penUp()
            forward(diametre)
            right(90)
            penDown()

    def demi_arc_de_cerle(diametre):
        pas = diametre / 115
        for loop in range(180):
            forward(pas)
            left(180 / 180)

    def chenille(longueur, largeur, diametre, width):
        rectangle(longueur, largeur, width)
        right(180)
        demi_arc_de_cerle(diametre)
        penUp()
        forward(longueur)
        penDown()
        demi_arc_de_cerle(diametre)
        penUp()

    def roue(deplacement, D_roue, espace):
        penUp()
        right(270)
        forward(deplacement)
        right(90)
        for loop in range(5):
            dot(D_roue)
            forward(espace)

    def chenille_entiere(longueur, largeur, deplacement, D_roue, espace,
        diametre, width):
        chenille(longueur, largeur, diametre, width)
        roue(deplacement, D_roue, espace)

    def pelle(longueur, largeur, couleur_5, cathete_1, deplacement,
        L_rectangle, x, L_piston_1, L_piston_2, y, width):
        hypothenuse = sqrt(cathete_1 ** 2 + largeur ** 2)
        setPenWidth(1)
        backward(deplacement)
        right(90)
        forward(cathete_1)
        left(180)
        setPenColor(couleur_5)
        setFillColor(couleur_5)
        startPath()
        for loop in range(2):
            forward(longueur)
            right(90)
            forward(largeur)
            right(90)
        forward(L_rectangle)
        right(126.87)
        forward(hypothenuse)
        right(36.87)
        penUp()
        fillPath()
        setPenWidth(width)
        right(110)
        forward(x)
        penDown()
        forward(L_piston_1)
        backward(L_piston_1)
        left(90)
        forward(y)
        right(105)
        forward(L_piston_2)

    def deplacement_5(hauteur, largeur):
        penUp()
        right(75)
        forward(hauteur)
        left(90)
        forward(largeur)

    def gyrophare(hauteur, couleur_6):
        setPenWidth(1)
        penDown()
        setPenColor(couleur_6)
        setFillColor(couleur_6)
        startPath()
        for loop in range(4):
            forward(hauteur)
            right(90)
        fillPath()
        right(90)
        forward(hauteur)
        left(90)
        forward(hauteur / 2)
        dot(hauteur + 1)
    cabine(longueur / 2, longueur / (8 / 3), couleur_1)
    deplacement_1(longueur / (8 / 3), longueur / 2)
    vitre(longueur / 4, longueur / (16 / 3), couleur_2, longueur / (64 / 9))
    deplacement_2(longueur / (400 / 145), longueur / (80 / 3), couleur_1)
    cache_moteur(longueur / 4, longueur / (16 / 3), couleur_1, longueur / (
        64 / 9))
    deplacement_3(longueur / (8 / 3), longueur, longueur / 80)
    fraise_lisseur(longueur / 8, longueur / 6.5, 'red', 'yellow', longueur /
        (400 / 7), longueur / 20, longueur / (40 / 9))
    deplacement_4(longueur / (80 / 111))
    chenille_entiere(longueur, longueur / (16 / 3), longueur / (119 / 11), 
        longueur / (200 / 33), longueur / 4, longueur / (16 / 3), longueur /
        (200 / 3))
    pelle(longueur / (20 / 3), longueur / (32 / 3), 'black', longueur / 10,
        longueur / (40 / 3), longueur / (40 / 9), longueur / 40, longueur /
        (400 / 70), longueur / (200 / 33), longueur / 10, longueur / (200 / 3))
    deplacement_5(longueur / (80 / 49), longueur / 4)
    left(4)
    gyrophare(longueur / (80 / 3), couleur_6)

# --- from eglise.py ---
def eglise(largeur, couleur_nef, couleur_clocher, couleur_toit, couleur_horloge="white"):
    setPenWidth(1)
    setPenColor('black')
    hideTurtle()

    def rectangle(hauteur, base, couleur):
        setFillColor(couleur)
        startPath()
        penDown()
        for _ in range(2):
            forward(hauteur)
            right(90)
            forward(base)
            right(90)
        fillPath()
        penUp()

    def demi_carre(cote, couleur):
        penDown()
        hypotenuse = sqrt(cote ** 2 + cote ** 2)
        setFillColor(couleur)
        startPath()
        forward(hypotenuse)
        right(180 - 45)
        forward(cote)
        right(90)
        forward(cote)
        fillPath()
        penUp()
    
    def fleche(base,hauteur,couleur) :
        angle_base = degrees(atan(hauteur / (base * 0.5)))
        angle_sommet = 180 - 2 * angle_base
        hypotenuse = sqrt((base / 2) ** 2 + hauteur ** 2)

        penDown()
        setFillColor(couleur)
        startPath()
        right(90 - angle_base)
        forward(hypotenuse)
        right(180 - angle_sommet)
        forward(hypotenuse)
        right(180 - angle_base)
        forward(base)
        fillPath()
        penUp()
        
    #nef
    hauteur_nef = 3 / 8 * largeur
    base_nef = 3 / 4 * largeur
    rectangle(hauteur_nef,base_nef,couleur_nef)
    
    #toit nef
    hauteur_toit = 2 / 3 * hauteur_nef
    largeur_toit = base_nef - hauteur_toit
    forward(hauteur_nef)
    right(45)
    demi_carre(hauteur_toit,couleur_toit)
    back(hauteur_toit)
    right(90)
    rectangle(hauteur_toit, largeur_toit,couleur_toit)
    
    #clocher
    hauteur_clocher = 3 / 4 * largeur
    base_clocher = largeur / 4
    back(hauteur_nef)
    right(90)
    forward(largeur / 2)
    left(90)
    rectangle(hauteur_clocher,base_clocher,couleur_clocher)

    #flèche
    hauteur_fleche = 2 * base_clocher
    forward(hauteur_clocher)
    fleche(base_clocher,hauteur_fleche,couleur_toit)
    
    #horloge
    back(base_clocher * 0.5)
    left(90)
    forward(1 / 2 * base_clocher)
    setPenColor(couleur_horloge)
    dot(2 / 5 * base_clocher)

# --- from eolienne.py ---
def eolienne(hauteur, couleur_base, couleur_helice, orientation):
    setPenWidth(1)
    setPenColor('black')
    hideTurtle()

    def pale(taille, couleur):
        penDown()
        petit_angle = degrees(atan(3 / 4))
        grand_angle = 90 - petit_angle
        setPenColor(couleur)
        setFillColor(couleur)
        startPath()
        forward(taille)
        right(180 - grand_angle)
        forward(0.6 * taille)
        right(90)
        forward(0.8 * taille)
        right(180 - petit_angle)
        fillPath()
        penUp()

    def helice(taille, couleur, orientation):
        setHeading(orientation)
        for _ in range(4):
            pale(taille, couleur)
            right(90)
    alpha = 5
    longueur_grand_cote = hauteur / cos(radians(5))
    longueur_petit_cote = tan(radians(5)) * hauteur
    right(5)
    setFillColor(couleur_base)
    startPath()
    forward(longueur_grand_cote)
    right(170)
    forward(longueur_grand_cote)
    right(95)
    forward(2 * longueur_petit_cote)
    fillPath()
    right(95)
    penUp()
    forward(longueur_grand_cote)
    helice(hauteur / 2, couleur_helice, orientation)
    setHeading(0)

# --- from fusee.py ---
def fusee(taille, couleur_base, couleur_aile, rapport_feu, couleur_feu):
    setPenWidth(2)
    setPenColor('black')
    hideTurtle()
    petite_base = taille
    grande_base = taille * 4
    largeur_rectangle = taille * 2
    longueur_rectangle = taille * 3.3333333
    base_triangle = taille * 1.66666666
    hauteur_trapeze = taille * 1.3333333
    hauteur_trapeze2 = taille * 0.666666666
    diametre_fenetre = taille * 1.2
    longueur_feu = rapport_feu * taille
    epaisseur_feu = grande_base / 3

    def trapeze(petite_base, grande_base, hauteur):
        alpha = degrees(atan(3 / 4))
        beta = 90 - alpha
        mini_cote = (grande_base - petite_base) / 2
        hypothenuse = sqrt(mini_cote ** 2 + hauteur ** 2)
        penDown()
        right(alpha)
        forward(hypothenuse)
        right(beta)
        forward(petite_base)
        right(beta)
        forward(hypothenuse)
        right(alpha + 90)
        forward(petite_base + 2 * mini_cote)
        right(90 + alpha)
        forward(hypothenuse)
        left(alpha)
        penUp()

    def rectangle(petite_base, longueur_rectangle, couleur):
        penDown()
        setFillColor(couleur)
        startPath()
        for _ in range(2):
            forward(longueur_rectangle)
            right(90)
            forward(petite_base)
            right(90)
        fillPath()
        penUp()

    def triangle(base):
        angle1 = 26.6
        angle2 = 63.4
        demi_base = base / 2
        hypotenuse = sqrt(demi_base ** 2 + base ** 2)
        penDown()
        right(angle1)
        forward(hypotenuse)
        right(180 - 2 * angle1)
        forward(hypotenuse)
        right(180 - angle2)
        forward(base)
        penUp()

    def fenetre(diametre, couleur):
        penDown()
        setPenColor(couleur)
        dot(diametre)

    def feu(largeur, longueur, couleur):
        penDown()
        setPenColor(couleur)
        setPenWidth(taille)
        forward(longueur)
        back(longueur)
        setPenWidth(1)
        setPenColor('black')
        penUp()
    right(180)
    feu(taille, longueur_feu, couleur_feu)
    right(90)
    forward(grande_base / 2)
    right(90)
    setFillColor(couleur_base)
    startPath()
    trapeze(largeur_rectangle, grande_base, hauteur_trapeze)
    fillPath()
    rectangle(largeur_rectangle, longueur_rectangle, 'light blue')
    forward(longueur_rectangle / 4)
    left(90)
    setFillColor(couleur_aile)
    startPath()
    triangle(base_triangle)
    fillPath()
    forward(longueur_rectangle / 4)
    left(90)
    forward(largeur_rectangle)
    left(90)
    forward(longueur_rectangle)
    left(180)
    forward(longueur_rectangle / 4)
    left(90)
    setFillColor(couleur_aile)
    startPath()
    triangle(base_triangle)
    fillPath()
    forward(longueur_rectangle / 4)
    left(90)
    forward(largeur_rectangle)
    right(90)
    setFillColor(couleur_base)
    startPath()
    trapeze(petite_base, largeur_rectangle, hauteur_trapeze2)
    fillPath()
    setFillColor(couleur_aile)
    startPath()
    triangle(petite_base)
    fillPath()
    left(180)
    forward(petite_base / 2)
    right(90)
    forward(largeur_rectangle)
    fenetre(diametre_fenetre, 'white')

# --- from fusee2.py ---
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

# --- from immeuble.py ---
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

# --- from montgolfiere.py ---
def montgolfiere(diametre_ballon, couleur_panier, couleur_ballon, couleur_sac):
    setPenWidth(2)
    setPenColor('black')
    hideTurtle()
    largeur_panier = diametre_ballon / 4
    longueur_corde = diametre_ballon / 3

    def panier(largeur_panier, couleur_panier):
        for loop in range(2):
            setPenColor(couleur_panier)
            setFillColor(couleur_panier)
            startPath()
            forward(largeur_panier)
            right(90)
            forward(2 * largeur_panier)
            right(90)
            fillPath()

    def faisceau_corde_gauche(longueur_corde):
        penDown()
        setPenColor('black')
        left(25)
        forward(longueur_corde)
        back(longueur_corde)
        right(25 + 90)
        penUp()

    def faisceau_corde_droite(longueur_corde):
        setPenColor('black')
        penDown()
        left(65)
        forward(longueur_corde)
        back(longueur_corde)
        right(65 + 90)
        penUp()

    def faisceau_corde_centre(longueur_corde):
        penDown()
        left(90)
        forward(longueur_corde * 0.9063)
        back(longueur_corde * 0.9063)
        right(90)
        penUp()

    def sac_montgolfiere(couleur_sac):
        forward(largeur_panier / 2)
        right(90)
        forward(largeur_panier / 4)
        left(90)
        penDown()
        setPenColor(couleur_sac)
        setFillColor(couleur_sac)
        startPath()
        forward(largeur_panier / 4)
        right(90)
        for loop in range(3):
            forward(largeur_panier / 2)
            right(90)
        forward(largeur_panier / 4)
        fillPath()
        penUp()

    def sac_montgolfiere_deux(couleur_sac):
        right(90)
        forward(largeur_panier)
        left(90)
        penDown()
        setPenColor(couleur_sac)
        setFillColor(couleur_sac)
        startPath()
        forward(largeur_panier / 4)
        right(90)
        for loop in range(3):
            forward(largeur_panier / 2)
            right(90)
        forward(largeur_panier / 4)
        fillPath()
        penUp()
    panier(largeur_panier, couleur_panier)
    sac_montgolfiere(couleur_sac)
    sac_montgolfiere_deux(couleur_sac)
    left(90)
    forward(diametre_ballon / 3.2)
    right(90)
    forward(largeur_panier / 2)
    faisceau_corde_gauche(longueur_corde)
    forward(largeur_panier)
    faisceau_corde_centre(longueur_corde)
    forward(largeur_panier)
    faisceau_corde_droite(longueur_corde)
    forward(largeur_panier)
    right(90)
    forward(2 * largeur_panier)
    right(90)
    forward(largeur_panier)
    right(90)
    forward(largeur_panier)
    left(90)
    forward(longueur_corde * 0.9063 * 2)
    setPenColor(couleur_ballon)
    dot(diametre_ballon)

# --- from moulin.py ---
def moulin(largeur, angle, couleur_toit, couleur_pan, couleur_fenetre,
    couleur_bat, couleur_porte):
    setPenWidth(1)
    setPenColor('black')
    hideTurtle()

    def toit(couleur_toit, largeur):
        right(90)
        setFillColor(couleur_toit)
        startPath()
        for _ in range(3):
            forward(largeur)
            left(120)
        left(90)
        fillPath()

    def pan(couleur_pan, largeur):
        angle = 360 / 12
        setFillColor(couleur_pan)
        startPath()
        for _ in range(4):
            right(angle)
            forward(largeur * 1.5)
            right(90 + angle / 2)
            forward(largeur * 0.78)
            right(90 + angle / 2)
            forward(largeur * 1.5)
            left(180 - angle)
        fillPath()

    def fenetre(couleur_fenetre, largeur):
        setPenColor(couleur_fenetre)
        dot(largeur / 2)

    def batiment(couleur_bat, largeur):
        gamma = atan(0.3 * largeur / (2.5 * largeur))
        alpha = degrees(gamma)
        longueur = sqrt((0.3 * largeur) ** 2 + (2.5 * largeur) ** 2)
        setFillColor(couleur_bat)
        startPath()
        left(180 - alpha)
        forward(longueur)
        left(90 + alpha)
        forward(largeur * 1.6)
        left(90 + alpha)
        forward(longueur)
        left(90 - alpha)
        forward(largeur)
        fillPath()

    def porte(couleur_porte, largeur):
        setFillColor(couleur_porte)
        startPath()
        for _ in range(2):
            forward(largeur)
            right(90)
            forward(largeur * 0.5)
            right(90)
        fillPath()
    gamma = atan(0.3 * largeur / (2.5 * largeur))
    alpha = degrees(gamma)
    longueur = sqrt((0.3 * largeur) ** 2 + (2.5 * largeur) ** 2)
    left(180 - alpha)
    forward(-longueur)
    setHeading(0)
    hauteura = sqrt(largeur ** 2 - (largeur / 2) ** 2) / 2.5
    hauteurb = sqrt((2.5 * largeur) ** 2 - (0.3 * largeur) ** 2)
    toit(couleur_toit, largeur)
    batiment(couleur_bat, largeur)
    right(180)
    penUp()
    forward(largeur / 2)
    left(90)
    forward(hauteura)
    back(hauteura + largeur / 2)
    fenetre(couleur_fenetre, largeur)
    forward(hauteura + largeur / 2)
    setHeading(angle)
    pan(couleur_pan, largeur)
    setHeading(0)
    penUp()
    back(hauteura + largeur / 2)
    back(hauteurb - largeur / 2)
    left(90)
    forward(largeur * 0.2)
    right(90)
    penDown()
    porte(couleur_porte, largeur)

# --- from nuage.py ---
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

# --- from sapin.py ---
def sapin(base_grand_triangle, nb_etages, couleur_sapin, couleur_boules, couleur_etoile):
    setPenWidth(1)
    setPenColor('black')
    hideTurtle()

    def tronc(base_tronc, hauteur_tronc, couleur_tronc):
        penDown()
        setFillColor('brown')
        startPath()
        lt(90)
        fd(base_tronc / 2)
        rt(90)
        fd(hauteur_tronc)
        rt(90)
        fd(base_tronc)
        rt(90)
        fd(hauteur_tronc)
        rt(90)
        fd(base_tronc / 2)
        rt(90)
        fd(hauteur_tronc)
        fillPath()
        penUp()

    def triangle(base, couleur):
        penDown()
        lt(90)
        setFillColor(couleur)
        startPath()
        fd(base / 2)
        rt(120)
        fd(base)
        rt(120)
        fd(base)
        rt(120)
        fd(base / 2)
        fillPath()
        penUp()

    def boules(nb_etages, base):
        penDown()
        for loop in range(nb_etages):
            penUp()
            back(base / 3.5 * 3)
            setPenColor('red')
            dot(base / 6)
            penUp()
            rt(90)
            fd(base / 4)
            dot(base / 6)
            penUp()
            back(base / 2)
            dot(base / 6)
            penUp()
            fd(base / 4)
            penDown()
            lt(90)
            base = base * 7 / 5
        penUp()
        fd(base / 3)
        penDown()
        for loop in range(nb_etages):
            setPenColor('red')
            dot(base / 9)
            penUp()
            fd(base / 2)
            penDown()
            base = base * 5 / 7
        penUp()

    def étoile(base,couleur):
        penDown()
        setPenColor(couleur)
        fd(base / 1.5)
        back(base / 3)
        for loop in range(8):
            rt(45)
            fd(base / 3)
            back(base / 3)
        penUp()
        
    base_tronc = base_grand_triangle / 6
    hauteur_tronc = base_tronc * 2
    tronc(base_tronc, hauteur_tronc, 'brown')

    base = base_grand_triangle
    for loop in range(nb_etages):
        triangle(base, couleur_sapin)
        rt(90)
        fd(base / 1.5)
        base = base / 7 * 5
    étoile(base,couleur_etoile)
    boules(nb_etages, base)

# --- from sapin_de_noel.py ---
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

# --- from soleil_lunettes.py ---
def soleil_a_lunettes(diametre, couleur_petits_rayons,
    couleur_grands_rayons, couleur_transition_soleil):
    setPenWidth(1)
    setPenColor('black')
    hideTurtle()

    def centre_soleil(diametre, couleur):
        penUp()
        setPenColor(couleur)
        dot(diametre)

    def triangle(cote1, cote2, couleur):
        angle = 180 - degrees(atan(cote2 / cote1))
        setFillColor(couleur)
        startPath()
        forward(cote1)
        right(angle)
        forward(sqrt(cote1 ** 2 + cote2 ** 2))
        right(180 - (angle - 90))
        forward(cote2)
        right(90)
        fillPath()

    def rayon_soleil(cote1, cote2, couleur):
        penDown()
        left(90)
        triangle(cote1, cote2, couleur)
        right(90)
        triangle(cote2, cote1, couleur)
        penUp()

    def rectangle(cote, couleur):
        setFillColor(couleur)
        startPath()
        for loop in range(2):
            forward(cote / 3)
            right(90)
            forward(cote)
            right(90)
        fillPath()

    def demi_cercle(cote, couleur):
        pas = pi * cote / 360
        setFillColor(couleur)
        startPath()
        for loop in range(360 // 2):
            forward(pas)
            right(360 / 360)
        right(90)
        fillPath()

    def branche_lunettes(longueur, epaisseur):
        setPenWidth(epaisseur)
        forward(longueur)

    def verre_lunettes(cote, couleur):
        rectangle(cote, couleur)
        right(270)
        back(cote)
        left(90)
        demi_cercle(cote, couleur)
        forward(cote)

    def lunettes(cote, couleur, epaisseur):
        penDown()
        angle_branche = 110
        setPenColor(couleur)
        right(angle_branche)
        branche_lunettes(cote / 2.5, epaisseur)
        left(angle_branche)
        verre_lunettes(cote, couleur)
        branche_lunettes(cote / 3, epaisseur)
        left(90)
        verre_lunettes(cote, couleur)
        left(angle_branche - 90)
        branche_lunettes(cote / 2.5, epaisseur)
        penUp()
    for loop in range(8):
        rayon_soleil(diametre * 2 / 5, diametre * 3.5 / 5,
            couleur_petits_rayons)
        right(360 / 16)
        rayon_soleil(diametre * 2 / 5, diametre * 4.18 / 5,
            couleur_grands_rayons)
        right(360 / 16)
    centre_soleil(diametre, 'orangered')
    centre_soleil(diametre - diametre * 0.1 / 5, 'darkorange')
    centre_soleil(diametre - diametre * 0.3 / 5, 'orange')
    centre_soleil(diametre - diametre * 0.7 / 5, couleur_transition_soleil)
    centre_soleil(diametre - diametre * 1.5 / 5, couleur_grands_rayons)
    angle_placement = 67.5
    left(angle_placement)
    forward(diametre / 2)
    right(angle_placement)
    lunettes(diametre * 3 / 10, 'black', diametre * 1 / 20)

# --- from tour_eiffel.py ---
def tour_eiffel(Base, couleur_lumiere, couleur):
    setPenWidth(2)
    setPenColor('black')
    hideTurtle()

    def arc_de_cercle(diametre, couleur):
        penDown()
        setFillColor(couleur)
        startPath()
        perimetre = diametre / 2 * 2 * pi
        un_degre = perimetre / 360
        for loop in range(180):
            forward(un_degre)
            right(1)

    def trapeze1(base):
        penDown()
        hypothenuse = sqrt((base / 4) ** 2 + (base / 2 + base / 6) ** 2)
        left(90)
        forward(base / 4)
        left(180 - 70)
        forward(hypothenuse)
        left(180 - 110)
        forward(base)
        left(180 - 110)
        forward(hypothenuse)
        left(180 - 70)
        forward(base / 4)
        fillPath()
        penUp()
        back(base / 4)
        left(70)
        forward(hypothenuse)
        left(20)

    def rectangle(longueur, couleur):
        penDown()
        setFillColor(couleur)
        startPath()
        largeur = longueur // 10
        for loop in range(2):
            forward(largeur)
            right(90)
            forward(longueur)
            right(90)
        fillPath()
        penUp()
        forward(largeur)

    def barrieres(Base, couleur):
        startPath()
        base = Base / 10 * 8
        hauteur = Base // 10
        cote = sqrt(hauteur ** 2 + (Base // 10) ** 2)
        fillPath()
        penUp()
        right(90)
        forward((Base - base) / 2)
        penDown()
        setFillColor(couleur)
        startPath()
        forward(base)
        left(45)
        forward(cote)
        left(180 - 45)
        forward(Base)
        left(180 - 45)
        forward(cote)
        fillPath()
        penUp()
        back(cote)
        left(135)

    def trapeze2(Base, couleur):
        penDown()
        Base_trapeze = Base - 2 * Base / 10
        base = Base_trapeze / 10 * 2
        hauteur = Base_trapeze * 2
        hypothenuse = sqrt((Base_trapeze / 10) ** 2 + hauteur ** 2)
        penUp()
        right(90)
        forward(Base / 10)
        left(90)
        penDown()
        setFillColor(couleur)
        startPath()
        right(90 - 78.5)
        forward(hypothenuse)
        right(180 - 101.5)
        forward(base)
        right(180 - 101.5)
        forward(hypothenuse)
        right(180 - 78.5)
        forward(Base_trapeze)
        fillPath()
        penUp()
        right(180 - 78.5)
        forward(hypothenuse)
        left(90 - 78.5)

    def socle_pointe(Base, couleur):
        penDown()
        setFillColor(couleur)
        startPath()
        Base_trapeze = Base - 2 * Base / 10
        base = Base_trapeze / 10 * 2
        hauteur = base / 3 * 4
        left(45)
        for loop in range(2):
            forward(hauteur // 8)
            right(45)
            forward(hauteur - hauteur // 4)
            right(45)
            forward(hauteur // 8)
            right(45)
            forward(base)
            right(45)
        fillPath()
        penUp()
        forward(hauteur // 8)
        right(45)
        forward(hauteur - hauteur // 4)
        right(45)
        forward(hauteur // 8)
        left(45)

    def pointe(Base, couleur):
        penDown()
        setFillColor(couleur)
        startPath()
        Base_trapeze = Base - 2 * Base / 10
        Base = Base_trapeze / 10 * 2
        hauteur = Base / 3 * 4
        base1 = hauteur - hauteur // 4
        hauteur1 = base1 * 2
        hypothenuse = sqrt(base1 ** 2)
        right(90 - 60)
        forward(hypothenuse)
        right(180 - 60)
        forward(hypothenuse)
        right(180 - 60)
        forward(base1)
        fillPath()
        penUp()
        right(90 + 30)
        forward(hypothenuse)
        left(30)

    def lumiere(couleur_lumiere, Base):
        penDown()
        diametre = Base // 10
        setPenColor(couleur_lumiere)
        dot(diametre)
        penUp()
    arc_de_cercle(Base, couleur)
    trapeze1(Base)
    rectangle(Base, couleur)
    barrieres(Base, couleur)
    trapeze2(Base, couleur)
    socle_pointe(Base, couleur)
    pointe(Base, couleur)
    lumiere(couleur_lumiere, Base)

# ---- exported names ----
__all__ = [
    'arriere_plan',
    'batiment',
    'chalet',
    'dessine_bateau',
    'dessine_dameuse',
    'dessiner_chateau',
    'eglise',
    'eolienne',
    'fusee',
    'fusee2',
    'immeuble',
    'montgolfiere',
    'moulin',
    'nuage',
    'sapin',
    'soleil_a_lunettes',
    'tour_eiffel',
]
