from math import *  # Importer toutes les fonctions de la bibliothèque mathématique

# Demander à l'utilisateur de saisir les longueurs des côtés du triangle
a = input("Saisir une première longueur d'un triangle quelconque : ")
b = input("Saisir une seconde longueur d'un triangle quelconque : ")
c = input("Saisir une troisième longueur d'un triangle quelconque : ")

# Convertir les entrées de texte en flottants pour faire des calculs
side_a = float(a)
side_b = float(b)
side_c = float(c)

# Calculer le périmètre du triangle en additionnant les longueurs des côtés
peri = side_a + side_b + side_c

# Afficher le périmètre calculé avec une unité
print("Le périmètre du triangle est de", peri, "cm.")

# Calculer le semi-périmètre (demi-perp) en divisant le périmètre par 2
d_p = peri / 2

# Calculer l'aire avant de prendre la racine carrée, selon la formule de Heron
avant_racine = d_p * (d_p - side_a) * (d_p - side_b) * (d_p - side_c)

# Calculer l'aire en utilisant la fonction racine carrée
aire = sqrt(avant_racine)

# Afficher l'aire du triangle, arrondie à 2 décimales
print(f"L'aire du triangle est de {aire:.2f} cm²")



