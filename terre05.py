import sys

# Vérifier si le nombre d'arguments est correct
if len(sys.argv) != 3:
    print("Erreur : Veuillez entrer deux nombres.")
    sys.exit(1)

try:
    num1 = int(sys.argv[1])
    num2 = int(sys.argv[2])

    # Vérification des erreurs
    if num2 == 0:
        print("Erreur.")
    elif num1 < num2:
        print("Erreur.")
    else:
        # faire la division et afficher le résultat et le reste
        print(f"résultat: {num1 // num2}")
        print(f"reste: {num1 % num2}")

except ValueError:
    print("Erreur : Veuillez entrer des nombres valides.")
    sys.exit(1)
