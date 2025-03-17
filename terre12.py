import sys

def trouver_valeur_milieu(a, b, c):
    if a == b == c:
        return "erreur."

    if (a <= b <= c) or (c <= b <= a):
        return b
    elif (b <= a <= c) or (c <= a <= b):
        return a
    else:
        return c

# Vérifier si trois arguments ont été passés
if len(sys.argv) != 4:
    print("Usage: python exo.py <entier1> <entier2> <entier3>")
    sys.exit(1)

# Convertir les arguments en entiers
try:
    entier1 = int(sys.argv[1])
    entier2 = int(sys.argv[2])
    entier3 = int(sys.argv[3])
except ValueError:
    print("Erreur : Les arguments doivent être des entiers.")
    sys.exit(1)

# Trouver et afficher la valeur du milieu
valeur_milieu = trouver_valeur_milieu(entier1, entier2, entier3)
print(valeur_milieu)
