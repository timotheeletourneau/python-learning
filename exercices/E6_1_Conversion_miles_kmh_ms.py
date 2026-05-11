# Demander à l'utilisateur d'entrer une vitesse en miles/heure
a = input("Entrez une donnée numérique en miles/heure : ")

# Convertir l'entrée de texte de l'utilisateur en flottant pour effectuer des calculs
km_per_hour = float(a)

# Calculer la conversion de miles/heure en km/h et afficher le résultat
# (1 mile = 1.609 km)
print("La vitesse est de", km_per_hour * 1.609, "km/h.")

# Calculer la conversion de miles/heure en mètres/seconde et afficher le résultat
# (1 mile = 1609 mètres, 1 heure = 3600 secondes)
print("La vitesse est de", km_per_hour * (1609 / 3600), "m/s.")
