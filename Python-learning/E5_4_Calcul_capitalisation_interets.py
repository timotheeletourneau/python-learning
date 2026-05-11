# Taux d'intérêt annuel (4,3 %)
taux = 0.043

# Capital initial en euros (100 €)
capital = 100

# Initialisation de l'année à 1
annee = 1

# Boucle pour calculer les intérêts pendant 20 ans
while annee <= 20:  # Boucle qui s'arrête après 20 années
    capital = round(capital, 2)  # Arrondi à 2 chiffres après la virgule pour une présentation propre
    print(f"Année {annee} -> {capital} €")  # Affichage du capital à la fin de l'année
    capital = capital + (taux * capital)  # Calcul des intérêts et ajout au capital
    annee += 1  # Incrémentation de l'année pour passer à la suivante
