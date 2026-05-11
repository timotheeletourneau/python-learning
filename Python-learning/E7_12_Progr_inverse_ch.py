import sys  # Permet de modifier le chemin d'accès pour inclure des modules externes

# Ajoute le dossier où se trouve le fichier 'dessins_tortue.py' pour pouvoir l'importer
sys.path.append(r"D:\Python\ProjetPython\Modules_de_fonction")

# Importe la fonction 'inverse' du module 'E7_12_Foncti_inverse_ch' pour pouvoir l'utiliser
from E7_12_Foncti_inverse_ch import inverse

# Appelle la fonction 'inverse' avec une chaîne de caractères en argumment et affiche le résultat
print(inverse("? tiordne'l à ut-sE"))
