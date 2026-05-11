from math import pi, sqrt   # On importe pi (π) et la racine carrée depuis le module math

l = float(input("Saisir la longueur du pendule : "))  # On demande à l’utilisateur la longueur en mètres et on convertit en nombre décimal

g = 9.81  # Constante de l’accélération gravitationnelle en m/s² (valeur moyenne sur Terre)

# Vérifie si la longueur est bien positive
if l > 0:
    # Formule de la période du pendule simple : T = 2π * √(l / g)
    T = 2 * pi * sqrt(l / g)
    # Affiche le résultat arrondi à 2 décimales
    print(f"La période d’un pendule simple de longueur {l} m est de {T:.2f} secondes.")
else:
    # Message d’erreur si la longueur est négative ou nulle
    print("Erreur : la longueur doit être positive")
