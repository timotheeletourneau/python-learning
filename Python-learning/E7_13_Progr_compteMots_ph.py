import sys  # Permet de modifier le chemin d'accès pour inclure des modules externes

# Ajoute le dossier où se trouve le fichier 'E7_13_Foncti_compteMots_ph.py' 
# pour que Python puisse le trouver et l'importer
sys.path.append(r"D:\Python\ProjetPython\Modules_de_fonction")

# Importe la fonction 'compteMots' depuis le module 'E7_13_Foncti_compteMots_ph'
# pour pouvoir l'utiliser directement dans ce script
from E7_13_Foncti_compteMots_ph import compteMots

# Appelle la fonction compteMots avec la phrase "Il y a de la neige"
# et affiche le résultat dans la console
print(compteMots("Il y a un site sefeso qui vient d'exploser"))
