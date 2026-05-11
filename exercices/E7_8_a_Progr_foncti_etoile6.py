import sys  # Permet de modifier le chemin d'accès pour inclure des modules externes
sys.path.append(r"D:\Python\ProjetPython\Modules_de_fonction")
# Ajoute le dossier où se trouve le fichier 'dessins_tortue.py' pour pouvoir l'importer

from E7_6_7_8_b_Foncti_turtle import etoile6, carre # Importe la fonction etoile5() depuis le module
from turtle import *  # Importe toutes les commandes Turtle (forward, right, goto, etc.)

up()  # Relève le crayon pour déplacer la tortue sans dessiner
goto(-340, 0)  # Positionne la tortue vers la gauche de l'écran

# Paramètres pour dessiner les étoiles
taille_e6 = [40, 60, 80, 60, 40]  # Tailles des étoiles
angle_e6 = 120  # Angle pour dessiner les triangles
couleur_e6 = "blue"  # Couleur des étoiles

# Paramètres pour dessiner les carrés
taille_c = [40, 60, 80, 60, 40]  # Tailles des carrés
angle_c = 90  # Angle pour dessiner les carrés
couleur_c = "red"  # Couleur des carrés


# Variables pour suivre la position et l'orientation
pos0 = position()  # Position initiale
h0 = heading()  # Orientation initiale
angle_initiale = [-120, -60, 0, 60, 120]  # Angles de départ pour chaque étoile

# Boucle pour dessiner plusieurs étoiles et carrés
for i in range(5):
    setheading(angle_initiale[i])  # Définit l'angle de départ pour chaque étoile
    down()  # Redescend le stylo pour commencer à dessiner
    etoile6(taille_e6[i], couleur_e6, angle_e6)  # Dessine l'étoile
    up()  # Relève le stylo après avoir dessiné l'étoile
    right(28)  # Tourne la tortue à droite de 28 degrés pour l'alignement
    forward(taille_e6[i] / 1.7)  # Avance pour espacer l'étoile du carré
    left(88)  # Tourne à gauche pour ajuster la position
    forward(taille_e6[i] + 5)  # Avance pour se positionner pour le carré
    down()  # Redescend le stylo pour dessiner le carré
    carre(taille_c[i], couleur_c, angle_c)  # Dessine le carré
    up()  # Relève le stylo après avoir dessiné le carré
    forward(taille_c[i] + 5)  # Avance pour espacer le carré suivant

done()  # Termine le dessin et garde la fenêtre ouverte jusqu'à un clic

  
     
    
