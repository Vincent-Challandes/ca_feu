## Modules and Functions
import sys

def error_handling(arguments):
    if not len(arguments) == 2:
        print("Error need 1 file in argument that is a sudoku")
        sys.exit()

def read_file(filename):
    ##Fonction qui lit le contenu d'un fichier et retourne son contenu sous forme de liste de chaînes de caractères
    try:
        with open(filename, 'r') as f:
            # on transforme chaque ligne "x" en sous_liste et on supprime les retour a la ligne)
            return [list(line.strip("\n")) for line in f.readlines()]
    except:
        print(f"Error : cannot read the file {filename}")
        sys.exit()

def is_sudoku(sudoku):
    # column = x et row = y
    column = 0
    row = 0
    for i in range(len(sudoku)):
        for j in range(len(sudoku[i])):
            column += 1 
        if column != 9:
            print("Error column : is not a sudoku")
            sys.exit()
        column = 0
        row += 1
    if row != 9:
        print("Error row : is not a sudoku")
        sys.exit()

def resolve_sudoku(sudoku):
    unknown = True
    while unknown == True:
        unknown = False
    # on check par ligne
        for i in range(len(sudoku)):
            count_nbx = 0
            index = ""
            nb_unknown = 0
            for j in range(len(sudoku[i])):
                if sudoku[i][j] != ".":
                    count_nbx += int(sudoku[i][j])
                else:
                    unknown = True
                    index = j
                    nb_unknown += 1
            if nb_unknown == 1:
                sudoku[i][index] = str(45 - count_nbx)
        # on check par colonne
        for k in range(len(sudoku)): 
            count_nby = 0
            index = ""
            nb_unknown = 0
            for l, row in enumerate(sudoku):
                if row[k] != ".":
                    count_nby += int(row[k])
                else:
                    unknown = True
                    index = l
                    nb_unknown += 1
            if nb_unknown == 1:
                sudoku[index][k] = str(45 - count_nby)
    return sudoku

def print_2d_array(array):
    for row in array:
        # on concatenate tous les élément d'une ligne en une chaine de caratère et la print
        print("".join(row))

## Error handling
error_handling(sys.argv)
sudoku = read_file(sys.argv[1])
is_sudoku(sudoku)

## Resolution
result_sudoku = resolve_sudoku(sudoku)
print_2d_array(result_sudoku)
