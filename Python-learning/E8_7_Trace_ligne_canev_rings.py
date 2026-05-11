# Petit exercice utilisant la bibliothèque graphique tkinter

from tkinter import *  # Importe toutes les classes et fonctions de tkinter pour créer des interfaces graphiques

# --- Définition des fonctions pour dessiner les anneaux ---

def draw_all_oval():
    """Dessine les 5 anneaux olympiques sur le canevas"""
    draw_oval_blue()
    draw_oval_black()
    draw_oval_red()
    draw_oval_yellow()
    draw_oval_green()
    

def draw_oval_blue():
    """Dessine l'anneau bleu"""
    global x1, y1, x2, y2
    can1.create_oval(x1, y1, x2, y2, width=6.2, outline='blue')

def draw_oval_black():
    """Dessine l'anneau noir"""
    global x3, y3, x4, y4
    can1.create_oval(x3, y3, x4, y4, width=6.2, outline='black')

def draw_oval_red():
    """Dessine l'anneau rouge"""
    global x5, y5, x6, y6
    can1.create_oval(x5, y5, x6, y6, width=6.2, outline='red')

def draw_oval_yellow():
    """Dessine l'anneau jaune"""
    global x7, y7, x8, y8
    can1.create_oval(x7, y7, x8, y8, width=6.2, outline='yellow')

def draw_oval_green():
    """Dessine l'anneau vert"""
    global x9, y9, x10, y10
    can1.create_oval(x9, y9, x10, y10, width=6.2, outline='green')


# --- Coordonnées pour chaque anneau ---
x1, y1, x2, y2 = 35, 40, 110, 115   # Anneau bleu
x3, y3, x4, y4 = 125, 40, 200, 115  # Anneau noir
x5, y5, x6, y6 = 215, 40, 290, 115  # Anneau rouge
x7, y7, x8, y8 = 80, 75, 155, 150   # Anneau jaune
x9, y9, x10, y10 = 170, 75, 245, 150 # Anneau vert


# --- Création de la fenêtre principale ---
fen1 = Tk()
fen1.title("Anneaux Olympiques")

# --- Création du canevas pour dessiner ---
can1 = Canvas(fen1, bg='white', height=180, width=320)
can1.pack(side=LEFT)

# --- Boutons pour dessiner les anneaux ---
Button(fen1, text='Quitter', command=fen1.quit).pack()
Button(fen1, text='Tracer anneau bleu', command=draw_oval_blue).pack()
Button(fen1, text='Tracer anneau noir', command=draw_oval_black).pack()
Button(fen1, text='Tracer anneau rouge', command=draw_oval_red).pack()
Button(fen1, text='Tracer anneau jaune', command=draw_oval_yellow).pack()
Button(fen1, text='Tracer anneau vert', command=draw_oval_green).pack()
Button(fen1, text='Tracer tous les anneaux', command=draw_all_oval).pack()


# --- Boucle principale pour gérer les événements ---
fen1.mainloop()
fen1.destroy()
