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
            # on transforme chaque ligne "x" en sous_liste et on supprime les retour a la ligne)
            return [list(line.strip("\n")) for line in f.readlines()]
    except:
        print(f"Erreur : impossible de lire le fichier {filename}")
        sys.exit()

def rectangle(array):
    # on met au format rectangle en commblant les vides par des espaces
    max_length = max(len(row) for row in array)
    array = [row + [" "] * (max_length - len(row)) for row in array]
    return array

def find_shape(board, shape):
    #trouver la taille de la forme x et y
    shape_x = len(shape[0])
    shape_y = len(shape)
    board_x = len(board[0])
    board_y = len(board)
    print(f"shape_x = {shape_x}")
    print(f"shape_y = {shape_y}")
    print(f"board_x = {board_x}")
    print(f"board_y = {board_y}")
    # de cette manière on délimite jusqu'à quel étage on peut descendre pour trouver le 1 er élément commun sans sortir du board
    for yb in range(board_y - shape_y + 1):
        print(f"yb = {yb}")
        # de cette manière on délimite jusqu'ou sur la ligne on peut trouver le 1 er élément commun sans sortir du board
        for xb in range(board_x - shape_x + 1):
            print(f"xb = {xb}")
            found = True
            # va permettre de compté le nombre d'espace au début de la forme pour incrémenté les coordonnées de x à retourner
            start_space = 0
            # permet de savoir si il s'agit d'espace au début de la forme ou é la fin car si se sont des espaces de la fin on n'incrément pas start_space
            first_element = True
            # on va chercher les élément de la forme l'un apres l'autre pour et les comparer avec les éléments du tableau
            for ys in range(shape_y):
                print(f"ys = {ys}")
                for xs in range(shape_x):
                    print(f"xs = {xs}")
                    # lorsque l'on veut donnée les coordonnées de tableau imbriqué on donne en premier les y (étages) et ensuite les x (position dans l'étage)
                    print(f"shape[ys][xs] = {shape[ys][xs]}")
                    # si l'élément shape est un espace on va a l'élélment suivant
                    if shape[ys][xs] != " " and shape[ys][xs] != board[yb + ys][xb + xs]:
                        print(f"board[yb + ys][xb + xs] = {board[yb + ys][xb + xs]}")
                        found = False
                        print("break")
                        break
                    print(f"board[yb + ys][xb + xs] = {board[yb + ys][xb + xs]}")
                    print("correspond")
                    # si élément est un espace du début de la forme on incrément notre variable start_space
                    if shape[ys][xs] == " " and first_element:
                        start_space += 1
                        print("space")
                        first_element = True  
                    # ici on permet de savoir qu'il ya eu élément autre qu'un espace donc nous ne sommes plus au début de la forme on stop l'incrémentation de start_space                      
                    elif shape[ys][xs] != " ":
                        first_element = False
                # permet de remonté au boucle tu tableau board pour parcourir l'élément suivant du board
                if not found:
                    break
            if found:
                if start_space > 0:
                    return xb + start_space, yb
                else :
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
board = rectangle(board)
shape = rectangle(shape)
print(board)
print(shape)

## Resolution
position = find_shape(board, shape)

## Display
print_position(position)
