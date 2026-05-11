import sys  # Permet de modifier le chemin d'accès pour inclure des modules externes

# Ajoute le dossier où se trouve le fichier 'dessins_tortue.py' pour pouvoir l'importer
sys.path.append(r"D:\Python\ProjetPython\Modules_de_fonction")

# Importe la fonction 'nomMois' du module 'fonct_hors_turt' pour pouvoir l'utiliser
from E7_11_Foncti_nomMois_n import nomMois

# Appelle la fonction 'nomMois' avec 11 comme argument et imprime le résultat
# Cela doit afficher "Novembre"
print(nomMois(11))
