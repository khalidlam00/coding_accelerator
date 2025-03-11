import sys 

# nombre d'arguments
if len(sys.argv) !=3:
    print("erreur: tu ne vas pas me la mettre à l'envers entre 2 arguments")
    sys.exit(1)

try:
    base = int(sys.argv[1]) # convertir en entier
    exposant = int(sys.argv[2])    # CONVERTIR EN ENTIER

    if exposant < 0:
        print("Erreur")
        sys.exit(1)

# calcul de la puissance
    resultat = 1
    for _ in range(exposant):
        resultat *= base # x la base par l'exposant
    print(resultat)

except ValueError:
    print("Erreur : Les arguments doivent être des nombres entiers.")
    sys.exit(1)