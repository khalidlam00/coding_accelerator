def afficher_alphabet_depuis(lettre):
    # Vérifier si la lettre est valide
    if 'a' <= lettre <= 'z':
        # Afficher l'alphabet à partir de la lettre donnée
        alphabet = [chr(i) for i in range(ord(lettre), ord('z') + 1)]
        print(' '.join(alphabet))
    else:
        print("Veuillez entrer une lettre minuscule valide (a-z).")
        
        # Exemple d'utilisation
lettre_debut = input("Entrez une lettre minuscule (a-z) : ")
afficher_alphabet_depuis(lettre_debut)