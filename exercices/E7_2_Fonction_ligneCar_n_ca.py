def ligneCar(n, ca):
    "cette fonction renvoie \
    une chaîne de <n> caractères \
    <ca>"

    var_v = ""  # variable vide qui va contenir la chaîne construite
    
    for i in range(n):  # boucle qui tourne n fois
        var_v = var_v + ca  # à chaque tour, ajoute ca à var_v
    
    return var_v  # renvoie la chaîne complète

ca = "ca"  # on définit ce que l'on veut répéter
print(ligneCar(4, ca))  # on appelle la fonction et on affiche le résultat

        
    




    



