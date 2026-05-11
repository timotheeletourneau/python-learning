import sys  # Permet de modifier le chemin d'accès pour trouver le module
sys.path.append(r"D:\Python\ProjetPython\Modules_de_fonction")    
# Ajoute le dossier contenant 'dessins_tortue.py' pour pouvoir l'importer

from E7_6_7_8_b_Foncti_turtle import carre, triangle  # Importe les deux fonctions du module
from turtle import *  # Importe les commandes Turtle (goto, forward, up, down, done...)

up()              # Relève le crayon pour déplacer la tortue sans dessiner
goto(-360, 0)     # Positionne la tortue vers la gauche de l’écran (point de départ)

# Paramètres pour les carrés
taille_c = [20, 30, 40, 50, 60]  # Liste des tailles pour chaque carré
angle_c = 90                     # Angle du carré (90° = angles droits)
couleur_c = "red"                # Couleur du carré

# Paramètres pour les triangles
taille_t = [21, 31, 41, 51, 61]  # Liste des tailles pour chaque triangle
angle_t = 120                    # Angle du triangle (120° pour un triangle équilatéral)
couleur_t = "blue"               # Couleur du triangle

# Boucle pour dessiner une série de carrés et triangles alignés
for i in range(5):
    
    down()  # Abaisse le crayon pour commencer à dessiner
    
    carre(taille_c[i], couleur_c, angle_c)  # Dessine un carré
    up()  # Relève le crayon
    forward(taille_c[i] + 4)  # Avance un peu pour espacer
    
    down()# Redescend le crayon
    triangle(taille_t[i], couleur_t, angle_t)  # Dessine un triangle
    up()  # Relève à nouveau le crayon
    forward(taille_t[i] + 5)  # Avance pour le prochain couple carré + triangle

done()  # Termine le dessin et garde la fenêtre ouverte
