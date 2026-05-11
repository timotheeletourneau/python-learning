def indexMax(liste):
    # Initialiser la valeur maximale avec le premier élément de la liste
    new_val_max = liste[0]
    
    # Initialiser l'index de la valeur maximale à 0
    new_index_val_max = 0

    # Parcourir chaque élément de la liste à l'aide de son index
    for i in range(len(liste)):
        # Comparer l'élément courant avec la valeur maximale actuelle
        if liste[i] > new_val_max:
            # Si l'élément courant est plus grand, mettre à jour la valeur maximale
            new_val_max = liste[i]
            # Mettre à jour l'index de la nouvelle valeur maximale
            new_index_val_max = i
    
    # Retourner l'index de la valeur maximale trouvée
    return new_index_val_max
