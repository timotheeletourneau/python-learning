t1 = ['Jean', 'Maximilien', 'Brigitte', 'Sonia', 'Jean-Pierre', 'Sandra']  
# Liste initiale de mots à analyser

t2 = []  
# Liste vide qui va contenir les mots avec moins de 6 caractères

t3 = []  
# Liste vide qui va contenir les mots avec 6 caractères ou plus

for nom in t1:  
    # On parcourt chaque mot de la liste t1
    # 'nom' est une variable temporaire qui prend successivement la valeur de chaque élément

    if len(nom) < 6:  
        # Si le mot a moins de 6 caractères
        t2.append(nom)  
        # On ajoute le mot à la liste des mots courts (t2)
    else:  
        # Sinon (le mot a 6 caractères ou plus)
        t3.append(nom)  
        # On ajoute le mot à la liste des mots longs (t3)

print(t2)  
# Affiche la liste des mots avec moins de 6 caractères

print(t3)  
# Affiche la liste des mots avec 6 caractères ou plus
