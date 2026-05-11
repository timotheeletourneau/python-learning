import math  # Importation de la librairie math pour accéder à pi et à d'autres fonctions mathématiques

# Fonction pour convertir les radians en degrés
def convertir_angles(radians):
    angle_en_degres = radians * (180/math.pi)  # Conversion des radians en degrés
    return angle_en_degres  # Retourne l'angle en degrés

# Conversion des radians donnés en degrés
angle_en_degres = convertir_angles(1.2620766709379663)

# Fonction pour convertir les degrés décimaux en degrés, minutes et secondes
def convertir_decim(angle_en_degres):
    degres = int(angle_en_degres)  # Partie entière de l'angle en degrés
    minutes = int((angle_en_degres - degres) * 60)  # Calcul des minutes (partie entière de la décimale * 60)
    secondes = int(((angle_en_degres - degres) * 60 - minutes) * 60)  # Calcul des secondes (partie entière de la décimale des minutes * 60)
    return degres, minutes, secondes  # Retourne les valeurs des degrés, minutes et secondes

# Appel de la fonction pour obtenir les valeurs des degrés, minutes et secondes
degres, minutes, secondes = convertir_decim(angle_en_degres)

# Affichage du résultat
print(f"{degres}°, {minutes}', {secondes}''")
