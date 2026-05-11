import sys  # Permet de modifier le chemin d'accès pour inclure des modules externes

# Ajoute le dossier où se trouve le fichier 'dessins_tortue.py' pour pouvoir l'importer
sys.path.append(r"D:\Python\ProjetPython\Modules_de_fonction")

# Importe la fonction 'indexMax' du module 'fonct_hors_turt' pour pouvoir l'utiliser
from E7_10_Foncti_indexMax_liste import indexMax

# Crée une liste d'exemple contenant des entiers
serie = [5, 8, 2, 1, 9, 3, 6, 7]

# Appelle la fonction 'indexMax' avec la liste pour trouver l'index de la valeur maximale
# Et affiche le résultat à l'écran
print(indexMax(serie))
