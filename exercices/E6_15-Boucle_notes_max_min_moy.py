# On crée une liste vide pour stocker toutes les notes
l1 = []

# On initialise les variables pour la plus grande et la plus petite note
# Au début, on ne connaît pas encore de note, donc on met None
grand = None
petit = None

while True:
    # On demande à l’utilisateur de saisir une note
    saisie = input("Veuillez entrer une note (négative pour arrêter) : ")
    valeur = float(saisie)
    
    # Si la valeur est négative, on arrête la boucle
    if valeur < 0:
        break
    
    # On ajoute la note saisie dans la liste
    l1.append(valeur)
    
    # Si c’est la première note (grand et petit valent encore None)
    # On initialise grand et petit avec cette valeur
    if grand is None and petit is None:
        grand = valeur
        petit = valeur
    else:
        # Sinon, on met à jour grand si la nouvelle note est plus grande
        if valeur > grand:
            grand = valeur
        # Et on met à jour petit si la nouvelle note est plus petite
        if valeur < petit:
            petit = valeur
    
    # On calcule la moyenne en divisant la somme des notes par leur nombre
    moyenne = sum(l1) / len(l1)
    
    # On affiche toutes les infos demandées
    print(f"Nombre de notes : {len(l1)} | Max : {grand} | Min : {petit} | Moyenne : {moyenne:.2f}")
