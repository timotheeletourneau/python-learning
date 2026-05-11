# Chaîne de caractères à tester
pal = "elle"

# Définition d'une fonction pour tester si la chaîne est un palindrome
def test_palindrome(pal):
    # Vérifie si la chaîne est égale à sa version inversée
    if pal == pal[::-1]:
        print(f"C'est un palindrome")
    else:
        print(f"Ce n'est pas un palindrome")

# Appel de la fonction avec la chaîne définie
test_palindrome(pal)
