import sys  # Permet de récupérer les arguments passés en ligne de commande

# Vérifier si un argument est fourni
if len(sys.argv) != 2:
    print("Erreur : Vous devez entrer une chaîne de caractères en argument.")
    sys.exit(1)  

# Récupérer la chaîne passée en argument
chaine = sys.argv[1]

# Initialiser un compteur
compteur = 0

# Parcourir la chaîne et compter chaque caractère
for caractere in chaine:
    compteur += 1  # On ajoute 1 à chaque caractère trouvé

# Afficher le résultat
print("Nombre de caractères :", compteur)
