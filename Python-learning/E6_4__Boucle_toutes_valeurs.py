# On crée une liste vide pour stocker les valeurs
l1 = []

# Boucle infinie (elle ne s'arrête que si on fait "break")
while True:
    # On demande une saisie à l'utilisateur
    saisie = input("Veuillez entrer une valeur : ")

    # Si l'utilisateur appuie juste sur Entrée (saisie vide), on arrête la boucle
    if saisie == "":
        break

    # Sinon : on convertit la saisie en nombre flottant
    valeur = float(saisie)

    # On ajoute ce nombre dans la liste
    l1.append(valeur)

# Quand la boucle est terminée, on affiche la liste complète
print(l1)
