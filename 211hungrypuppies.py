from itertools import permutations
import numpy as np
import copy

def hungry_puppies(treats):
    treat_sizes = treats.split(' ')
    treat_sizes = list(map(lambda x: int(x), treat_sizes))

    def happiness(treat_order):
        happy_level = 0

        for i, _ in enumerate(treat_order):
            if i == 0:
                happy_level += np.sign(treat_order[i] - treat_order[i+1])
            elif i == len(treat_order) - 1:
                happy_level += np.sign(treat_order[i] - treat_order[i-1])
            elif treat_order[i] < min(treat_order[i-1], treat_order[i+1]):
                happy_level -= 1
            elif treat_order[i] > max(treat_order[i-1], treat_order[i+1]):
                happy_level += 1
        return happy_level

    # Go through all permutations
    max_happy_level = float("-inf")
    best_order = treat_sizes
    for order in list(permutations(treat_sizes)):
        happy = happiness(order)
        if happy > max_happy_level:
            max_happy_level = happy
            best_order = order

    return best_order, max_happy_level

class treat_machine:
    def __init__(self, treat_options):
        self.treat_options = treat_options.split(' ')
        self.treat_order = []

    def forecast_treat(self, i):
        treat_copy = self.deepcopy()
        treat_copy.treat_order = treat_options.pop(i)
        
        return treat_copy

    def utility(self):
        score = lambda x: 1 if 




if __name__ == "__main__":
    print(hungry_puppies('1 2 2 3 3 3 4'))
    print(hungry_puppies('1 1 2 2 2 2 2 2 3 4 4 4 5 5 5 6 6 6 7 7 8 8 9 9 9 9 9 9 9 9'))
