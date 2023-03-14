## Modules and functions
import sys

def error_handling(arguments):
    if len(arguments) != 3:
        print("Error needs two arguments")
        sys.exit()
    elif not arguments[1].isdigit() or not arguments[2].isdigit():
        print("Error need two numbers")
        sys.exit()
    elif arguments[1] == "0" or arguments[2] == "0":
        print("Error can't be 0")
        sys.exit()

def rectangle_generator(nb_axe_x, nb_axe_y):
    rectangle = []
    for i in range(nb_axe_y):
        if i == 0 or i == nb_axe_y -1:
            if nb_axe_x == 1:
                rectangle.append("o")
            elif nb_axe_x == 2:
                rectangle.append("o o")
            else:
                rectangle.append(f"o {'- ' * (nb_axe_x -2)}o")
        else:
            if nb_axe_x == 1:
                rectangle.append("|")
            elif nb_axe_x == 2:
                rectangle.append("| |")
            else:
                rectangle.append(f"| {'  ' * (nb_axe_x -2)}|")
    return rectangle

def display_rectangle(array):
    for i in array:
        print(i)

## Error handling
error_handling(sys.argv)

## Parsing
nb_axe_x = int(sys.argv[1])
nb_axe_y = int(sys.argv[2])

## Resolution
array_resultat = rectangle_generator(nb_axe_x, nb_axe_y)

## Display
display_rectangle(array_resultat)
