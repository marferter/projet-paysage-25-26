# Auto-generated combined module
# Source folder: paysage
# Generated: 2026-03-02T17:32:06.406556Z
# NOTE: top-level calls have been skipped. Review warnings printed during generation.

# ---- imports (deduplicated) ----
from gturtle import *
from math import sin, radians
from math import sqrt
from math import pi
from math import sqrt, degrees, atan
from math import cos, tan, atan, radians, degrees
from math import atan, degrees
from math import pi, atan, degrees, sin
from math import radians, sqrt, tan
from math import atan, degrees, pi, sqrt

# ---- collected definitions / assignments ----

# --- from alien.py ---
def alien(couleur, taille, phase_bras):

    def ligne_sinus(longueur,epaisseur,dephasage=0,frequence=10, amplitude=5):
        pas = 1
        iterations = int(longueur / pas)
        
        for _ in range(iterations):
            penUp()
            forward(pas)
            left(90)
            print()
            forward(sin(dephasage + radians(_) * frequence) * amplitude)
            dot(epaisseur)
            back(sin(dephasage + radians(_) * frequence) * amplitude)
            right(90)

    setPenWidth(1)
    setPenColor(couleur)
    hideTurtle()
    
    #enregistrer les coordonnées et orientation de début pour pouvoir revenir au centre pour faire les bras
    centre_x,centre_y = getPos()
    orientation = heading()

    #corps et tête
    dot(taille)
    penUp()
    forward(taille / 1.4)
    penDown()
    dot(taille / 1.7)

    #oeil
    setPenColor("white")
    dot(taille / 4)
    setPenColor("black")
    dot(taille / 8)
    left(45)

    #antennes
    for loop in range(3):
        setPenColor(couleur)
        penUp()
        forward(taille / 3.2)
        penDown()
        setPenWidth(taille // 12)
        forward(taille / 4.5)
        dot(taille / 8)
        penUp()
        back(taille / 3.2 + taille / 4.5)
        right(45)

    #jambes
    left(90)
    back(taille + taille / 4.5)
    penDown()
    left(90)
    forward(taille / 10)
    left(90)
    forward(taille / 3)
    right(90)
    forward(taille / 5)
    back(taille / 5)
    left(90)
    back(taille / 3)
    left(90)
    forward(taille / 5)
    right(90)
    forward(taille / 3)
    left(90)
    forward(taille / 5)
    penUp()

    #bras droit
    setPos(centre_x,centre_y)
    setHeading(orientation)
    right(90)
    forward(taille / 2)
    ligne_sinus(taille * 0.8,taille / 10,phase_bras,frequence=10, amplitude=5)
        
    #bras gauche
    setPos(centre_x,centre_y)
    right(180)
    forward(taille / 2)
    ligne_sinus(taille * 0.8,taille / 10,phase_bras,frequence=10, amplitude=5)
"""
Docstring – fonction `alien`

Paramètres
----------
couleur : str
        Nom ou code de couleur accepté par `gturtle` (ex. "red", "#RRGGBB"). Sert à définir la couleur du trait,
        des points et des éléments du corps de l'alien.
taille : int ou float
        Taille de base de l'alien (unités en pixels/units de `gturtle`). Utilisée comme facteur d'échelle pour
        le corps (`dot`), les yeux, les antennes, les jambes et la longueur des bras. Doit être strictement
        supérieure à 0 pour obtenir un rendu correct.
phase_bras : int ou float
        Paramètre qui permet de contrôler la phase de la sinusoïde utilisée pour dessiner les bras de l'alien. Il pourrait être utilisé pour créer une animation ou pour différencier la position des bras entre plusieurs aliens.

Fonction interne
-----------------
ligne_sinus(longueur, epaisseur, dephasage=0, frequence=10, amplitude=5)
        Fonction locale qui trace un ensemble de points suivant une variation sinusoïdale le long d'une
        longueur donnée.

        longueur : int ou float
                Longueur totale parcourue le long de l'axe principal (unités `gturtle`). Si `longueur < 1`,
                la fonction n'itérera pas et aucun point ne sera tracé.
        epaisseur : int ou float
                Diamètre (ou taille) des points tracés par `dot` le long de la sinusoïde. Doit être positif.
        dephasage : int ou float, optionnel
                Décalage angulaire (en degrés convertis via `radians`) appliqué à la sinusoïde.
        frequence : int ou float, optionnel
                Facteur multiplicatif de la fréquence de la sinusoïde (plus grand → plus d'oscillations).
        amplitude : int ou float, optionnel
                Amplitude (en unités `gturtle`) de la variation sinusoïdale en ordonnée.

Valeurs limites et mises en garde
---------------------------------
- `taille` doit être strictement > 0. Une valeur nulle ou négative produit des formes incohérentes
    (points de taille nulle, déplacements négatifs inattendus).
- `longueur`, `epaisseur`, `amplitude` doivent être des nombres réels; `epaisseur` et `longueur`
    négatifs peuvent empêcher le tracé ou provoquer des déplacements non souhaités.
- L'itération dans `ligne_sinus` utilise `pas = 1` et `iterations = int(longueur / pas)`. Si
    `longueur < 1`, `iterations == 0` et aucun point n'est dessiné.
- Des fréquences très élevées ou une amplitude très grande peuvent dessiner hors du canevas visible.
- Si `couleur` n'est pas reconnue par `gturtle`, l'appel à `setPenColor` peut lever une erreur ou
    produire un rendu inattendu selon l'implémentation de `gturtle` utilisée.
- Les paramètres doivent être de types numériques appropriés (int/float) ; passer d'autres types
    peut lancer des exceptions (TypeError, ValueError).
- `phase_bras` est ignoré dans le code actuel : lui attribuer une valeur n'a aucun effet.
"""

# --- from arriere_plan.py ---
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

# --- from bateau.py ---
def bateau(Gbase_bateau, couleur_coque, couleur_cabine,
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
"""
bateau(Gbase_bateau, couleur_coque, couleur_cabine,
               couleur_fenetre, couleur_toit, couleur_base_cheminee,
               couleur_haut_cheminee)

Dessine un bateau de croisière vu de côté, composé d'une coque,
d'une cabine avec fenêtres et hublots, d'un toit de cabine et de
cheminées.

Paramètres :
    Gbase_bateau          : longueur totale du bateau (en pixels).
                            C'est la dimension principale ; toutes les
                            autres proportions (hauteur de coque, taille
                            des hublots, dimensions de la cabine, etc.)
                            en découlent.
    couleur_coque         : couleur de la coque (partie inférieure du bateau).
    couleur_cabine        : couleur des murs de la cabine (superstructure).
    couleur_fenetre       : couleur des fenêtres de la cabine.
    couleur_toit          : couleur du toit de la cabine.
    couleur_base_cheminee : couleur de la partie basse des cheminées.
    couleur_haut_cheminee : couleur de l'anneau supérieur des cheminées.

Position initiale de la tortue :
    La tortue part depuis la position par défaut (origine), au coin
    inférieur gauche de la coque, orientée vers le haut (nord).
    Le dessin de la coque commence par un virage à droite de 90°
    pour tracer la base du bateau vers la droite.
"""

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
"""
chalet(base_chalet, couleur_toit, couleur_facade, couleur_fenetre)

Dessine un chalet de montagne vu de face, avec une façade rectangulaire,
une fenêtre carrée, une porte en bois et un toit en demi-carré (45°).

Paramètres :
    base_chalet     : largeur de la façade du chalet (en pixels).
                      La hauteur de la façade (3/5 de la base), la taille
                      de la fenêtre (1/5 de la base), la taille de la porte
                      et la base du toit (12/10 de la base) en découlent.
    couleur_toit    : couleur du toit triangulaire.
    couleur_facade  : couleur des murs de la façade.
    couleur_fenetre : couleur de la fenêtre carrée.

Position initiale de la tortue :
    La tortue part depuis la position par défaut (origine), au coin
    inférieur gauche de la façade, orientée vers le haut (nord).
"""

# --- from chateau.py ---
def chateau(taille=1, couleur_tours='gray', couleur_fenetre='lightblue'):
    setPenWidth(1)
    setPenColor('black')
    hideTurtle()

    def tour(hauteur, largeur_creneaux, nbr_creneaux):
        penDown()
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
        penUp()

    def fenetre_triangle(longueur=15):
        penDown()
        for _ in range(3):
            fd(longueur * taille)
            lt(120)
        penUp()

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
        penDown()
        fd(largeur * taille)
        lt(90)
        fd(hauteur * taille)
        for _ in range(18):
            fd(largeur * pi / 36 * taille)
            rt(10)
        penUp()
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
    pu()
    fd(250 * taille)
    bk(45 * taille)
    lt(90)
    fd(30 * taille)
    rt(90)
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
    fenetre_tour(3,30,couleur_fenetre)
    pu()
    rt(90)
    fd(120 * taille)
    lt(90)
    fd(70 * taille)
    setPenColor('saddlebrown')
    setFillColor('saddlebrown')
    startPath()
    porte_chateau(35, 20)
    fillPath()
"""
chateau(taille=1, couleur_tours='gray', couleur_fenetre='lightblue')

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

# --- from dameuse.py ---
def dameuse(longueur, couleur_1, couleur_2, couleur_6):
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
"""
dameuse(longueur, couleur_1, couleur_2, couleur_6)

Dessine une dameuse (engin de damage des pistes de ski) vue de côté,
avec sa cabine, sa vitre, son cache-moteur, sa chenille, sa fraise
de damage, sa pelle et son gyrophare.

Paramètres :
    longueur  : longueur totale de la dameuse (en pixels).
                C'est la dimension de référence ; toutes les autres
                proportions (hauteur de la cabine, taille de la fraise,
                diamètre des roues, longueur de la chenille, etc.)
                en sont dérivées.
    couleur_1 : couleur principale du corps de la dameuse (cabine et
                cache-moteur).
    couleur_2 : couleur de la vitre/pare-brise de la cabine.
    couleur_6 : couleur du gyrophare situé sur le toit de la cabine.

Position initiale de la tortue :
    La tortue part depuis la position par défaut (origine), au coin
    inférieur gauche de la cabine, orientée vers le haut (nord).
"""

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
"""
eglise(largeur, couleur_nef, couleur_clocher, couleur_toit,
       couleur_horloge='white')

Dessine une église vue de face, composée d'une nef rectangulaire avec
son toit triangulaire, d'un clocher surmonté d'une flèche et d'une
horloge circulaire.

Paramètres :
    largeur         : largeur totale de l'église (en pixels).
                      La hauteur de la nef (3/8 de la largeur), la base
                      de la nef (3/4 de la largeur), la hauteur du clocher
                      (3/4 de la largeur) et toutes les autres dimensions
                      en découlent.
    couleur_nef     : couleur des murs de la nef (corps principal).
    couleur_clocher : couleur des murs du clocher (tour).
    couleur_toit    : couleur du toit de la nef et de la flèche du clocher.
    couleur_horloge : couleur de l'horloge sur le clocher (blanc par défaut).

Position initiale de la tortue :
    La tortue part depuis la position par défaut (origine), au coin
    inférieur gauche de la nef, orientée vers le haut (nord).
"""

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
"""
eolienne(hauteur, couleur_base, couleur_helice, orientation)

Dessine une éolienne vue de face, composée d'un mât légèrement incliné
et d'un rotor à quatre pales.

Paramètres :
    hauteur        : hauteur du mât de l'éolienne (en pixels).
                     La taille des pales (moitié de la hauteur) et la
                     largeur de la base du mât découlent également de
                     ce paramètre.
    couleur_base   : couleur du mât (pylône).
    couleur_helice : couleur des pales du rotor.
    orientation    : angle de rotation du rotor en degrés (direction vers
                     laquelle pointe la première pale, selon le système
                     de cap de la tortue).

Position initiale de la tortue :
    La tortue part depuis la position par défaut (origine), à la base
    du mât, orientée vers le haut (nord). Le mât est légèrement incliné
    (5°) vers la droite.
"""

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
"""
fusee(taille, couleur_base, couleur_aile, rapport_feu, couleur_feu)

Dessine une fusée spatiale vue de côté, composée d'un corps trapézoïdal,
d'un corps rectangulaire bleu (avec hublot), d'ailerons triangulaires
et d'un panache de feu à la tuyère.

Paramètres :
    taille       : unité de taille de base de la fusée (en pixels).
                   La grande base du trapèze inférieur vaut 4×taille,
                   le corps rectangulaire fait 2×taille de large et
                   ~3.33×taille de long. Toutes les dimensions en découlent.
    couleur_base : couleur principale du corps de la fusée
                   (trapèzes supérieur et inférieur).
    couleur_aile : couleur des ailerons/empennages.
    rapport_feu  : longueur du panache de feu en multiples de taille
                   (ex. rapport_feu=1 → longueur_feu = 1×taille).
    couleur_feu  : couleur du panache de feu à la tuyère.

Position initiale de la tortue :
    La tortue part depuis la position par défaut (origine), à la tuyère
    (bas) de la fusée, orientée vers le haut (nord). Le premier élément
    dessiné est le panache de feu vers le bas, puis la fusée est construite
    de bas en haut.
"""

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
"""
fusee2(taille_base, couleur_primaire, couleur_secondaire,
       couleur_flammes, longueur_flammes)

Dessine une fusée spatiale stylisée vue de côté, composée d'un corps
à trois sections (deux secondaires et une principale), d'un nez
triangulaire, de flammes à la tuyère, d'ailerons triangulaires et
d'un hublot circulaire.

Paramètres :
    taille_base        : unité de taille de base de la fusée (en pixels).
                         La largeur du corps vaut 1.5×taille_base ; la
                         hauteur totale du corps vaut environ 3.33×taille_base.
                         Toutes les proportions en découlent.
    couleur_primaire   : couleur principale du corps (section centrale
                         et nez triangulaire).
    couleur_secondaire : couleur secondaire du corps (sections du bas
                         et du haut encadrant la section principale).
    couleur_flammes    : couleur des flammes à la tuyère.
    longueur_flammes   : longueur des flammes de la tuyère (en pixels).

Position initiale de la tortue :
    La tortue part depuis la position par défaut (origine), à la base
    de la tuyère (bas de la fusée), orientée vers le haut (nord).
    La première section dessinée est la partie basse du corps.
"""

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
"""
immeuble(nb_colonnes, nb_etages, cote, couleur_fenetres,
         couleur_immeuble, couleur1, couleur2, couleur3)

Dessine un immeuble vu de face, composé de colonnes de fenêtres empilées
en étages, avec une guirlande lumineuse décorative en façade.

Paramètres :
    nb_colonnes      : nombre de colonnes de fenêtres (sections verticales).
    nb_etages        : nombre de fenêtres par colonne (nombre d'étages).
    cote             : côté de chaque fenêtre carrée (en pixels).
                       Les colonnes ont une largeur de 2×cote et les
                       hauteurs d'étage de 1.5×cote.
    couleur_fenetres : couleur de remplissage des fenêtres.
    couleur_immeuble : couleur de la façade et des encadrements.
    couleur1         : première couleur des points lumineux de la guirlande.
    couleur2         : deuxième couleur des points lumineux de la guirlande.
    couleur3         : troisième couleur des points lumineux de la guirlande.

Position initiale de la tortue :
    La tortue part depuis la position par défaut (origine), au coin
    inférieur gauche de l'immeuble, orientée vers le haut (nord).
"""

# --- from meteorite.py ---
def meteorite(diametre_meteorite, couleurflamme_ext, couleurflamme_int):
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
        
    def centre_meteorite(diametre_meteorite,couleur_ext):
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
    centre_meteorite(diametre_meteorite,couleurflamme_ext)
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
'''
Météorite enflammée (gturtle)

Ce script définit une fonction `meteorite` qui dessine, avec la bibliothèque
`gturtle`, une météorite entourée de flammes (deux couches de flammes : externe
puis interne) ainsi que quelques cratères (points) sur la météorite. Le dessin
repose sur des arcs de cercle approximés par de petits segments et sur des
triangles isocèles (pour les flammes) calculés à l’aide de trigonométrie.

Paramètres
----------
diametre_meteorite : float | int
    Diamètre (en pixels) du disque principal de la météorite (le point gris
    final dans ce code). Ce paramètre sert aussi d’échelle globale : les
    diamètres des couches, les hauteurs/bases des flammes et le placement des
    cratères sont proportionnels à cette valeur.
couleurflamme_ext : str
    Couleur utilisée pour la couche de flammes externe (remplissage) et aussi
    comme couleur du disque externe de la météorite (premier `dot` de taille
    `diametre_meteorite * 1.15` dans ce code). La chaîne doit être reconnue par
    `gturtle` (nom de couleur ou spécification acceptée par l��environnement).
couleurflamme_int : str
    Couleur utilisée pour la couche de flammes interne (remplissage). La chaîne
    doit être reconnue par `gturtle`.

Notes
-----
- Le rendu dépend de l’état initial de la tortue (position et orientation) au
  moment de l’appel : la fonction ne se repositionne pas à une origine absolue.
- Les flammes sont construites à partir d’un demi-disque rempli et de trois
  triangles remplis (flamme centrale + gauche + droite). Les triangles sont
  tracés via des rotations/avancées basées sur :
  - `alpha = atan(hauteur / (base/2))` (angle au sommet par rapport à l’axe),
  - `hyp = hauteur / sin(alpha)` (longueur des côtés).
- L’arc de cercle est approximé en `n = 36` pas (constant dans ce code) ; plus
  `n` est grand, plus l’arc est lisse, mais plus il y a de segments.

Valeurs limites et mises en garde
---------------------------------
- `diametre_meteorite` doit être strictement positif (`diametre_meteorite > 0`).
  - Si `diametre_meteorite == 0`, tous les déplacements et points sont nuls et
    certaines constructions deviennent dégénérées (dessin invisible ou réduit).
  - Si `diametre_meteorite < 0`, les tailles passées à `dot()` et les distances
    de déplacement deviennent incohérentes (selon `gturtle`, cela peut ne rien
    dessiner, produire un comportement inattendu, ou inverser des déplacements).
- Trigonométrie dans le calcul des flammes :
  - `demi_base = base / 2` : dans ce code `base` est dérivé de `diametre`, donc
    attendu strictement positif. Si `base == 0`, alors `atan(hauteur / demi_base)`
    provoque une division par zéro.
  - `alpha = atan(hauteur / demi_base)` puis `hyp = hauteur / sin(alpha)` :
    si `hauteur == 0`, alors `alpha == 0` et `sin(alpha) == 0`, donc division par
    zéro. En pratique, il faut `hauteur > 0` et `base > 0` pour éviter `sin(alpha)=0`.
- Couleurs :
  - Si `couleurflamme_ext` ou `couleurflamme_int` n’est pas reconnue par `gturtle`,
    l’appel à `setPenColor` / `setFillColor` peut échouer (erreur) ou retomber sur
    une couleur par défaut selon l’implémentation ; le rendu sera alors incorrect.
- Approximation de l’arc :
  - L’arc utilise `int(angle / 360 * n) + 1` itérations. Si `angle` était nul ou
    très petit (ici il est fixé à 180 dans ce code), l’arc se réduit à peu de
    segments et la forme peut être anguleuse.
'''

# --- from montagne.py ---
def montagne(hauteur, hauteur_neige, angle, couleur, couleur_neige):
    setPenWidth(1)
    setPenColor('black')
    hideTurtle()
    angle_exterieur = 180 - angle
    neige = hauteur - hauteur_neige
    demi_basse_neige = neige * tan(radians(angle / 2))

    def triangle(hauteur, angle, couleur):
        demi_basse = hauteur * tan(radians(angle / 2))
        penDown()
        setFillColor(couleur)
        startPath()
        for loop in range(2):
            forward(sqrt(hauteur ** 2 + demi_basse ** 2))
            right(angle_exterieur)
        fillPath()
        penUp()
    demi_basse = hauteur * tan(radians(angle / 2))
    right((180 - angle_exterieur) / 2)
    triangle(hauteur, angle, couleur)
    right(angle)
    forward(sqrt(hauteur ** 2 + demi_basse ** 2))
    left(angle_exterieur)
    forward(sqrt(neige ** 2 + demi_basse_neige ** 2))
    left(180)
    triangle(neige, angle, couleur_neige)
    left(angle_exterieur)
    forward(sqrt(hauteur ** 2 + demi_basse ** 2) - sqrt(neige ** 2 + 
        demi_basse_neige ** 2))
    right((180 - angle_exterieur) / 2)
    left(180)
"""
Docstring – fonction montagne(hauteur, hauteur_neige, angle, couleur, couleur_neige)

Paramètres
----------
hauteur : (int | float)
    Hauteur totale de la montagne (grand triangle), exprimée en pixels (unités gturtle).
    Plus la valeur est grande, plus le triangle dessiné est haut.

hauteur_neige : (int | float)
    Hauteur de la partie de montagne qui reste visible (non enneigée), mesurée depuis la base.
    La hauteur effective de la calotte de neige est calculée comme :
        neige = hauteur - hauteur_neige
    Donc :
    - si hauteur_neige est proche de hauteur, il reste peu de neige (petit triangle blanc),
    - si hauteur_neige est petit, la neige occupe une grande partie du sommet.

angle : (int | float)
    Angle au sommet (en degrés) du triangle isocèle représentant la montagne (et la neige).
    Cet angle contrôle “l’ouverture” de la montagne :
    - angle petit -> montagne pointue (pentes raides),
    - angle grand -> montagne plus large (pentes douces).
    Doit être compris strictement entre 0 et 180 degrés pour que la trigonométrie (tan(angle/2))
    reste cohérente.

couleur : (str)
    Couleur de remplissage de la montagne (grand triangle).
    Doit être un nom de couleur reconnu par gturtle (ex. 'bisque', 'red', 'gray', etc.).

couleur_neige : (str)
    Couleur de remplissage de la neige (petit triangle au sommet).
    Doit être un nom de couleur reconnu par gturtle (ex. 'snow2', 'white', etc.).
"""

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
"""
montgolfiere(diametre_ballon, couleur_panier, couleur_ballon, couleur_sac)

Dessine une montgolfière vue de face, composée d'un panier rectangulaire
(nacelle), d'un brûleur (sac), de cordages en faisceau et d'un ballon
circulaire.

Paramètres :
    diametre_ballon : diamètre du ballon (en pixels).
                      Le panier a une largeur de 1/4 du diamètre et les
                      cordages une longueur de 1/3 du diamètre.
    couleur_panier  : couleur du panier (nacelle).
    couleur_ballon  : couleur du ballon.
    couleur_sac     : couleur du brûleur / sac à gaz relié au ballon.

Position initiale de la tortue :
    La tortue part depuis la position par défaut (origine), au coin
    inférieur gauche du panier, orientée vers le haut (nord).
    Le dessin commence par le panier, puis remonte vers le ballon.
"""

# --- from moulin.py ---
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
"""
moulin(largeur, angle, couleur_toit, couleur_pan, couleur_fenetre,
       couleur_bat, couleur_porte)

Dessine un moulin à vent vu de face, avec un bâtiment trapézoïdal,
un toit triangulaire, une fenêtre circulaire, une porte et des ailes
(pans) en croix.

Paramètres :
    largeur         : largeur de la base du bâtiment du moulin (en pixels).
                      La hauteur du bâtiment (1.5×largeur) et toutes les
                      autres dimensions en découlent.
    angle           : orientation des ailes du moulin en degrés (angle de
                      cap de la tortue au moment de dessiner les ailes).
    couleur_toit    : couleur du toit triangulaire.
    couleur_pan     : couleur des ailes/pales du moulin.
    couleur_fenetre : couleur de la fenêtre circulaire.
    couleur_bat     : couleur des murs du bâtiment.
    couleur_porte   : couleur de la porte d'entrée.

Position initiale de la tortue :
    La tortue part depuis la position par défaut (origine), au coin
    inférieur gauche de la base du bâtiment, orientée vers le haut (nord).
"""

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
"""
nuage(taille, couleur)

Dessine un nuage composé de plusieurs disques (cercles pleins) de
tailles décroissantes disposés autour d'un disque central.

Paramètres :
    taille  : diamètre du disque central du nuage (en pixels).
              Les disques satellites ont des diamètres proportionnels
              au disque central (0.7×taille, 0.6×taille, 0.4×taille).
    couleur : couleur du nuage (tous les disques ont la même couleur).

Position initiale de la tortue :
    La tortue part depuis la position par défaut (origine), au centre
    du disque principal du nuage. Le premier cercle est tracé à cet
    endroit, puis la tortue se déplace pour tracer les cercles satellites.
"""

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

    def etoile(base,couleur):
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
    etoile(base,couleur_etoile)
    boules(nb_etages, base)
"""
sapin(base_grand_triangle, nb_etages, couleur_sapin, couleur_boules,
      couleur_etoile)

Dessine un sapin décoré vu de face, composé d'un tronc, de plusieurs
niveaux de triangles (étages de branches), de boules de décoration et
d'une étoile au sommet.

Paramètres :
    base_grand_triangle : largeur de la base du plus grand triangle
                          (étage inférieur) du sapin (en pixels).
                          C'est la dimension de référence ; les triangles
                          des étages supérieurs sont progressivement plus
                          petits (chaque étage vaut 5/7 du précédent).
    nb_etages           : nombre de niveaux de branches triangulaires.
    couleur_sapin       : couleur de remplissage des triangles de branches.
    couleur_boules      : couleur des boules de décoration.
    couleur_etoile      : couleur de l'étoile au sommet du sapin.

Position initiale de la tortue :
    La tortue part depuis la position par défaut (origine), au bas du
    tronc, orientée vers le haut (nord). Le dessin débute par le tronc,
    puis les étages de branches sont construits de bas en haut.
"""

# --- from sapin_de_noel.py ---
def sapin_de_noel(taille):
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
"""
sapin_de_noel(taille)

Dessine un sapin de Noël décoré vu de face, composé d'un tronc,
de trois rangées de branches triangulaires (avec boules rouges),
d'ailerons latéraux triangulaires et d'une étoile dorée au sommet.

Paramètres :
    taille : taille globale du sapin (en pixels).
             Le tronc a une largeur de 1/5 de taille et une hauteur
             de 2/5 de taille. Les branches sont des triangles équilatéraux
             de côté taille. L'étoile est de côté taille/2.

Position initiale de la tortue :
    La tortue part depuis la position par défaut (origine), au coin
    inférieur gauche du tronc, orientée vers le haut (nord).
"""

# --- from soleil_a_lunettes.py ---
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
"""
soleil_a_lunettes(diametre, couleur_petits_rayons, couleur_grands_rayons,
                  couleur_transition_soleil)

Dessine un soleil avec des lunettes de soleil, composé de rayons
triangulaires alternés (petits et grands) autour d'un disque central
avec dégradé de couleur, surmonté d'une paire de lunettes.

Paramètres :
    diametre                 : diamètre du disque central du soleil
                               (en pixels). La longueur des rayons
                               est proportionnelle au diamètre
                               (petits : ~2/5 + 3.5/5, grands : ~2/5 + 4.18/5).
    couleur_petits_rayons    : couleur des rayons courts (alternés).
    couleur_grands_rayons    : couleur des rayons longs (alternés) et
                               du centre intérieur du soleil.
    couleur_transition_soleil: couleur intermédiaire du dégradé au centre
                               du soleil.

Position initiale de la tortue :
    La tortue part depuis la position par défaut (origine), au centre
    du soleil. Les rayons s'étendent depuis ce centre, puis la tortue
    revient au centre pour tracer les disques concentriques et les lunettes.
"""

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
"""
tour_eiffel(Base, couleur_lumiere, couleur)

Dessine la Tour Eiffel vue de face, composée d'un arc de cercle formant
les pieds, d'un grand trapèze, d'une plateforme rectangulaire, de
barrières inclinées, d'un second trapèze, d'un socle de flèche et d'une
pointe, avec une lumière au sommet.

Paramètres :
    Base            : largeur de la base de la Tour Eiffel (en pixels).
                      Toutes les hauteurs et largeurs des différentes
                      sections (trapèzes, rectangle de plateforme,
                      barrières, flèche) sont calculées proportionnellement
                      à cette valeur.
    couleur_lumiere : couleur de la lumière (point lumineux) au sommet
                      de la tour.
    couleur         : couleur de la structure de la tour (piliers,
                      trapèzes, plateforme, pointe).

Position initiale de la tortue :
    La tortue part depuis la position par défaut (origine), au centre
    de la base de la Tour Eiffel (entre les deux pieds), orientée vers
    le haut (nord). Le premier élément dessiné est l'arc de cercle
    formant les pieds de la tour.
"""

# ---- exported names ----
__all__ = [
    'alien',
    'arriere_plan',
    'bateau',
    'batiment',
    'chalet',
    'chateau',
    'dameuse',
    'eglise',
    'eolienne',
    'fusee',
    'fusee2',
    'immeuble',
    'meteorite',
    'montagne',
    'montgolfiere',
    'moulin',
    'nuage',
    'sapin',
    'sapin_de_noel',
    'soleil_a_lunettes',
    'tour_eiffel',
]
