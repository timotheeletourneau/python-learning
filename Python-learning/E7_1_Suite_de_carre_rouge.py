# Importation de la fonction 'carre' depuis le module 'Modules_de_fonction'
from Modules_de_fonction import carre

# Importation de toutes les fonctions du module turtle
from turtle import *

# Positionnement du curseur : lever le stylo pour ne pas dessiner
penup()  
# Déplace le curseur à la position (-150, 50) sans dessiner
goto(-150, 50)  

# Initialisation d'un compteur
i = 0  
# Boucle pour dessiner 10 carrés
while i < 10:
    # Abaisse le stylo pour commencer à dessiner
    pendown()  
    # Appelle la fonction 'carre' pour dessiner un carré de 25 unités en rouge
    carre(25, 'red')  
    # Lève le stylo pour ne pas dessiner pendant le déplacement
    penup()  
    # Déplace le curseur de 30 unités vers l'avant
    forward(30)  
    # Incrémente le compteur pour passer au prochain carré
    i += 1  

# Termine le dessin (affiche la fenêtre et attend que l'utilisateur la ferme)
done()
