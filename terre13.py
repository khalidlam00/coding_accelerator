import sys

def est_triee(liste):
    for i in range(len(liste) - 1):
        if liste[i] > liste[i + 1]:
            return False
    return True

# Vérifier si des arguments 
if len(sys.argv) < 2:
    print("Usage: python exo.py <entier1> <entier2> ... <entierN>")
    sys.exit(1)

# Convertir les arguments en entiers
try:
    entiers = list(map(int, sys.argv[1:]))
except ValueError:
    print("erreur tu ne veux me la faire à l'envers.")
    sys.exit(1)

# Vérifier si la liste est triée
if est_triee(entiers):
    print("Triée chef!")
else:
    print("Pas triée chef!")
