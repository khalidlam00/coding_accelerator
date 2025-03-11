try:
    n = int(input("Tapez la valeur de n : "))

    if n < 2:
        print(f"Le nombre {n} n'est pas premier.")
    else:
        # Vérification de la racine carrée de n
        est_premier = True
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                est_premier = False
                break

        if est_premier:
            print(f"Le nombre {n} est premier.")
        else:
            print(f"Le nombre {n} n'est pas premier.")

except ValueError:
    print("Erreur : Veuillez entrer un nombre entier valide.")
