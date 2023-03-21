## Modules and Functions
import sys

def error_handling(arguments):
    if not len(arguments) == 3:
        print("Error need 2 files in argument arg1 = board and arg2 = to_find")
        sys.exit()

def read_file(filename):
    ##Fonction qui lit le contenu d'un fichier et retourne son contenu sous forme de liste de chaînes de caractères
    try:
        with open(filename, 'r') as f:
            return f.read().splitlines()
    except:
        print(f"Erreur : impossible de lire le fichier {filename}")
        sys.exit()

def find_shape(board, shape):
    #trouver la taille de la forme x et y
    shape_x = len(shape[0])
    print(f"shape_x = {shape_x}")
    shape_y = len(shape)
    print(f"shape_y = {shape_y}")
    board_x = len(board[0])
    print(f"board_x = {board_x}")
    board_y = len(board)
    print(f"board_y = {board_y}")
    # de cette manière on délimite jusqu'à quel étage on peut descendre pour trouver le 1 er élément commun sans sortir du board
    for yb in range(board_y - shape_y + 1):
        print(f"yb = {yb}")
        # de cette manière on délimite jusqu'ou sur la ligne on peut trouver le 1 er élément commun sans sortir du board
        for xb in range(board_x - shape_x + 1):
            print(f"xb = {xb}")
            found = True
            # on va chercher les élément de la forme l'un apres l'autre pour et les comparer avec les éléments du tableau
            for ys in range(shape_y):
                print(f"ys = {ys}")
                for xs in range(shape_x):
                    print(f"xs = {xs}")
                    # lorsque l'on veut donnée les coordonnées de tableau imbriqué on donne en premier les y (étages) et ensuite les x (position dans l'étage)
                    if shape[ys][xs] != " " and shape[ys][xs] != board[yb + ys][xb + xs]:
                        found = False
                        print("break")
                        break
                    print("correspond")
                if not found:
                    break
            if found:
                return xb, yb
    return None

def print_position(position):
    #Fonction qui affiche la position de la forme ou le message 'Introuvable' si la forme n'a pas été trouvée
    if position:
        print("Trouvé !")
        print(f"Coordonnées : {position[0]},{position[1]}")
    else:
        print("Introuvable")
                   
## Error handling
error_handling(sys.argv)

## Parsing
board = read_file(sys.argv[1])
shape = read_file(sys.argv[2])
print(board)
print(shape)

## Resolution
position = find_shape(board, shape)

## Display
print_position(position)