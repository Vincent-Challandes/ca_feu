## Modules and functions
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
            return [[int(cell) if cell.isdigit() else 0 for cell in line.strip("\n")] for line in f.readlines()]
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

def is_valid(sudoku, row, col, num):
    for i in range(9):
        # on check chaque ligne et chaque colone que le num ne soit pas dejà présent
        if sudoku[row][i] == num or sudoku[i][col] == num:
            return False
    # on check si le num est déjà présent dans la sous-grille 3x3 à laquelle appartient la case.
    # avec cette formule on trouve a chaque fois la case en haut a gauche de chaque sous-grille 3x3
    # exemple row = 5 : 5 - 5 % 3 = 5 - 2(5%3=2 car 1 fois 3 dans 5 reste 2 ) = 3 donc start row egale 3   ATTENTION on commence à 0
    # de cette manière on obtient soit 0, 3 ou 6 comme valeur qui sont les valeurs des 9 coin de départ des sous-grille 3x3
    start_row, start_col = row - row % 3, col - col % 3
    for i in range(3):
        for j in range(3):
            if sudoku[i + start_row][j + start_col] == num:
                return False
    return True

def solve_sudoku(sudoku):
    row, col = -1, -1
    vide = False
    # on cherche la première case vide
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                row, col = i, j
                vide = True
                break
        if vide:
            break
    # si plus de case vide la résolution est terminée
    if not vide:
        return True
    # ici on cherche un chiffre entre 1 et 10 pour notre case vide et on check avec notre fonction is_valid si oui on ajoute se numéro à la case vide.
    for num in range(1, 10):
        if is_valid(sudoku, row, col, num):
            sudoku[row][col] = num
            # la on va maintenant rappeler la fonction solve_sudoku() de manière récursive
            # du coup on va passer a la prochaine case vide et refaire le même process
            # si a un moment ca ne fonctionne plus le if n'est plus accepter donc la récursive n'a pas trouvé de solution
            # on remet la case à zéro puis on essai avec le chiffre valide suivant.
            if solve_sudoku(sudoku):
                return True
            sudoku[row][col] = 0
    return False

def print_2d_array(array):
    for row in array:
        # on concatenate tous les élément d'une ligne en une chaine de caratère et la print
        # on parse en str chacun des entiers
        print("".join(str(e) for e in row))

## Error handling
error_handling(sys.argv)

## Parsing
sudoku = read_file(sys.argv[1])
is_sudoku(sudoku)

# Resolution
if solve_sudoku(sudoku):
    print_2d_array(sudoku)
else:
    print("Pas de solution")
