## Modules and Functions
import sys

operator_array = ["+", "-", "*", "/", "%", " ", "(", ")"]

def error_handling(arguments):
    if len(arguments) != 2:
        print("Error need an argument")
        sys.exit()
    for i in sys.argv[1]:
        if not i.isdigit() and not i in operator_array:
            print("Error need an \"arithmetic expression\"")
            sys.exit()

def count_parenthesis(expression):
    count = 0
    for i in expression:
        if i == "(":
            count += 1
    return count

def array_expression(expression):
    # on sépare l'expression par les espace et la met dans un tableau
    array = expression.split()
    first_array = []
    result = ""
    # on va maintenant passé au travers chaque élément du tableau array et séparé les parenthèses
    for i in range(len(array)):
        for j in array[i]:
            print(f"j = {j}")
            if j.isdigit():
                result += f"{j}"
                continue
            # ici on va ajouter result une fois qu'on a plus de nombre qui se suit
            # c'est pour pas séparer les nombres a plus de 1 chiffre comme 21 par exemple
            # le continue permet de checker si chiffre il ya un chiffre qui suit et si pas le cas on ajout result
            # au first_array et on passe a la suite de la fonction
            elif result:
                first_array.append(result)
                result = ""
            if j == "(":
                result += "(" 
                first_array.append(result)
                result = ""
            elif j == ")":
                result += ")"
                first_array.append(result)
                result = ""
            else:
                result += f"{j}"
                first_array.append(result)
                result = ""
    # permet l'ajout du dernier élément si il s'agit d'un nombre.
    if result:
        first_array.append(result)
    return first_array

def calculate_parenthesis(array_expression, nb_parenthesis):
    a = array_expression
    po = index_parentesis_open = []
    pc = index_parentesis_close = []
    nb = nb_parenthesis
    counter = 0
    while counter < nb_parenthesis:
        po = [0]
        pc = []
        for i in range(len(a)):
            if a[i] == "(":
                po.pop()
                po.append(i)
            elif a[i] == ")":
                pc.append(i)
                break
            print(f" po = {po}")
            print(f" pc = {pc}")
        print(f" a[po[0] + 1:pc[0]] = {a[po[0] + 1:pc[0]]}")
        a[po[0]:pc[0] + 1] = calculations(a[po[0] + 1:pc[0]])
        counter += 1
    return a

def calculations(expr):
    # on sépare les nombres des operateurs
    #if type(expression) == str:
        #expr = expression.split()
    #else:
        #expr = expression
    # on parse en integer les nombres
    #for i in range(len(expr)):
        #if type(expr[i]) == str and expr[i].isdigit():
            #expr[i] = int(expr[i])
    # on commence avec "*"
    # on cherche le nombre de chacune de nos opération dans notre array
    op_multiplication = 0
    op_division = 0
    op_modulo = 0
    op_addition = 0
    op_substraction = 0
    for op in expr:
        if op == "*":
            op_multiplication += 1
        elif op == "/":
            op_division += 1
        elif op == "%":
            op_modulo += 1
        elif op == "+":
            op_addition += 1
        elif op == "-":
            op_substraction += 1
    # on traite les multiplications et divisions prioprité dans sens de lecture 
    print(f"avant calcule {expr}")
    for i in range(op_multiplication + op_division):
        # on part de 1 car et fini à - 1 car expr[j - 1:j + 1]
        for j in range(1, len(expr) - 1):
            if expr[j] == "*":
                # on écrase j - 1 et j + 1 par le resultat de j - 1 * j + 1
                print(f" j - 1 = {expr[j - 1]} j + 1 = {expr[j + 1]}")
                expr[j - 1:j + 1] = [int(expr[j - 1]) * int(expr[j + 1])]
                # on pop pour supprimé l'élément J 
                expr.pop(j)
                # ATTENTION pas oublié de break pour ressortir de la boucle remettre le len(expr) à jour sinon IndexOutOfRange et levé
                print(expr)
                break
            elif expr[j] == "/":
                expr[j - 1:j + 1] = [int(expr[j - 1]) / int(expr[j + 1])]
                expr.pop(j)
                print(expr)
                break
    # on traite les modulos
    for i in range(op_modulo):
        for j in range(1, len(expr) - 1):
            if expr[j] == "%":
                expr[j - 1:j + 1] = [int(expr[j - 1]) % int(expr[j + 1])]
                expr.pop(j)
                print(expr)
                break
    # on traite les additions et substraction priorité dans sens de lecture
    for i in range(op_addition + op_substraction):
        for j in range(1, len(expr) - 1):
            if expr[j] == "+":
                expr[j - 1:j + 1] = [int(expr[j - 1]) + int(expr[j + 1])]
                expr.pop(j)
                print(expr)
                break
            if expr[j] == "-":
                expr[j - 1:j + 1] = [int(expr[j - 1]) - int(expr[j + 1])]
                expr.pop(j)
                print(expr)
                break
    return expr

def display_result(array):
    for i in array:
        i = int(i)
        print(i)

## Error handling
error_handling(sys.argv)

## Parsing
arithmetic_expression = sys.argv[1]

## Resolution
nb_parenthesis = count_parenthesis(arithmetic_expression)
our_expression_in_array = array_expression(arithmetic_expression)
print(f"our_expression_in_array {our_expression_in_array}")
first_array_calculate = calculate_parenthesis(our_expression_in_array, nb_parenthesis)
print(f"first array {first_array_calculate}")
resultat = calculations(first_array_calculate)
print(f"resultat {resultat}")

## Display
display_result(resultat)
