a = 42

# Implémantation similaire au switch-case : match (>= Python 10)
match a:
    case 1:
        print("Premier")
    case 2:
        print("Deuxième")
    case 42:
        print("The Answer")
    case _:
        print("Autre cas")
