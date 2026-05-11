# Initialisation des variables
case = 1  # On commence à la première case
grain = 1  # Le premier nombre de grains est 1

# Boucle qui s'exécute tant que la case est inférieure à 65
while case < 65:
    # Affichage du nombre de grains sur chaque case
    print(f"Case:{case} -> {grain} grains")
    
    # Incrémenter le numéro de la case
    case += 1
    
    # Double le nombre de grains à chaque case suivante (2^case)
    grain *= 2

