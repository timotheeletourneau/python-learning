a, c = 3, 1        # Initialisation :
                   # a = 3 (valeur de départ)
                   # c = 1 (compteur pour contrôler la boucle)

while c < 13:      # Tant que c est plus petit que 13, on continue la boucle
    print(a, end=" ")  
                   # Affiche la valeur actuelle de a, suivi d’un espace (sans retour à la ligne)

    a, c = a*3, c+1  
                   # Mise à jour :
                   # - a devient a*3 (donc multiplié par 3 à chaque tour)
                   # - c augmente de 1 (sert de compteur pour arrêter la boucle après 12 tours)
