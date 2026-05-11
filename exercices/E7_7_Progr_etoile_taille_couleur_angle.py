import sys  # Permet de modifier le chemin d'accès pour inclure des modules externes
sys.path.append(r"D:\Python\ProjetPython\Modules_de_fonction")  
# Ajoute le dossier où se trouve le fichier 'dessins_tortue.py' pour pouvoir l'importer

from E7_6_7_8_b_Foncti_turtle import etoile5  # Importe la fonction etoile5() depuis le module
from turtle import *  # Importe toutes les commandes Turtle (forward, right, goto, etc.)

up()              # Relève le crayon pour déplacer la tortue sans dessiner
goto(-360, 0)     # Positionne la tortue vers la gauche de l'écran (abscisse, ordonnée)

# --- Paramètres pour dessiner plusieurs étoiles ---
taille_e5 = [22, 32, 42, 52, 62, 52, 42, 32, 22]  # Tailles variées pour chaque étoile
angle_e5 = 144                                     # Angle typique pour une étoile à 5 branches
couleur_e5 = "blue"                                # Couleur du tracé des étoiles

# --- Boucle pour tracer une série d'étoiles ---
for i in range(9):          # Répète 9 fois, pour 9 étoiles
    down()                  # Abaisse le crayon pour commencer à dessiner
    etoile5(taille_e5[i], couleur_e5, angle_e5)  # Appelle la fonction pour dessiner une étoile
    up()                    # Relève le crayon pour se déplacer sans tracer
    forward(taille_e5[i] + 5)  # Avance pour espacer les étoiles selon leur taille

done()  # Termine le dessin et empêche la fenêtre Turtle de se fermer immédiatement
