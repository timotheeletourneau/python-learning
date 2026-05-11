def volBoite(x1=10, x2=10, x3=10):
    """Calcule et renvoie le volume d'une boîte."""
    return x1 * x2 * x3


# Appels de test
print(volBoite())          # 1000
print(volBoite(5.2))       # 520.0
print(volBoite(5.2, 3))    # 156.0
