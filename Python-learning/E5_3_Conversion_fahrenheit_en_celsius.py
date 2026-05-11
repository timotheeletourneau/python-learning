# Fonction pour convertir de Fahrenheit à Celsius
def conversion_en_celsius(temp_fahr):
    # Conversion en Celsius en utilisant la formule
    cel = (temp_fahr - 32) / 1.8
    # Retourner la valeur en Celsius
    return cel

# Définir une température en Fahrenheit
temp_fahr = 100
# Appeler la fonction pour convertir la température en Celsius
cel = conversion_en_celsius(temp_fahr)

# Fonction pour convertir de Celsius à Fahrenheit
def conversion_en_fahren(temp_cels):
    # Conversion en Fahrenheit en utilisant la formule
    far = (temp_cels * 1.8) + 32
    # Retourner la valeur en Fahrenheit
    return far

# Définir une température en Celsius
temp_cels = 37.78
# Appeler la fonction pour convertir la température en Fahrenheit
far = conversion_en_fahren(temp_cels)

# Arrondir les résultats à 2 décimales
cel = round(cel, 2)
far = round(far, 2)

# Afficher les résultats avec les valeurs arrondies
print(f"{temp_fahr}°F -> {cel}°C")
print(f"{temp_cels}°C -> {far}°F")
