import math  # Importation de la librairie math pour accéder à pi et à d'autres fonctions mathématiques

def convertir_angles(degres, minutes, secondes):
    angle_en_degres = degres + minutes / 60 + secondes / 3600
    radians = angle_en_degres * (math.pi / 180)
    return radians  # Retourne la valeur des radians

# Appelle la fonction et récupère le résultat dans la variable "radians"
radians = convertir_angles(72, 18, 42)

# Affiche le résultat
print(f"{radians} rad")
