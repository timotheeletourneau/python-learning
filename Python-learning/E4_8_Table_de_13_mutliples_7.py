a, b, c = 13, 13, 1       # Initialisation : a=13, b=13 (premier terme), c=1 (compteur)

while c<51:             # Afficher les 50 premiers termes
    if(b%7 == 0):       # Vérifie si b est un multiple de 7
        print(f"{b}", end=" ") # si multiple de 7 → afficher
    else:
        pass      # sinon rien
    a, b, c = a, a*c, c+1
    
    

    




