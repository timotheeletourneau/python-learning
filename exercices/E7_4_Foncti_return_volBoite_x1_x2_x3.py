def volBoite(x1, x2, x3):
    # On définit une fonction appelée volBoite avec trois paramètres :
    # x1, x2, x3 représentent les dimensions de la boîte (longueur, largeur, hauteur)

    volume = float(x1) * float(x2) * float(x3)
    # On calcule le volume en multipliant les trois dimensions
    # float() s'assure que les valeurs sont traitées comme des nombres à virgule (au cas où ce serait des entiers ou des chaînes de caractères)

    return volume  
    # On renvoie le volume calculé

# On appelle la fonction avec les valeurs 5.2, 7.7 et 3.3
# et on arrondit le résultat à 3 décimales pour correspondre à l'exemple donné
print(round(volBoite(5.2, 7.7, 3.3), 3))
# Résultat affiché : 132.132
# Ici, le '3' dans round(..., 3) signifie qu'on veut garder 3 chiffres après la virgule
