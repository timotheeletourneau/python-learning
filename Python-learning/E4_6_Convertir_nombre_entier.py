def convertir_secondes(secondes):
    # 1 an = 365 jours * 24 heures * 60 minutes * 60 secondes
    # Cela donne 31 536 000 secondes dans une année
    annees = secondes // 31536000  # Calcul du nombre d'années
    secondes = secondes % 31536000  # Reste des secondes après avoir extrait les années

    # 1 mois = 30 jours en moyenne * 24 heures * 60 minutes * 60 secondes
    # Cela donne environ 2 592 000 secondes dans un mois
    mois = secondes // 2592000  # Calcul du nombre de mois
    secondes = secondes % 2592000  # Reste des secondes après avoir extrait les mois

    # 1 jour = 24 heures * 60 minutes * 60 secondes
    # Cela donne 86 400 secondes dans un jour
    jours = secondes // 86400  # Calcul du nombre de jours
    secondes = secondes % 86400  # Reste des secondes après avoir extrait les jours

    # 1 heure = 60 minutes * 60 secondes
    # Cela donne 3600 secondes dans une heure
    heures = secondes // 3600  # Calcul du nombre d'heures
    secondes = secondes % 3600  # Reste des secondes après avoir extrait les heures

    # 1 minute = 60 secondes
    minutes = secondes // 60  # Calcul du nombre de minutes
    secondes = secondes % 60  # Reste des secondes après avoir extrait les minutes

    # Les secondes restantes
    print(f"{annees} années, {mois} mois, {jours} jours, {heures} heures, {minutes} minutes et {secondes} secondes")

# Exemple d'utilisation
convertir_secondes(50000000000000)
