from functools import reduce
import re

class Stack:
    def __init__(self):
        self.list = []

    def push(self, x):
        self.list.append(x)

    def pop(self):
        return self.list.pop(-1)

def recurrence_relation(relation):
    instructions = relation.split('\n')
    operators = instructions[0].split(' ')
    x_0 = float(instructions[1])
    n = int(instructions[2])

    def function_generator(instruction):
        if instruction[0] == '*':
            return lambda x: float(x) * float(instruction[1:])
        elif instruction[0] == '+':
            return lambda x: float(x) + float(instruction[1:])
        elif instruction[0] == '-':
            return lambda x: float(x) - float(instruction[1:])
        elif instruction[0] == '/':
            return lambda x: float(x) / float(instruction[1:])
        else:
            raise Exception("Not a valid operator")

    def compose(a,b):
        return lambda x: b(a(x))

    operations = list(map(function_generator, operators))
    composition = reduce(compose, operations)

    for i in range(n+1):
        print("Term %d: " % i, str(x_0))
        x_0 = composition(x_0)


def polish_notation(rpn):
    instructions = rpn.split('\n')
    reverse_pole = instructions[0].split(' ')
    max_n = int(instructions[-1])
    operators = ['+', '-', '*', '/']

    starting_terms = [x.split(':') for x in instructions[1:-1]]
    starting_terms = {int(x[0]): int(x[1]) for x in starting_terms}

    def binary_operation(a, operator, b):
        if operator == '+':
            return a + b
        elif operator == '-':
            return a - b
        elif operator == '*':
            return a * b
        else:
            return a / b    

    def rpn_function(reverse_pole, n):
        myStack = Stack()
        if n in starting_terms.keys():
            return starting_terms[n]

        for token in reverse_pole:
            if token in operators:
                operand_2 = myStack.pop()
                operand_1 = myStack.pop()
                result = binary_operation(int(operand_1), token, int(operand_2))
                myStack.push(result)
            elif re.match(r'\(\d+\)', token):
                i = re.search('\(([^)]+)', token).group(1)
                try:
                    myStack.push(starting_terms[n - int(i)])
                # No valid terms
                except:
                    return '?'
            else:
                myStack.push(token)

        result = myStack.pop()
        starting_terms[n] = result
        return result
    
    for i in range(max_n+1):
        term = rpn_function(reverse_pole, i)
        if term != '?':
            print("Term %d:" % i , term)


if __name__ == "__main__":
    input_4 = '''0 (1) 2 * 1 + -
5:31
14'''
    # polish_notation(input_4)

    input_5 = '''(2) (4) (6) + +
0:0
2:0
4:1
30'''
    polish_notation(input_5)
