## Modules and functions
import sys
from queue import Queue

def error_handling(arguments):
    if len(arguments) != 2:
        print("Error: need file as an argument")
        sys.exit()

def read_file(filename):
    ##Fonction qui lit le contenu d'un fichier et retourne son contenu sous forme de liste 2d
    try:
        with open(filename, 'r') as f:
            # on transforme chaque ligne "x" en sous_liste et on supprime les retour a la ligne
            # f.readlines()[1:] permet de commencé a la seconde ligne et finir à la fin
            return [list(line.strip("\n")) for line in f.readlines()]
    except:
        print(f"Error : cannot read {filename}")
        sys.exit()

def check_laby(laby):
    # on récupère les caractère qui sont autorisé dans le labyrinthe
    carakter_accept = laby[0][-5:]
    # ici on check que ce soit bien un rectangle par qu'il manque des caractères
    # on contrôle que chaque ligne fasse la meme longueur
    width = len(laby[1])
    for row in laby[1:]:
        if len(row) != width:
            print("Error : map is not a rectangle")
            sys.exit()
    # On vérifie que tous les caractères sont valides
    for row in laby[1:]:
        for char in row:
            if char not in carakter_accept:
                print("Error : map has wrong string")
                sys.exit()

def solve_laby(labyrinthe):
    print("fonction solve")
    info = labyrinthe[0]
    wall = info[-5]
    path_symbol = info[-3]
    laby = labyrinthe[1:]
  
    start = ""
    nb_target = 0
    targets = []
    # on cherche la position de départ ainsi que les positions des sorties
    for i in range(len(laby)):
        for j in range(len(laby[i])):
            if laby[i][j] == info[-2]:
                start = i, j

            elif laby[i][j] == info[-1]:
                nb_target += 1
                target = i, j
                targets.append(target)

    print(start)
    print(targets)    
    print(wall)
    path = my_bfs(laby, start, targets, wall)
    return display_result_laby(laby, path, path_symbol)

# algorithme de recherche en largeur BFS implémenté par une boucle while.
# le principe on avance 1 pas puis on étudie toutes les possibilités. 
# puis on avance 1 pas dans chacune des possibilité etc. jusqu'a trouvé une sorti
# de cette manière on obtient la solution la plus courte jusqu'a la sorti
def my_bfs(array_2d, start, target, wall):
    rows = len(array_2d)
    cols = len(array_2d[0])
    # fonction set() permet de créer une collection d'élément similaire a une liste mais sans doublon
    visited = set()  # ensemble pour stocker les nœuds visités
    # la fonction Queue() permet d'impiler des élément en les ajoutant dans l'ordre d'arrivé avec put() et en retirer le premier element arriver avec get()
    queue = Queue()  # file pour stocker les nœuds à visiter
    parents = {}  # dictionnaire pour stocker les parents de chaque nœud visité
    
    # Ajouter le nœud de départ à la file
    queue.put(start)
    parents[tuple(start)] = None

    while not queue.empty():
        # Retirer le premier nœud de la file
        current = queue.get()
        row, col = current

        # Vérifier si le nœud actuel est le nœud cible
        if current in target:
            # Reconstituer le chemin parcouru à partir des parents
            path = []
            while current != start:
                path.append(current)
                current = parents[current]
            # on renvoi le chemin dans l'ordre du début a la fin avec [::-1]
            return path[::-1]
        
        # Ajouter tous les voisins non visités à la file
        # voisin d'en haut
        if row > 0 and array_2d[row-1][col] != wall and (row-1, col) not in visited:
            queue.put((row-1, col))
            visited.add((row-1, col))
            parents[(row-1, col)] = current
        # voisin d'en bas
        if row < rows-1 and array_2d[row+1][col] != wall and (row+1, col) not in visited:
            queue.put((row+1, col))
            visited.add((row+1, col))
            parents[(row+1, col)] = current
        # voisin de gauche
        if col > 0 and array_2d[row][col-1] != wall and (row, col-1) not in visited:
            queue.put((row, col-1))
            visited.add((row, col-1))
            parents[(row, col-1)] = current
        # voisin de droite
        if col < cols-1 and array_2d[row][col+1] != wall and (row, col+1) not in visited:
            queue.put((row, col+1))
            visited.add((row, col+1))
            parents[(row, col+1)] = current
    
    # Le nœud cible n'a pas été trouvé
    return None

# Ici on vient tracé le chemin sur le labyrinthe
def display_result_laby(labyrinthe, path, symbol):
    # -1 pour pas changé le symbole de la sortie
    for coords in path[:-1]:
        row, col = coords
        labyrinthe[row][col] = symbol
    return labyrinthe

def print_2d_array(array):
    for row in array:
        # on concatenate tous les élément d'une ligne en une chaine de caratère et la print
        print("".join(row))

## Error handling
error_handling(sys.argv)

## Parsing
labyrinthe_init = read_file(sys.argv[1])

## Resolution
check_laby(labyrinthe_init)
labyrinthe_solve = solve_laby(labyrinthe_init)
print("Labyrinthe au départ :")
print_2d_array(labyrinthe_init[1:])
print()
print("Solution la plus courte pour sortir du labyrinthe")
print(labyrinthe_solve)
print_2d_array(labyrinthe_solve)