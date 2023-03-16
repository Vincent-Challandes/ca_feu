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

def split_parenthesis(expression):
    # on créer un tableau ou l'on split au parenthèse
    array_expression = []
    # result permet de regrouper une chaine de caractère pour ensuite l'ajouter au array_expression
    result = ""
    # permet d'obtenir le début de notre chaine de caractère pour l'ajout au array_expression
    index = 0
    for i in range(len(expression)):
        if expression[i] == "(":
            if i == 0:
                index = 1
            else:
                result = expression[index:i]
                array_expression.append(result)
                index = i + 1
        elif expression[i] == ")":
            result = expression[index:i]
            resultat = calculations(result)
            print(f"resultat inside parenthesis {resultat}")
            array_expression.append(resultat)
            index = i + 1
        elif i == len(expression) - 1:
            result = expression[index:]
            array_expression.append(result)
    return array_expression

def calculations(expression):
    # on sépare les nombres des operateurs
    if type(expression) == str:
        expr = expression.split()
    else:
        expr = expression
    # on parse en integer les nombres
    for i in range(len(expr)):
        if type(expr[i]) == str and expr[i].isdigit():
            expr[i] = int(expr[i])
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
                expr[j - 1:j + 1] = [expr[j - 1] * expr[j + 1]]
                # on pop pour supprimé l'élément J 
                expr.pop(j)
                # ATTENTION pas oublié de break pour ressortir de la boucle remettre le len(expr) à jour sinon IndexOutOfRange et levé
                print(expr)
                break
  
            elif expr[j] == "/":
                expr[j - 1:j + 1] = [expr[j - 1] / expr[j + 1]]
                expr.pop(j)
                print(expr)
                break
    # on traite les modulos
    for i in range(op_modulo):
        for j in range(1, len(expr) - 1):
            if expr[j] == "%":
                expr[j - 1:j + 1] = [expr[j - 1] % expr[j + 1]]
                expr.pop(j)
                print(expr)
                break
    # on traite les additions et substraction priorité dans sens de lecture
    for i in range(op_addition + op_substraction):
        for j in range(1, len(expr) - 1):
            if expr[j] == "+":
                expr[j - 1:j + 1] = [expr[j - 1] + expr[j + 1]]
                expr.pop(j)
                print(expr)
                break
            if expr[j] == "-":
                expr[j - 1:j + 1] = [expr[j - 1] - expr[j + 1]]
                expr.pop(j)
                print(expr)
                break
    return expr

def output_array_in_array(array):
    new_array = []
    for i in range(len(array)):
        if type(array[i]) == str:
            array[i] = array[i].split()
        for j in array[i]:
            new_array.append(j)
    return new_array

def display_result(array):
    for i in array:
        i = int(i)
        print(i)

## Error handling
error_handling(sys.argv)

## Parsing
arithmetic_expression = sys.argv[1]

## Resolution
first_array = split_parenthesis(arithmetic_expression)
print(f"first array {first_array}")
second_array = output_array_in_array(first_array)
print(f"second array {second_array}")
resultat = calculations(second_array)
print(f"resultat {resultat}")

## Display
display_result(resultat)
