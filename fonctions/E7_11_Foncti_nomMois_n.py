def nomMois(n):
    # Liste contenant les mois de l'année
    l1 = ["Janvier", "Février", "Mars", "Avril", "Mai", "Juin", "Juillet",
          "Août", "Septembre", "Octobre", "Novembre", "Décembre"]
    
    # Vérifie si n est hors des limites valides (1 à 12)
    if n > 12 or n < 1:
        return "Mois invalide"  # Retourne un message d'erreur si n n'est pas valide

    # Ajuste n pour correspondre à l'index de la liste (par exemple, n=4 devient index 3)
    index_mois = n - 1
        
    # Récupère le mois correspondant à l'index ajusté
    mois = l1[index_mois]
    
    # Retourne le nom du mois
    return mois
