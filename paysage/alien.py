from gturtle import *
from math import sin, radians

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

if __name__ == '__main__':
    alien('red', 80,0)

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