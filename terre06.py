import sys

# Vérification du nombre d'arguments
if len(sys.argv) != 2:
    print("Erreur : Vous devez fournir une chaîne de caractères en argument.")
    sys.exit(1)

# Récupérer l'argument fourni
input_string = sys.argv[1]

# Inverser la chaîne de caractères 
reversed_string = ""
for i in range(len(input_string) - 1, -1, -1):
    reversed_string += input_string[i]

print(reversed_string)
