# Create a blank grid of zeros that will be layered over with rectangles of numbers, the number representing the color of the rectangle
# Receiving inputs for rectangles, produce the resulting image as a result of laying them one on top of another
from collections import Counter
import itertools

def pile_of_paper(canvas_string):
    instructions = test_input.split('\n')
    grid_dim = [int(x) for x in instructions[0].split(' ')]
    rectangles = [list(map(int,x.split(' '))) for x in instructions[1:]]

    empty_grid = [[0 for _ in range(grid_dim[1])] for _ in range(grid_dim[0])]

    for rect in rectangles:
        for i in range(rect[3]):
            for j in range(rect[4]):
                empty_grid[rect[1] + i][rect[2] + j] = rect[0]

    chain = Counter(itertools.chain(*empty_grid))
    for k, v in chain.items():
        print(k, v)

if __name__ == "__main__":
    test_input = '''20 10
1 5 5 10 3
2 0 0 7 7'''
    print(pile_of_paper(test_input))