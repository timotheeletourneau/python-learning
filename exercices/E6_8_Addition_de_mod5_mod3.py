# Définir les bornes
a, b = 0, 32  

# Initialiser la somme des multiples
somme = 0  

# Variable pour savoir si c’est le premier nombre affiché
first = True  

# Parcourir tous les nombres entre a et b inclus
for i in range(a, b + 1):  
    # Vérifier si le nombre est multiple de 15 (donc de 3 et de 5 en même temps)
    if i % 15 == 0:  
        # Si ce n’est pas le premier multiple trouvé, on affiche un +
        if not first:  
            print("+", end=" ")  
        # Afficher le multiple
        print(i, end=" ")  
        # Ajouter ce multiple à la somme
        somme += i  
        # Après avoir trouvé le premier nombre, indiquer que ce n’est plus le premier
        first = False  

# Afficher le résultat final
print("=", somme)  
