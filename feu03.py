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

## Error handling
error_handling(sys.argv)
sudoku = read_file(sys.argv[1])
is_sudoku(sudoku)

## Resolution
print("ok")
