# Importation de la bibliothèque Turtle pour le dessin
from turtle import *

# Avance de 120 unités dans la direction actuelle
forward(120)

# Tourne de 90 degrés vers la gauche
left(90)

# Change la couleur de la ligne en rouge
color('red')

# Avance de 80 unités dans la direction actuelle
forward(80)

# Réinitialise la position et l'orientation de la tortue
reset()

# Initialise la variable a à 0
a = 0

# Boucle qui s'exécute tant que a est inférieur à 12
while a < 12:
    # Incrémente a de 1
    a = a + 1
    
    # Avance de 150 unités dans la direction actuelle
    forward(150)

    # Tourne de 150 degrés vers la gauche
    left(150)
