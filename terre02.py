import sys

if len(sys.argv) > 1:
    print("Arguments reçus :")
    
    for arg in sys.argv[1:]:
        print(arg)
else:
    print("Aucun argument fourni.")
    
