import math

def ascii_gradient(instructions):
    instructions = instructions.split('\n')
    grid_size = instructions[0].split(' ')
    colours = instructions[1]
    gradient_parameters = instructions[2].split(' ')

    grid = [['.' for _ in range(int(grid_size[0]))] for _ in range(int(grid_size[1]))]

    if gradient_parameters[0] == "radial":
        x_0, y_0 = int(gradient_parameters[1]), int(gradient_parameters[2])
        radius = int(gradient_parameters[3])
        
        gradient_threshold = radius / len(colours)


        for j, _ in enumerate(grid):
            for i, _ in enumerate(grid[j]):
                try:
                    grid[j][i] = colours[int(math.sqrt((j - y_0)**2  + (i - x_0)**2) / gradient_threshold)]
                except IndexError:
                    grid[j][i] == '.'
   
    else:
        x_0, y_0 = int(gradient_parameters[1]), int(gradient_parameters[2])
        x_1, y_1 = int(gradient_parameters[3]), int(gradient_parameters[4])

        for j, _ in enumerate(grid):
            for i, _ in enumerate(grid[j]):
                try:
                    grid[j][i] = colours[min(int(((j - y_0) + (i - x_0)) / ((abs(x_0 - x_1) + abs(y_0 - y_1)) / (len(colours)))),0)]
                except IndexError:
                    grid[j][i] == '.'

    for row in grid:
            print(''.join(row))


if __name__ == "__main__":
    input_1 = '''40 30
 .,:;xX&@
radial 20 15 20'''
    ascii_gradient(input_1)

    input_2 = '''40 40
aaabcccdeeefggg
radial -10 20 60'''
    ascii_gradient(input_2)

    input_3 = '''60 30
 '"^+$
linear 30 30 0 0'''
    ascii_gradient(input_3)
