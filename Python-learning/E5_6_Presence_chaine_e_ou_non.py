ch = ''  # On initialise la chaîne à 'a'

def tester_si_e(ch):  # Définition de la fonction qui teste si 'e' est dans la chaîne
    if 'e' in ch:  # Si 'e' est dans la chaîne
        print("e est dans la chaîne")  # Affichage du message si 'e' est présent
    else:
        print("e n'est pas dans la chaîne")  # Affichage du message si 'e' n'est pas présent

tester_si_e(ch)  # Appel de la fonction sans réassigner 'ch'
