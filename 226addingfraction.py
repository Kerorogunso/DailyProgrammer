from functools import reduce
import numpy as np

def add_fraction(*args):

    fractions = [arg.split('/') for arg in args]
    denominators = [int(arg[1]) for arg in fractions]
    numerators = [int(arg[0]) for arg in fractions]
    D = reduce((lambda x, y: x * y),denominators)
    # Multiply numerators by the product of every other denominator
    multipliers = list(map((lambda x: D / x), denominators))
    N = sum(np.array(numerators) * np.array(multipliers))
    
    # Euclid's algorithm
    def euclid(a,b):
        a,b = a if a > b else b, b if a > b else a # change the numbers around to be the largest
        while a%b != 0:
            c = int(b)
            b = a%b
            a = c

        return b
    hcf = euclid(N,D)

    # Reduce the fraction
    return '%d/%d' % (N/hcf, D/hcf)

print(add_fraction('1/6','3/10','4/13'))

