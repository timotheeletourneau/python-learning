import sys  # Permet de modifier le chemin d'accès pour inclure des modules externes

# Ajoute le dossier où se trouve le fichier 'dessins_tortue.py' pour pouvoir l'importer
sys.path.append(r"D:\Python\ProjetPython\Modules_de_fonction")

from E7_9_Foncti_occurences_e import compteCar  # Importe la fonction 'compteCar' du module 'fonct_hors_turt'

# Appelle la fonction 'compteCar' avec les arguments "e" (le caractère à compter) 
# et "Cette phrase est un exemple" (la chaîne dans laquelle chercher)
print(compteCar("e", "Cette phrase est un exemple"))
