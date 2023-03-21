## Modules and Functions
import sys
import os

def error_handling(arguments):
    if not len(arguments) == 3:
        sys.exit("Error need 2 files in argument arg1 = board and arg2 = to_find")
    if not os.path.exists(arguments[1])or not os.path.exists(arguments[2]):
        sys.exit("Error files not found")

def get_lignes_inside_file(file):
    with open(file, "r") as fichier:
        array_lignes = fichier.readlines()
    return array_lignes

def board_is_rectangle(board_in_array_of_lignes):
    for i in range(1):
        for j in range(1, len(board_in_array_of_lignes)):
            # on compare le nombre de caratère de la premiere ligne du board avec le nombre de caratère de chaque autre ligne
            # afin de savoir si le board est rectangulaire
            if len(board_in_array_of_lignes[i]) != len(board_in_array_of_lignes[j]):
                sys.exit("Error your board is not rectanlge")

def put_in_array_x_y(array_of_lignes):
    array_x_y = []
    for ligne in array_of_lignes:
        array_x_y.append(list(ligne))
    return array_x_y

def find_coordinates(array_x_y):
    nb_element = 0
    array_coords_x = []
    array_coords_y = []
    for i, row in enumerate(array_x_y):
        for j, cell in enumerate(row):
            if cell != " " and cell != "\n":
                array_coords_x.append(j)
                array_coords_y.append(i)
                nb_element += 1
    return array_coords_x, array_coords_y, nb_element

def find_in_board(array_board, array_to_find, nb_element_to_find, nb_element_board):
    # Ici on a une fonction qui va chercher la forme c'est a dire on parcourt notre board à la recherche du premier element to find
    # et si il est trouver on increment les x et y afin de voir si les element suivant corresponde à la suite des elements de la forme. 
    # Si ne corresponde pas on break et on passe plus loin dans notre board vois si il ya a nouveau notre forme
    # on parcourt les élément du board à l'aide des coordonnée xb et yb
    for i in range(nb_element_board):
        found = True
        xb = array_coords_x_board[i]
        #print(f"xb = {xb}")
        yb = array_coords_y_board[i]
        #print(f"yb = {yb}")
        # on parcourt les élément de to_find à l'aide des coordonnée xf et yf
        for j in range(nb_element_to_find):
            xf = array_coords_x_to_find[j]
            #print(f"xf = {xf}")
            yf = array_coords_y_to_find[j]
            #print(f"yf = {yf}")
            # tant que les éléments sont les bon on avance sinon on break et on va a la prochaine position ou la forme est présente
            if array_x_y_to_find[yf][xf] != array_x_y_board[yb + yf][xb + xf]:
                found = False
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
board = sys.argv[1]
to_find = sys.argv[2]

## Resolution
lignes_board = get_lignes_inside_file(board)
#print(f"lignes_board = {lignes_board}")
lignes_to_find = get_lignes_inside_file(to_find)
#print(f"ligne_to_find = {lignes_to_find}")
board_is_rectangle(lignes_board)
array_x_y_board = put_in_array_x_y(lignes_board)
#print(f"array_x_y_board = {array_x_y_board}")
array_x_y_to_find = put_in_array_x_y(lignes_to_find)
#print(f"array_x_y_to_find = {array_x_y_to_find}")
array_coords_x_to_find, array_coords_y_to_find, nb_element_to_find = find_coordinates(array_x_y_to_find)
#print(f"array_coords_x_to_find, array_coords_y_to_find, nb_element_to_find = {array_coords_x_to_find, array_coords_y_to_find, nb_element_to_find }")
array_coords_x_board, array_coords_y_board, nb_element_board = find_coordinates(array_x_y_board)
#print(f"array_coords_x_board, array_coords_y_board, nb_element_board = {array_coords_x_board, array_coords_y_board, nb_element_board }")
position = find_in_board(array_x_y_board, array_x_y_to_find, nb_element_to_find, nb_element_board)

## Display
print_position(position)