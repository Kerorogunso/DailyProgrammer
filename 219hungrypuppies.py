from itertools import permutations

def hungry_puppies(treats):
    treat_sizes = treats.split(' ')

    def happiness(treat_order):
        happy_level = 0
        for i, _ in enumerate(treat_order):
            if treat_order[i] > max(treat_order[i-1], treat_order[i+1]):
                happy_level += 1
            elif treat_order[i] < min(treat_order[i-1], treat_order[i+1]):
                happy_level -= 1

        return happy_level

    # Go through all permutations
    max_happy_level = float("-inf")
    for order in list(permutations(treat_sizes)):
        happy = happiness(order)



if __name__ == "__main__":
