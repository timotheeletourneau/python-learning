a = 0 # Initialisation de a à 1

# Vérifie si a est une valeur falsy
if not a:
    print('gagné')  # Ce bloc s'exécutera seulement si a est falsy
elif a:
    print('perdu')  # Ce bloc s'exécutera seulement si a est truthy
