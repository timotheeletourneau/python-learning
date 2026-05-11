# Déclaration d'une liste de prénoms
l1 = ['Jean-Michel', 'Marc', 'Vanessa', 'Anne', 'Maximilien',
      'Alexandre-Benoît', 'Louise']

# Boucle for qui parcourt chaque élément (chaque prénom) de la liste l1
for nom in l1:
    # Affiche le prénom suivi de sa longueur (nombre de caractères)
    # f"" permet d’insérer des variables directement dans la chaîne de caractères
    # len(nom) calcule le nombre de caractères dans le prénom
    print(f"{nom} : {len(nom)} caractères")
