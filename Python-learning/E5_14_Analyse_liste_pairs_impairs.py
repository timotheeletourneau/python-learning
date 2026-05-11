t1 = [32, 5, 12, 8, 3, 75, 2, 15]  
# Liste initiale contenant des nombres à analyser

t2 = []  
# Liste vide qui va accueillir les nombres pairs

t3 = []  
# Liste vide qui va accueillir les nombres impairs

for liste in t1:  
    # On parcourt chaque élément de la liste t1
    # 'liste' est une variable temporaire qui prend successivement la valeur de chaque élément

    if (liste) % 2 == 0:  
        # Si le nombre est divisible par 2 (c'est-à-dire pair)
        t2.append(liste)  
        # On ajoute le nombre à la liste des pairs
    else:  
        # Sinon (le nombre est impair)
        t3.append(liste)  
        # On ajoute le nombre à la liste des impairs

print(t2)  
# Affiche la liste contenant tous les nombres pairs

print(t3)  
# Affiche la liste contenant tous les nombres impairs
