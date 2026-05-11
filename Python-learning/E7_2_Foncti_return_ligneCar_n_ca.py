def ligneCar(n, ca):
    # On définit une fonction appelée ligneCar avec deux paramètres :
    # n = le nombre de répétitions
    # ca = le caractère (ou la chaîne) à répéter

    var_vide = ""  # On crée une chaîne vide qui servira à stocker le résultat final

    for i in range(n):  # On répète l’action n fois
        var_vide += ca  # À chaque tour, on ajoute la chaîne 'ca' à la fin de var_vide

    return var_vide  # À la fin de la boucle, on renvoie la chaîne complète construite

# Exemple d’utilisation de la fonction :
ca = "ca"  # On définit la chaîne à répéter
print(ligneCar(4, ca))  # On appelle la fonction avec n = 4 et on affiche le résultat
# Résultat attendu : "cacaca"
