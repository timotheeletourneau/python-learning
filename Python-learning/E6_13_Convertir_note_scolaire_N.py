# On demande à l'utilisateur de saisir une note sur 85
note = input("Veuillez saisir votre note sur 85 : ")

# On convertit la saisie en nombre flottant
valeur = float(note)

# Fonction pour vérifier que la note est bien entre 0 et 85 (valide)
def verification(valeur):
    if valeur <= 85 and valeur >= 0:
        return True
    else:
        return False

# Fonction pour convertir la note sur 85 en note normalisée sur 100
def calcul_note_100(valeur):
    # On vérifie d'abord que la note est valide
    if not verification(valeur):
        print("Saisir correctement la note sur /85")  # Message d'erreur si invalide
        return
    # Calcul : on ramène la note sur 100 via une règle de trois
    note_st = (valeur / 85) * 100
    return note_st

# On calcule la note normalisée sur 100
note_st = calcul_note_100(valeur)

# Fonction pour afficher la note standardisée selon les seuils donnés
def note_standardisee(note_st):
    # Si la note est supérieure ou égale à 80%
    if note_st >= 80:
        print("A")
    # Entre 60% et moins de 80%
    elif 60 <= note_st < 80:
        print("B")
    # Entre 50% et moins de 60%
    elif 50 <= note_st < 60:
        print("C")
    # Entre 40% et moins de 50%
    elif 40 <= note_st < 50:
        print("D")
    # Moins de 40%
    else:
        print("E")

# On appelle la fonction pour afficher la note standardisée
note_standardisee(note_st)
