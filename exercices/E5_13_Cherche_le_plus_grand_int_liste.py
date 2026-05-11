t1 = [32, 5, 12, 8, 3, 75, 2, 15]  # Liste de nombres dans laquelle on cherche le plus grand élément

grand = 0  # On initialise la variable 'grand' à 0, elle servira à stocker le plus grand nombre rencontré

for nombre in t1:  # On parcourt chaque nombre de la liste t1
    if nombre > grand:  # Si le nombre courant est plus grand que ce que l'on a déjà enregistré dans 'grand'
        grand = nombre  # Alors on met à jour 'grand' pour qu'il prenne la valeur de ce nombre

print(f"Le plus grand élément de cette liste a la valeur {grand}")  
# Après avoir parcouru toute la liste, on affiche la valeur finale de 'grand', c'est-à-dire le plus grand nombre

    
    
    
