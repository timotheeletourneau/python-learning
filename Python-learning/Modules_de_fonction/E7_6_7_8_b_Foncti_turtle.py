from turtle import *  # Importe toutes les fonctions du module turtle

def carre(taille, couleur, angle):
    """
    Fonction qui dessine un carré de taille, couleur et orientation déterminées.
    
    Paramètres :
    - taille : longueur de chaque côté du carré
    - couleur : couleur du tracé (ex. 'red', 'blue')
    - angle : orientation du carré (ex. 90 pour un carré classique)
    """
    color(couleur)  # Définit la couleur du tracé
    c = 0  # Initialise un compteur pour compter les côtés
    while c < 4:  # Répète 4 fois (un carré a 4 côtés)
        forward(taille)  # Avance de 'taille' unités
        left(angle)  # Tourne de l’angle indiqué
        c = c + 1  # Incrémente le compteur pour passer au côté suivant

def triangle(taille, couleur, angle):
    """
    Fonction qui dessine un triangle équilatéral de taille, couleur et orientation données.
    
    Paramètres :
    - taille : longueur de chaque côté du triangle
    - couleur : couleur du tracé
    - angle : orientation du triangle (ex. 120 pour un triangle équilatéral)
    """
    color(couleur)  # Définit la couleur du tracé
    c = 0  # Initialise le compteur pour les 3 côtés
    while c < 3:  # Répète 3 fois (un triangle a 3 côtés)
        forward(taille)  # Avance de 'taille' unités
        left(angle)  # Tourne de l’angle indiqué (souvent 120° pour un triangle équilatéral)
        c = c + 1  # Incrémente le compteur

def etoile6(taille, couleur, angle):
    """
    Dessine une étoile à 6 branches en utilisant deux triangles équilatéraux imbriqués.
    
    Paramètres :
    - taille : longueur de chaque côté des triangles
    - couleur : couleur de l'étoile
    - angle : angle pour le dessin des triangles
    """
    color(couleur)  # Définit la couleur de l'étoile
    pos_initiale = position()  # Enregistre la position actuelle de la tortue
    h_initiale = heading()  # Enregistre l'orientation actuelle de la tortue
    c = 0  # Compteur pour le nombre de triangles dessinés
  
    while c < 1:  # Cette boucle ne s'exécute qu'une seule fois
        triangle(taille, couleur, angle)  # Dessine le premier triangle
        up()  # Relève le stylo pour ne pas dessiner pendant les déplacements
        left(90)  # Tourne la tortue à gauche de 90 degrés
        forward(taille / 1.7)  # Avance vers l'avant d'une fraction de la taille
        left(90)  # Tourne la tortue à gauche de 90 degrés à nouveau
        backward(taille)  # Recule de 'taille' unités pour repositionner la tortue
        down()  # Redescend le stylo pour commencer à dessiner à nouveau
        triangle(taille, couleur, angle)  # Dessine le second triangle
        up()  # Relève le stylo après avoir dessiné le second triangle
        c = c + 1  # Incrémente le compteur (a peu d'impact car la boucle s'exécute qu'une fois)
    
    goto(pos_initiale)  # Retourne à la position de départ de l'étoile
    setheading(h_initiale)  # Rétablit l'orientation initiale de la tortue

def etoile5(taille, couleur, angle):
    """
    Dessine une étoile en utilisant les paramètres fournis.
    
    Paramètres :
    - taille : longueur de chaque côté des dessins
    - couleur : couleur de l'étoile
    - angle : angle de rotation après chaque côté
    """
    color(couleur)  # Définit la couleur de l'étoile
    c = 0  # Compteur pour le nombre de fois que l'étoile est dessinée
    
    while c < 5:  # Répète le dessin 5 fois
         forward(taille)  # Avance de 'taille' unités
         left(angle)  # Tourne de l'angle spécifié
         c = c + 1  # Incrémente le compteur
