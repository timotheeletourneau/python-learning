import sys  # Permet de modifier le chemin d'accès pour inclure des modules externes
sys.path.append(r"D:\Python\ProjetPython\Modules_de_fonction")  
# Ajoute le dossier où se trouve le fichier 'dessins_tortue.py' pour pouvoir l'importer

from E7_6_7_8_b_Foncti_turtle import etoile6, carre, etoile5, triangle # Importe la fonction etoile5() depuis le module
from turtle import *  # Importe toutes les commandes Turtle (forward, right, goto, etc.)

# Relève le crayon et repositionne la tortue à l'origine
up()  
goto(0, 0)  

# Définition des paramètres pour le dessin des triangles
taille_t = [18, 21, 25, 27, 31, 35, 39, 43, 47, 51]  # Tailles des triangles
angle_t = 120  # Angle pour dessiner les triangles
couleur_t = "red"  # Couleur des triangles

# Paramètres pour dessiner les étoiles
taille_e5 = [18, 21, 25, 27, 31, 35, 39, 43, 47, 51]  # Tailles des étoiles
angle_e5 = 144  # Angle pour dessiner les triangles des étoiles
couleur_e5 = "blue"  # Couleur des étoiles

# Paramètres pour dessiner les étoiles à 6 branches
taille_e6 = [18, 21, 25, 27, 31, 35, 39, 43, 47, 51, 55]  # Tailles des étoiles à 6 branches
angle_e6 = 120  # Angle pour dessiner les triangles des étoiles à 6 branches
couleur_e6 = "blue"  # Couleur des étoiles à 6 branches

# Paramètres pour dessiner les carrés
taille_c = [18, 21, 25, 27, 31, 35, 39, 43, 47, 51, 55]  # Tailles des carrés
angle_c = 90  # Angle pour dessiner les carrés
couleur_c = "red"  # Couleur des carrés

# Variables pour suivre la position et l'orientation initiale
pos0 = position()  # Position initiale de la tortue
h0 = heading()  # Orientation initiale de la tortue
angle_initiale = [0, 60, 120, 180, 240, 300, 360, 420, 480]  # Angles de départ pour chaque figure

# Boucle pour dessiner plusieurs étoiles, triangles et carrés
for i in range(9):
    down()  # Redescend le stylo pour commencer à dessiner
    etoile5(taille_e5[i], couleur_e5, angle_e5)  # Dessine l'étoile avec la taille et la couleur spécifiées
    up()  # Relève le stylo après avoir dessiné l'étoile
    forward(taille_e5[i] + 5)  # Avance pour espacer les dessins
    down()  # Redescend le stylo pour dessiner le triangle
    triangle(taille_t[i], couleur_t, angle_t)  # Dessine le triangle
    up()  # Relève le stylo après avoir dessiné le triangle
    forward(taille_t[i] + 5)  # Avance pour espacer les dessins
    setheading(angle_initiale[i])  # Change l'orientation de la tortue
    down()  # Redescend le stylo pour dessiner l'étoile à 6 branches
    etoile6(taille_e6[i], couleur_e6, angle_e6)  # Dessine l'étoile à 6 branches
    up()  # Relève le stylo après avoir dessiné l'étoile à 6 branches
    right(28)  # Tourne la tortue à droite de 28 degrés pour l'alignement
    forward(taille_e6[i] / 1.7)  # Avance pour espacer les dessins
    left(88)  # Tourne à gauche pour ajuster la position
    forward(taille_e6[i] + 5)  # Avance pour se positionner pour le carré
    down()  # Redescend le stylo pour dessiner le carré
    carre(taille_c[i], couleur_c, angle_c)  # Dessine le carré
    up()  # Relève le stylo après avoir dessiné le carré
    forward(taille_c[i] + 5)  # Avance pour espacer le carré suivant

done()  # Termine le dessin et garde la fenêtre ouverte jusqu'à un clic
