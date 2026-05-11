def eleMax(liste, debut=0, fin=None):
    # Si aucun indice de fin n'est fourni, on prend la fin de la liste
    if fin is None:
        fin = len(liste)

    # On crée une sous-liste allant de 'debut' à 'fin' inclus
    # +1 nécessaire car le slice Python exclut la borne de fin
    sous_liste = liste[debut:fin + 1]
    
    # On retourne le maximum dans cette sous-liste
    return max(sous_liste)

# Exemple de liste
serie = [9, 3, 6, 1, 7, 5, 4, 8, 2]

# Maximum sur toute la liste
print(eleMax(serie))                 # 9

# Maximum entre les indices 2 et 5 inclus (6, 1, 7, 5)
print(eleMax(serie, 2, 5))           # 7

# Maximum entre l'indice 2 et la fin de la liste (6, 1, 7, 5, 4, 8, 2)
print(eleMax(serie, 2))              # 8

# Maximum entre les indices 1 et 3 inclus (3, 6, 1)
print(eleMax(serie, fin=3, debut=1)) # 6
