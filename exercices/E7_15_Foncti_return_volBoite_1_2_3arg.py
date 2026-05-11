def volBoite(x1=None, x2=None, x3=None):
    """
    Calcule le volume d'une « boîte » selon le nombre d'arguments fournis.
    
    Cas gérés :
      – 0 argument  ➔ retourne –1 (indique une erreur)
      – 1 argument  ➔ cube                    : a³
      – 2 arguments ➔ prisme à base carrée    : a² × h
      – 3 arguments ➔ parallélépipède (boîte) : a × b × c
    
    Le résultat (sauf l’erreur –1) est arrondi à 3 décimales.
    """
    
    # 0 argument : x1 n’a pas été fourni → erreur
    if x1 is None:
        return -1
    
    # 1 seul argument : x1 est fourni, x2 et x3 sont None
    # On a affaire à un cube de côté x1, volume = x1³
    elif x2 is None:
        return round(x1 ** 3, 3)
    
    # 2 arguments : x1 et x2 donnés, x3 est None
    # Prisme droit à base carrée : base a² et hauteur h
    elif x3 is None:
        return round(x1 ** 2 * x2, 3)
    
    # 3 arguments : x1, x2, x3 tous fournis
    # Parallélépipède : volume = a × b × c
    else:
        return round(x1 * x2 * x3, 3)


# Appels de test demandés dans l’énoncé :
print(volBoite())             # -> -1
print(volBoite(5.2))          # -> 140.608
print(volBoite(5.2, 3))       # -> 81.12
print(volBoite(5.2, 3, 7.4))  # -> 115.44
