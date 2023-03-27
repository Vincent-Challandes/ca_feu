## Modules and Functions
import sys

def error_handling(arguments):
    if not len(arguments) == 2:
        print("Error need 1 file in argument as a map")
        sys.exit()

def read_file(filename):
    ##Fonction qui lit le contenu d'un fichier et retourne son contenu sous forme de liste de chaînes de caractères
    try:
        with open(filename, 'r') as f:
            # on transforme chaque ligne "x" en sous_liste et on supprime les retour a la ligne)
            # f.readlines()[1:] permet de commencé a la seconde ligne et finir à la fin
            return [list(line.strip("\n")) for line in f.readlines()[1:]]
    except:
        print(f"Error : cannot read {filename}")
        sys.exit()

def main(my_map):
    if len(my_map) > 1 and len(my_map[0]) > 1:
        map_y = len(my_map)
        map_x = len(my_map[0])
    else:
        print("Error : your map is not 2d")
        sys.exit()
    if map_y >= map_x :
        size_square = map_x
    else:
        size_square = map_y
    while size_square > 0:
        result = find_biggest_square(my_map, size_square, map_x, map_y)
        if not result == False:
            return result
        size_square -= 1
    return False

def find_biggest_square(my_map, size_square_to_find, x, y):
    # on place le curseur pour le départ du check du carré en haut à gauche
    for ym in range(y - size_square_to_find + 1):
            for xm in range(x - size_square_to_find + 1):
                # on cheque tous le carré
                found_obstacle = False
                for ys in range(size_square_to_find):
                    for xs in range(size_square_to_find):
                        if my_map[ym + ys][xm + xs] == "x":
                            found_obstacle = True
                            break
                    if found_obstacle:
                        break
                if not found_obstacle:
                    for ys in range(size_square_to_find):
                        for xs in range(size_square_to_find):
                            my_map[ym + ys][xm + xs] = "o"
                    return my_map
    return False            
        
def print_2d_array(array):
    for row in array:
        # on concatenate tous les élément d'une ligne en une chaine de caratère et la print
        print("".join(row))

## Error handling
error_handling(sys.argv)

## Parsing
my_map = read_file(sys.argv[1])

## Resolution
map_with_biggest_square = main(my_map)

## Display
if not map_with_biggest_square == False:
    print_2d_array(map_with_biggest_square)
else:
    print("Error cannot found square")
