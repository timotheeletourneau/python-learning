def compteMots(ph):
    nombre_mots = 0        # Compteur pour le nombre de mots
    dans_mot = False        # Indique si on est actuellement dans un mot

    for char in ph:         # On parcourt chaque caractère de la phrase
        if char == " ":     # Si le caractère est un espace
            dans_mot = False  # On sort du mot (on n'est plus dans un mot)

        if char != " ":     # Si le caractère n'est pas un espace
            if not dans_mot:    # Si on n'était pas déjà dans un mot
                dans_mot = True   # On entre dans un mot
                nombre_mots += 1  # On compte un nouveau mot

    return nombre_mots     # Retourne le nombre total de mots
