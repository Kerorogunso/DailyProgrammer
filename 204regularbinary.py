from itertools import permutations, combinations, product

def hyperbinary(number):
    valid_representations = []
    bin_number = bin(number)
    max_chars = len(bin_number) - 2

    all_rep = [list(map(int, list(x))) for x in product('012', repeat = max_chars)]
    for representation in all_rep:
        evaluate = sum([2**(max_chars - i - 1) * x for i, x in enumerate(representation)])
        if evaluate == number:
            valid_representations.append(int(''.join([str(x) for x in representation])))

    return valid_representations

if __name__ == "__main__":
    input_1 = 18
    print(hyperbinary(input_1))
    input_2 = 239  
    print(hyperbinary(input_2))
    input_3 = 128
    print(hyperbinary(input_3))