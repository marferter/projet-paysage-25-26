from gturtle import *
from math import pi, atan, degrees, sin

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

    

if __name__ == '__main__':
    meteorite(150, 'firebrick1', 'darkOrange')

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