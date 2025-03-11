import sys 

# nombre d'arguments
if len(sys.argv) !=2:
    print("erreur: tu ne vas pas me la mettre à l'envers entre 1 arguments entier")
    sys.exit(1)
try: 
    nombre = int(sys.argv[1])

    if nombre < 0:
        print("erreur le nombre doit être positif")
        sys.exit(1)

# Trouver la racine carré
    racine = 0 
    while racine * racine < nombre:
        racine += 1

    if racine * racine == nombre:
        print(racine)
    else:
        print("erreur le nombre n'a pas une racine carré entière")

except ValueError:
    print("erreur : l'argument doit être un nombre entier")
    sys.exit(1)