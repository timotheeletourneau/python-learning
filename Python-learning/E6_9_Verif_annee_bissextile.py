# Demande à l'utilisateur de saisir une année
saisie = input("Saisir une année : ")

# Conversion de la saisie en entier
valeur = int(saisie)

# Vérification des conditions pour déterminer si l'année est bissextile
# 1. L'année est divisible par 4 mais pas par 100, ou
# 2. L'année est divisible par 400.
if (valeur % 4 == 0 and valeur % 100 != 0) or (valeur % 400 == 0):
    # Si l'une des conditions est vraie, l'année est bissextile
    print("C'est une année bissextile", end=" ")
else:
    # Sinon, l'année n'est pas bissextile
    print("Ce n'est pas une année bissextile", end=" ")
