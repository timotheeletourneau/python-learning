from math import pi  # On importe la constante pi depuis le module math

def surfCercle(R):
    # On définit une fonction appelée surfCercle qui prend un paramètre R (le rayon)
    
    surface = pi * float(R) ** 2  
    # On calcule l'aire du cercle : pi * R^2
    # float(R) s'assure que le rayon est traité comme un nombre à virgule (au cas où R serait un entier)
    
    return surface  
    # On renvoie la valeur de l'aire calculée

print(surfCercle(2.5))  
# On appelle la fonction avec un rayon de 2.5 et on affiche le résultat
# Résultat attendu : environ 19.63495
