def changeCar(ch, ca1, ca2, debut=0, fin=None):
    # Si 'fin' n'est pas spécifié, on prend la longueur de la chaîne
    if fin is None:
        fin = len(ch)

    # Construire la nouvelle chaîne :
    # - ch[:debut] : impliquer tous les caractères avant l'indice 'debut'
    # - ch[debut:fin+1] : cela inclut le segment de 'debut' à 'fin' et remplace 'ca1' (espace) par 'ca2' (astérisque)
    # - ch[fin:] : tous les caractères après l'indice 'fin'
    return ch[:debut] + ch[debut:fin+1].replace(ca1, ca2) + ch[fin:]

# Chaîne de test
phrase = 'Ceci est une toute petite phrase.'

# Remplace tous les espaces par des astérisques dans toute la chaîne
print(changeCar(phrase, ' ', '*'))                     # Attendu : 'Ceci*est*une*toute*petite*phrase.'

# Remplace les espaces uniquement entre les indices 8 et 12
print(changeCar(phrase, ' ', '*', 8, 12))              # Attendu : 'Ceci est*une*toute petite phrase.'

# Remplace les espaces à partir de l'indice 12 jusqu'à la fin
print(changeCar(phrase, ' ', '*', 12))                 # Attendu : 'Ceci est une*toute*petite*phrase.'

# Remplace tous les espaces de la chaîne jusqu'à l'indice 12
print(changeCar(phrase, ' ', '*', fin=12))             # Attendu : 'Ceci*est*une*toute petite phrase.'
