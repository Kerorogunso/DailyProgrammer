import random

def addition_chain(numbers):
    terms, limit = map(int,numbers.split(' '))
    chain = [1]
    for i in range(int(terms)):
        next_values = [n + m for n in chain for m in chain if n + m > chain[-1] and (n + m) * 2 ** (terms - len(chain) + 1) >= limit] 
        chain.append(random.choice(next_values))

    # if chain[-1] == int(limit):
    return chain

def back_track():
    chain = [1]
    constraints = {}

    while True:
        possible_values = [n + m for n in chain for m in chain if n + m > chain[-1]]
        if not possible_values:
            chain = chain[:-1]
            constraints[i].append() 
        else: 
            chain.append(random.choice(next_values))

if __name__ == "__main__":
    input_1 = '13 743'
    while True:
        x = addition_chain(input_1)
        if x[-1] == 43:
            print(x)
        else:
            pass