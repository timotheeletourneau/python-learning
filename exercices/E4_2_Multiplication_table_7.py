a, b, c = 7, 0, 1   # Initialisation : a=7, b=0, c=1

while c < 21:       # Tant que c est plus petit que 21, on continue la boucle
    print(b, end=" ")   # Affiche la valeur actuelle de b, suivi d’un espace (pas de retour à la ligne)

    a, b, c = a, a*c, c+1   
    # Mise à jour des variables à chaque tour :
    # - a reste identique (il reprend sa valeur précédente)
    # - b devient a*c (donc dépend des anciennes valeurs de a et c)
    # - c augmente de 1 (compteur qui arrête la boucle après 20 tours)
