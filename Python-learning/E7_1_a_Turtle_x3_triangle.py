from turtle import *

# Fonction pour dessiner un triangle d'une couleur spécifiée
def triangle(color):
    # Définit la couleur du trait de la tortue
    pencolor(color)
    
    # Dessine un triangle équilatéral
    a = 0
    while a < 3:
        a += 1  # Incrémente le compteur
        forward(150)  # Avance de 150 unités
        right(120)    # Tourne à droite de 120 degrés
    
    # Déplace la tortue à une nouvelle position pour dessiner le prochain triangle
    up()  # Lève le stylo pour ne pas dessiner de traits
    backward(170)  # Recule de 170 unités pour espacer les triangles
    down()  # Redescend le stylo pour dessiner

# Dessine un triangle vert
triangle("red")
# Dessine un triangle jaune
triangle("yellow")
# Dessine un triangle rouge
triangle("green")

done()  # Termine le dessin et garde la fenêtre ouverte


        



  
