a, b, c = 7, 7, 2       # Initialisation : a=7, b=7 (premier terme), c=1 (compteur)

while c<22:             # Afficher les 20 premiers termes
    if(b%3 == 0):       # Vérifie si b est un multiple de 3
        print(f"{b}*", end=" ") # si multiple de 3 → ajoute *
    else:
        print(b, end=" ")       # sinon juste b
    a, b, c = a, a*c, c+1
    
    

    




