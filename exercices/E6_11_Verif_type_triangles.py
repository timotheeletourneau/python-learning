# Demande à l'utilisateur de saisir les longueurs des côtés du triangle
longu_a = input("Saisir longueur a : ")
longu_b = input("Saisir longueur b : ")
longu_c = input("Saisir longueur c : ")

# Conversion des entrées de l'utilisateur en nombres flottants
a = float(longu_a)
b = float(longu_b)
c = float(longu_c)

# Fonction pour tester si les longueurs peuvent former un triangle valide
def test_triangle(a, b, c):
    # La condition vérifie que la somme de deux côtés est toujours plus grande que le troisième côté
    # C'est le critère de validité d'un triangle selon l'inégalité triangulaire
    if (a + b > c) and (a + c > b) and (b + c > a):
        return True  # Si la condition est vraie, c'est un triangle possible
    else:
        return False  # Sinon, ce n'est pas un triangle

# Fonction pour déterminer le type du triangle
def type_triangle(a, b, c):
    # On commence par tester si le triangle est valide
    if not test_triangle(a, b, c):
        print("Il n'est pas possible de construire un triangle")  # Si ce n'est pas un triangle, on l'affiche
        return  # On arrête l'exécution de la fonction ici
    
    # Si on arrive ici, cela signifie que les longueurs forment un triangle valide
    print("Il est possible de construire un triangle")

    # On vérifie si le triangle est rectangle en utilisant le théorème de Pythagore
    # Un triangle rectangle respecte la relation a^2 + b^2 = c^2 (ou l'une de ses permutations)
    if (a ** 2 + b ** 2 == c ** 2) or (a ** 2 + c ** 2 == b ** 2) or (b ** 2 + c ** 2 == a ** 2):
        print("Le triangle est rectangle")
    
    # On vérifie ensuite si le triangle est isocèle (deux côtés égaux)
    elif (a == b) or (a == c) or (b == c):
        print("Le triangle est isocèle")
    
    # Si tous les côtés sont égaux, le triangle est équilatéral
    elif a == b == c:
        print("Le triangle est équilatéral")
    
    # Si aucune des conditions précédentes n'est remplie, le triangle est scalène (tous les côtés sont différents)
    else:
        print("Le triangle est scalène, (ou quelconque)")

# Appel de la fonction pour déterminer le type du triangle en utilisant les longueurs fournies
type_triangle(a, b, c)
