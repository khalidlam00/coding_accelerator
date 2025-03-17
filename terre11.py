import sys

def convertir_heure_24h_en_12h(heure_24h):
    try:
        # Séparer l'heure et les minutes
        heure, minutes = map(int, heure_24h.split(':'))
    except ValueError:
        print("Erreur : L'heure doit être au format HH:MM")
        sys.exit(1)

    # Vérifier que l'heure est valide
    if heure < 0 or heure > 23 or minutes < 0 or minutes > 59:
        print("Erreur : L'heure doit être comprise entre 00:00 et 23:59")
        sys.exit(1)

    # Déterminer AM ou PM
    if heure == 0:
        period = "AM"
        heure_12h = 12
    elif heure == 12:
        period = "PM"
        heure_12h = 12
    elif heure < 12:
        period = "AM"
        heure_12h = heure
    else:
        period = "PM"
        heure_12h = heure - 12

    # Formater l'heure en 12h
    heure_12h_str = f"{heure_12h}:{minutes:02d}{period}"
    return heure_12h_str

# Vérifier si un argument a été passé
if len(sys.argv) != 2:
    print("Usage: python convertir_heure.py HH:MM")
    sys.exit(1)

heure_24h = sys.argv[1]
heure_12h = convertir_heure_24h_en_12h(heure_24h)
print(heure_12h)
