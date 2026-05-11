import math  # On importe le module 'math' pour pouvoir utiliser math.sqrt (racine carrée)

# On demande à l'utilisateur de saisir un nombre
nombre = input("Veuillez saisir un nombre : ")

# On convertit l'entrée (une chaîne de caractères) en nombre décimal (float)
valeur = float(nombre)

# Fonction qui vérifie si la valeur est positive ou nulle (définie pour la racine carrée réelle)
def valeur_pos_nul(valeur):
    if valeur >= 0:
        return True    # Si la valeur est positive ou nulle, on retourne True
    else:
        return False   # Sinon (valeur négative), on retourne False

# Fonction qui calcule et affiche la racine carrée si la valeur est valide
def calcul_racine(valeur):
    if not valeur_pos_nul(valeur):  # Si la valeur n'est pas positive, on affiche un message
        print("La racine carrée de ce nombre ne peut être calculée")
        return  # On sort de la fonction sans faire de calcul
    racine = math.sqrt(valeur)  # Sinon, on calcule la racine carrée avec math.sqrt()
    print(f"La racine carrée de {valeur} est {racine}")  # On affiche le résultat

# Appel de la fonction principale pour lancer le calcul
calcul_racine(valeur)
