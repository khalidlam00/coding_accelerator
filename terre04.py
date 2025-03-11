# Créez un programme qui permet de déterminer si l’argument donné est un entier pair ou impair..

# Demander à l'utilisateur d'entrer un nombre
try:
    n = int(input("Entrez un nombre: "))  # Entrée utilisateur, convertie en entier
    if n % 2 == 0:  # Vérifie si le nombre est pair
        print("Nombre pair.")
    else:  # Si ce n'est pas pair, alors il est impair
        print("Nombre impair.")
except ValueError:
    print("Tu ne vas pas me la mettre à l'envers.") 