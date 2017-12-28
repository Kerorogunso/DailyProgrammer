from itertools import permutations
import numpy as np
import copy
import random

def hungry_puppies(treats):
    treat_sizes = treats.split(' ')
    treat_sizes = list(map(lambda x: int(x), treat_sizes))

def happiness(treat_order):
    happy_level = 0

    happy_level = [1 if treat_order[i] > max(treat_order[i+1], treat_order[i-1]) 
                   else -1 if treat_order[i] < min(treat_order[i+1], treat_order[i-1])
                   else 0
                   for i in range(1, len(treat_order) - 1)]
    happy_level = sum(happy_level) + np.sign(treat_order[0] - treat_order[1]) + np.sign(treat_order[-1] - treat_order[-2])

    return happy_level

def neighbours(order):
    pos_1 = range(len(order))
    pos_2 = range(len(order))

    def switch(x, y):
        new_order = list(order)
        new_order[x], new_order[y] = new_order[y], new_order[x]
        return new_order

    switched_items = [switch(x, y) for x in pos_1 for y in pos_2 if x != y and switch(x, y) != order]
    return switched_items


# greedy hill climb
def hill_climb(treat_options, steps = int(1e3)):
    current_node = list(map(int,treat_options.split(' ')))
    global_maximum = None
    global_eval = float("-inf")

    for _ in range(steps):
        random.shuffle(current_node)
        # 1eX iterations
        for _ in range(steps):
            # Get the list of potential options
            L = neighbours(current_node)

            # Initialise to be worse case utility
            next_eval = float("-inf")
            next_node = None

            for neighbour_node in L:
                if happiness(neighbour_node) > next_eval:
                    next_node = neighbour_node
                    next_eval = happiness(neighbour_node)

                    if happiness(neighbour_node) > global_eval:
                        global_maximum = neighbour_node
                        global_eval = next_eval
            current_node = next_node

    return global_eval, global_maximum

class treat_machine:
    def __init__(self, treat_options):
        self.treat_options = treat_options.split(' ')
        self.treat_order = []

    def forecast_treat(self, i):
        treat_copy = self.deepcopy()
        treat_copy.treat_order = treat_options.pop(i)
        
        return treat_copy

if __name__ == "__main__":
    print(hill_climb('1 2 2 3 3 3 4'))
    print(hill_climb('1 1 2 3 3 3 3 4 5 5'))
    print(hill_climb('1 1 2 2 3 4 4 5 5 5 6 6'))
    print(hill_climb('1 1 2 2 2 2 2 2 3 4 4 4 5 5 5 6 6 6 7 7 8 8 9 9 9 9 9 9 9 9'))
    # print(hungry_puppies('1 1 2 2 2 2 2 2 3 4 4 4 5 5 5 6 6 6 7 7 8 8 9 9 9 9 9 9 9 9'))
