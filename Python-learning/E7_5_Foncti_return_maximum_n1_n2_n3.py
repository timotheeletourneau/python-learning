def maximum(n1, n2, n3):
    # On définit une fonction appelée maximum qui prend trois nombres en paramètres
    # L'objectif est de renvoyer le plus grand des trois nombres

    n1 = int(n1)  # On convertit n1 en float pour s'assurer que les comparaisons fonctionnent
    n2 = int(n2)  # Même chose pour n2
    n3 = int(n3)  # Même chose pour n3

    val_max = n1  # On suppose d'abord que n1 est le maximum

    if n2 > val_max:  # Si n2 est plus grand que val_max, alors n2 devient le maximum
        val_max = n2
    if n3 > val_max:  # Si n3 est plus grand que val_max, alors n3 devient le maximum
        val_max = n3

    return val_max  # On renvoie le maximum trouvé

# Exemple d'utilisation
# On convertit le résultat en int pour obtenir un entier, comme demandé dans l'exemple
print(maximum(2, 5, 4))  # Résultat affiché : 5
