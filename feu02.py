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
    # la on créer un tableau array_display qui à exacement le format de board mais ou chaque élément est remplacé par "-"
    # donc il s'agit d'une compréhension de liste 
    # for row in board donc chaque ligne du board puis on boucle dans chaque ligne et remplace chaque élément par "-" avec "-" for _ in range(len(row))
    # le _ aurait pu être i ca ne change rien mais par convention si on ne fait rien avec les valeur des élément on met _ c'est tous
    array_display = [["-" for _ in range(len(row))] for row in board]
    #trouver la taille de la forme x et y
    shape_x = len(shape[0])
    shape_y = len(shape)
    board_x = len(board[0])
    board_y = len(board)
    # de cette manière on délimite jusqu'à quel étage on peut descendre pour trouver le 1 er élément commun sans sortir du board
    for yb in range(board_y - shape_y + 1):
        # de cette manière on délimite jusqu'ou sur la ligne on peut trouver le 1 er élément commun sans sortir du board
        for xb in range(board_x - shape_x + 1):
            found = True
            # va permettre de compté le nombre d'espace au début de la forme pour incrémenté les coordonnées de x à retourner
            start_space = 0
            # permet de savoir si il s'agit d'espace au début de la forme ou é la fin car si se sont des espaces de la fin on n'incrément pas start_space
            first_element = True
            # on va chercher les élément de la forme l'un apres l'autre pour et les comparer avec les éléments du tableau
            for ys in range(shape_y):
                for xs in range(shape_x):
                    # lorsque l'on veut donnée les coordonnées de tableau imbriqué on donne en premier les y (étages) et ensuite les x (position dans l'étage)
                    # si l'élément shape est un espace on va a l'élélment suivant
                    if shape[ys][xs] != " " and shape[ys][xs] != board[yb + ys][xb + xs]:
                        found = False
                        break
                    # si élément est un espace du début de la forme on incrément notre variable start_space
                    if shape[ys][xs] == " " and first_element:
                        start_space += 1
                        first_element = True  
                    # ici on permet de savoir qu'il ya eu élément autre qu'un espace donc nous ne sommes plus au début de la forme on stop l'incrémentation de start_space                      
                    elif shape[ys][xs] != " ":
                        first_element = False
                        # on ajout au tableau array_display les valeur trouvé pour autant que l'élément de recherche shape[ys][xs] n'est pas un espace
                        array_display[yb + ys][xb + xs] = shape[ys][xs]
                # permet de remonté au boucle tu tableau board pour parcourir l'élément suivant du board
                if not found:
                    break
            if found:
                if start_space > 0:
                    return xb + start_space, yb, array_display
                else :
                    return xb, yb, array_display
            # ici on écrase a nouveau les valeur avec "-" car nous avons pas trouvé la forme entière donc on passe a l'élément suivant du tableau.
            array_display = [["-" for _ in range(len(row))] for row in board]
    return None

def print_position(position):
    #Fonction qui affiche la position de la forme ou le message 'Introuvable' si la forme n'a pas été trouvée
    if position:
        print("Trouvé !")
        print(f"Coordonnées : {position[0]},{position[1]}")
        print_2d_array(position[2])
    else:
        print("Introuvable")

def print_2d_array(array):
    for row in array:
        # on concatenate tous les élément d'une ligne en une chaine de caratère et la print
        print("".join(row))
                   
## Error handling
error_handling(sys.argv)

## Parsing
board = read_file(sys.argv[1])
shape = read_file(sys.argv[2])

## Resolution
board = rectangle(board)
shape = rectangle(shape)
position = find_shape(board, shape)

## Display
print_position(position)
    