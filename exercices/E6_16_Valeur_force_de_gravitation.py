G = 6.67 * (10 ** -11)  # constante gravitationnelle en N·m²/kg²
m1 = 10000               # masse 1 en kg
m2 = 10000               # masse 2 en kg
d0 = 0.05                # distance initiale entre les masses en m

while d0 < 50:           # boucle tant que la distance est inférieure à 50 m
    F = G * (m1 * m2) / d0 ** 2  # calcul de la force gravitationnelle pour la distance actuelle
    # préparation de l'affichage de la distance : enlever le 0 initial si d < 1
    print(f"d = {str(f'{d0:.2f}')[1:]} m : la force vaut {F:.3f} N")  
    d0 = d0 * 2           # passer à la distance suivante dans la progression géométrique (double la distance)
