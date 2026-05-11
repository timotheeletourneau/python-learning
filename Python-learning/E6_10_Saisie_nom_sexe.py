# Demande à l'utilisateur de saisir son nom
info1 = input("Saisir votre nom : ")

# Demande à l'utilisateur de saisir son sexe en majuscule (M pour masculin, F pour féminin)
# La méthode .upper() convertit l'entrée en majuscule pour éviter les erreurs de casse
info2 = input("Saisir votre sexe en MAJ (M ou F) : ").upper()

# Conversion des informations en chaînes de caractères (ce n'est pas nécessaire ici car input() retourne déjà une chaîne)
donnees1 = str(info1)
donnees2 = str(info2)

# Vérification du sexe. Si l'utilisateur a saisi 'M' (pour masculin), on affiche le message correspondant
if 'M' in donnees2:
    print(f"Cher Monsieur {donnees1}", end=" ")  # Affiche "Cher Monsieur [nom]"
    
# Si l'utilisateur a saisi 'F' (pour féminin), on affiche le message correspondant
elif 'F' in donnees2:
    print(f"Chère Mademoiselle {donnees1}", end=" ")  # Affiche "Chère Mademoiselle [nom]"
    
# Si l'utilisateur entre quelque chose d'autre que 'M' ou 'F', un message d'erreur est affiché
else:
    print("Sexe invalide. Veuillez saisir M pour masculin ou F pour féminin.")
