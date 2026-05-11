# Petit exercice utilisant la bibliothèque graphique tkinter

from tkinter import *  # Importe tous les éléments de la bibliothèque tkinter pour créer des interfaces graphiques
from random import randrange  # Importe la fonction randrange pour générer des nombres aléatoires

# --- définition des fonctions gestionnaires d'événements : --
def drawline():
    "Tracé d'une ligne dans le canevas can1"
    global x1, y1, x2, y2, coul  # Indique que nous allons utiliser les variables globales définies plus bas
    can1.create_line(x1, y1, x2, y2, width=2, fill=coul)  # Trace une ligne de (x1, y1) à (x2, y2) avec la couleur spécifiée

    # modification des coordonnées pour la ligne suivante :
    y2, y1 = y2 + 10, y1 - 10  # Met à jour y1 et y2 pour la prochaine ligne tracée

def changecolor():
    "Changement aléatoire de la couleur du tracé"
    global coul  # Indiquer que nous utilisons la variable global 'coul' pour la couleur
    pal = ['purple', 'cyan', 'maroon', 'green', 'red', 'blue', 'orange', 'yellow']  # Liste des couleurs possibles
    c = randrange(8)  # génère un nombre aléatoire entre 0 et 7 pour choisir une couleur
    coul = pal[c]  # Met à jour 'coul' avec une couleur aléatoire de la liste

def drawline2():
    global x3, y3, x4, y4, x5, y5, x6, y6, coul1  # Indique que nous allons utiliser des variables globales
    # Trace la première ligne de la croix (verticale)
    can1.create_line(x3, y3, x4, y4, width=1.5, fill=coul1)  
    # Trace la deuxième ligne de la croix (horizontale)
    can1.create_line(x5, y5, x6, y6, width=1.5, fill=coul1)  

    # Mise à jour de y pour les lignes (ceci semble redondant dans ce contexte)
    y4, y3 = y4 + 0, y3 + 0  # Ne change pas les valeurs
    y6, y5 = y6 + 0, y5 + 0  # Ne change pas les valeurs
    
    
# ------ Programme principal --------
    
# les variables suivantes seront utilisées de manière globale :
x1, y1, x2, y2 = 10, 190, 190, 10  # Coordonnées de la première ligne tracée par 'drawline'
coul = 'dark green'  # Couleur de la première ligne

# Coordonnées pour tracer une croix (deux lignes rouges)
x3, y3, x4, y4 = 0, 100, 200, 100  # Ligne horizontale de la croix
x5, y5, x6, y6 = 100, 0, 100, 200  # Ligne verticale de la croix
coul1 = 'red'  # Couleur des lignes de la croix

# Création du widget principal ("maître") :
fen1 = Tk()  # Crée une nouvelle fenêtre Tkinter

# Création des widgets "esclaves" :
can1 = Canvas(fen1, bg='dark grey', height=200, width=200)  # Crée un canevas pour le dessin
can1.pack(side=LEFT)  # Place le canevas à gauche dans la fenêtre

# Boutons fonctionnels
bou1 = Button(fen1, text='Quitter', command=fen1.quit)  # Crée un bouton pour quitter l'application
bou1.pack(side=BOTTOM)  # Place le bouton en bas de la fenêtre
bou2 = Button(fen1, text='Tracer une ligne', command=drawline)  # Crée un bouton pour tracer une ligne
bou2.pack()  # Place le bouton dans la fenêtre
bou3 = Button(fen1, text='Autre couleur', command=changecolor)  # Crée un bouton pour changer la couleur
bou3.pack()  # Place le bouton dans la fenêtre
bou4 = Button(fen1, text='Viseur', command=drawline2)  # Crée un bouton pour tracer une croix
bou4.pack()  # Place le bouton dans la fenêtre

fen1.mainloop()  # Démarre la boucle principale pour gérer les événements
fen1.destroy()  # Ferme la fenêtre lorsque la boucle est arrêtée
