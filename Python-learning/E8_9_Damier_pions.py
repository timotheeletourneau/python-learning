from tkinter import *

# ---- fonctions qui dessinent un carré (bleu ou blanc) ----
def carre_b(x1, y1, x2, y2, ho, ver, coul ='black'):
    # dessine un carré bleu
    # x1, y1 : coin haut gauche
    # x2, y2 : coin bas droit
    # ho : décalage horizontal (colonne)
    # ver : décalage vertical (ligne)
    can.create_rectangle(x1+ho, y1+ver, x2+ho, y2+ver, outline=coul, width=0.1, fill='dark blue')

def carre_w(x1, y1, x2, y2, ho, ver, coul ='black'):
    # dessine un carré blanc
    can.create_rectangle(x1+ho, y1+ver, x2+ho, y2+ver, outline=coul, width=0.1, fill='white')


# ---- fonction qui dessine le damier ----
def figure_1():
    can.delete(ALL)      # efface le canevas avant de redessiner

    # on veut 10 lignes (0 à 9)
    for i in range(10):
        ho = 0          # on repart au début de la ligne (colonne 0)
        c = 0           # compteur de cases sur la ligne

        ver = i * 20    # décalage vertical : chaque ligne descend de 20 pixels

        # tant qu'on n'a pas atteint la largeur du canevas (200 px)
        while ho < 200:

            # alternance des couleurs :
            # si c et i sont de même parité -> carré bleu
            # sinon -> carré blanc
            if c % 2 == i % 2:
                carre_b(0, 0, 20, 20, ho, ver)  # carré bleu
            else:
                carre_w(0, 0, 20, 20, ho, ver)  # carré blanc

            ho += 20   # on passe à la case suivante (20 px)
            c += 1     # on incrémente le compteur de cases

        # fin de ligne : ver est déjà calculé en début de ligne
        # (ver = i * 20)
        # la boucle passe à la ligne suivante automatiquement


# ---- interface ----

fen = Tk()  # création de la fenêtre principale

# création du canevas où on dessine le damier
# width = largeur en pixels
# height = hauteur en pixels
# bg = couleur de fond
can = Canvas(fen, width=200, height=200, bg='white')
can.pack(side=TOP, padx=5, pady=5)  # positionne le canevas dans la fenêtre

# création du bouton "damier"
# text = texte affiché
# command = fonction appelée quand on clique dessus
b1 = Button(fen, text='damier', command=figure_1, width=8, height=1)
b1.pack(side=LEFT, padx=11, pady=11)  # positionne le bouton

fen.mainloop()  # lance la boucle principale Tkinter (affiche la fenêtre)
