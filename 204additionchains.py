import sympy
import random
import copy
from collections import defaultdict

def constraint(name, expr):
    if not len(expr.free_symbols):
        return expr
    func = Function(name)(*expr.free_symbols)
    setattr(func, "expr", expr)
    setattr(func, "subs", lambda *a, **b: constraint(name, expr.subs(*a, **b)))
    setattr(func, "_subs", lambda *a, **b: expr.subs(*a, **b))
    return func

def addition_chain(numbers):
    terms, limit = map(int,numbers.split(' '))
    chains = [[1]]
    for i in range(terms):
        chain_copy = [chain + [chain[-1] + n] 
                        for chain in chains
                        for n in chain 
                            if (chain[-1] + n) * 2 ** (terms - len(chain) + 1) >= limit]
        chains = copy.deepcopy(chain_copy)

    correct_chain = [x for x in chains if x[-1] == limit]
    return correct_chain[0]

    x = sympy.symbols('X:%d' % terms + 1)
    constraints = defaultdict(set())

    constraints[x[0]].add(sympy.constraint(sympy.Eq(x[0],1)))
    constraints[x[1]].add(sympy.constraint(sympy.Eq(x[1],2)))
    # Each term when doubled enough must exceed the target
    for i in range(2, terms):
        constraints[x[i]].added(sympy.constraint(x[i] * 2 ** (terms - i) * >= limit))

    # Each term must be the sum of two previous terms
    for i in range(2, terms):
        constraint_list_i = []
        for x in range(i):
            




if __name__ == "__main__":
    # input_1 = '9 95'
    # input_2 = '10 127'
    # print(addition_chain(input_1))
    # print(addition_chain(input_2))

    x = sympy.symbols('X:%d' % 7)
    print(x)