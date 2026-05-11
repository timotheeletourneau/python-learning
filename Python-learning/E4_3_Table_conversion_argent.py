a, b, c = 2, 1, 1.65    # Initialisation : 
                        # a = 2 (facteur de multiplication)
                        # b = 1 (montant en euros de départ)
                        # c = 1.65 (montant en dollars correspondant au départ)

while b < 32768:        # Tant que le montant en euros (b) est inférieur à 32768, on répète la boucle
    print(f"{b} euros(s)={c:.2f} dollars(s)")  
                        # Affiche le montant actuel en euros et en dollars
                        # .2f formate c pour n’afficher que 2 chiffres après la virgule

    a, b, c = a, b*a, c*a   
                        # Mise à jour des variables à chaque tour :
                        # - a reste le même (toujours 2)
                        # - b devient b*a → donc double à chaque tour
                        # - c devient c*a → donc aussi multiplié par 2 à chaque tour
