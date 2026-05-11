# Petit exercice utilisant la bibliothèque graphique tkinter

from tkinter import *  # Importe toutes les classes et fonctions de tkinter pour créer des interfaces graphiques
from random import randrange  # Importe la fonction randrange pour générer des nombres aléatoires

# --- définition des fonctions gestionnaires d'événements : --
def draw_rectangle():
    "Dessine un rectangle dans le canevas can1"
    global x1, y1, x2, y2, coul  # Indique que nous allons utiliser les variables globales définies plus bas
    can1.create_rectangle(x1, y1, x2, y2, width=1, fill=coul)  # Trace un rectangle avec les coordonnées spécifiées

    # Mise à jour des coordonnées pour la ligne suivante (déplacement de 2 pixels)
    y2, y1, x2, x1 = y2 + 2, y1 + 2, x2 + 2, x1 + 2  # Déplace les coins du rectangle pour le prochain tracé

def draw_arc():
    "Dessine un arc dans le canevas can1"
    global x3, y3, x4, y4, coul1  # Indique que nous allons utiliser les variables globales
    can1.create_arc(x3, y3, x4, y4, width=1, fill=coul1)  # Trace un arc dans le rectangle défini par les coordonnées

    # Mise à jour des coordonnées pour l'arc (déplacement similaire)
    y4, y3, x4, x3 = y4 + 2, y3 + 2, x4 + 2, x3 + 2  # Déplace les coins de l'arc pour le prochain tracé

def draw_oval():
    "Dessine un ovale dans le canevas can1"
    global x5, y5, x6, y6, coul2  # Indique que nous allons utiliser les coordonnées globales
    can1.create_oval(x5, y5, x6, y6, width=1, fill=coul2)  # Trace un ovale dans le rectangle déterminé par les coordonnées

    # Mise à jour des coordonnées pour l'oval
    y6, y5, x6, x5 = y6 + 2, y5 + 2, x6 + 2, x5 + 2  # Déplace les coins de l'oval pour le prochain tracé

def draw_polygon():
    "Dessine un polygone dans le canevas can1"
    global x7, y7, x8, y8, x9, y9, coul3  # Indique que nous allons utiliser les coordonnées globales
    can1.create_polygon(x7, y7, x8, y8, x9, y9, width=1, fill=coul3, outline='black')  # Trace un polygone

    # Mise à jour des coordonnées pour le polygone
    y9, y8, y7, x9, x8, x7 = y9 + 2, y8 + 2, y7 + 2, x9 + 2, x8 + 2, x7 + 2  # Déplace les sommets du polygone pour le prochain tracé

def changecolor():
    "Change aléatoirement la couleur du tracé"
    global coul, coul1, coul2, coul3  # Indique que nous allons utiliser plusieurs variables globales
    pal = ['purple', 'cyan', 'maroon', 'green', 'red', 'blue', 'orange', 'yellow']  # Liste de couleurs possibles
    c = randrange(8)  # Génère un nombre aléatoire entre 0 et 7
    coul, coul1, coul2, coul3 = pal[c], pal[c], pal[c], pal[c]   # Met à jour toutes les couleurs sur la même ligne


# Coordonnées pour tracer un rectangle
x1, y1, x2, y2 = 120, 10, 150, 70  # Rectangle défini par les points (x1, y1) en haut à gauche et (x2, y2) en bas à droite
coul = 'dark green'  # Couleur du rectangle

# Coordonnées pour tracer un arc
x3, y3, x4, y4 = -80, 5, 100, 100  # Rectangle dans lequel l'arc sera dessiné
coul1 = 'dark green'  # Couleur de l'arc

# Coordonnées pour tracer un ovale
x5, y5, x6, y6 = 5, 85, 100, 185  # Rectangle dans lequel l'ovale sera dessiné
coul2 = 'dark green'  # Couleur de l'ovale

# Coordonnées pour tracer un polygone
x7, y7, x8, y8, x9, y9 = 120, 150, 150, 100, 150, 150  # Coordonnées des sommets du polygone (triangle, par exemple)
coul3 = 'dark green'  # Couleur du polygone

# Création du widget principal ("maître") :
fen1 = Tk()  # Crée une fenêtre principale

# Création des widgets "esclaves" :
can1 = Canvas(fen1, bg='dark grey', height=200, width=200)  # Crée un canevas de 200x200 pixels avec un fond gris
can1.pack(side=LEFT)  # Place le canevas à gauche dans la fenêtre

# Boutons pour dessiner les formes
Button(fen1, text='Quitter', command=fen1.quit).pack(side=BOTTOM)  # Bouton pour quitter
Button(fen1, text='Tracer un rectangle', command=draw_rectangle).pack()  # Bouton pour tracer un rectangle
Button(fen1, text='Tracer un arc', command=draw_arc).pack()  # Bouton pour tracer un arc
Button(fen1, text='Tracer un ovale', command=draw_oval).pack()  # Bouton pour tracer un ovale
Button(fen1, text='Tracer un polygone', command=draw_polygon).pack()  # Bouton pour tracer un polygone
Button(fen1, text='Autre couleur', command=changecolor).pack()  # Bouton pour changer la couleur

fen1.mainloop()  # Démarre la boucle principale pour gérer les événements
fen1.destroy()  # Ferme la fenêtre lorsque la boucle est arrêtée
