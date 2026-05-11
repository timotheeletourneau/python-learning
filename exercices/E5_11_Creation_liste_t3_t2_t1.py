t1 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
# Liste des jours de chaque mois (janvier à décembre)

t2 = ['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin',
      'Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre', 'Décembre']  
# Liste des mois correspondants aux jours de t1

t3 = []  
# Liste vide qui va accueillir les mois et leurs jours, alternés

for i in range(12):  
    # Boucle qui parcourt les indices de 0 à 11 (pour les 12 mois)
    
    t3.append(t2[i])  
    # Ajoute le mois courant (t2[i]) à la liste t3
    
    t3.append(t1[i])  
    # Ajoute le nombre de jours correspondant (t1[i]) juste après le mois

print(t3)  
# Affiche la liste complète t3 une fois la boucle terminée
# Résultat : ['Janvier', 31, 'Février', 28, 'Mars', 31, ... , 'Décembre', 31]

    
    
    
