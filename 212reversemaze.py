import re

def reverse_maze(maze):
    # Split instructions
    input_instructions = maze.split('\n') 
    lines_to_read, maze, path = input_instructions[0], input_instructions[1:-1], input_instructions[-1]
    maze_width, maze_height = len(maze[0]), len(maze)
    maze_grid = [['x' if y != ' ' else ' ' for y in list(row)] for row in maze]

    def traverse_path(starting_point, path, direction = 0):
        orientation = [[1, 0], [0, 1], [-1, 0], [0, -1]] # south, east, north, west
        path = [x for x in re.split('(\d+|\w)',path) if x != '']
        pos = starting_point

        # Go through each instruction and apply the movement
        for instruction in path:
            if re.match('\d+', instruction): # move forward in the direction
                for n in range(int(instruction)):
                    pos[0] += orientation[direction][0]
                    pos[1] += orientation[direction][1]

                    # check if you hit a wall
                    try:
                        if maze_grid[pos[0]][pos[1]] != ' ':
                            return False
                    except IndexError:
                        return False
            elif instruction == 'l': # turn left, go up an index in orientation
                direction = (direction + 1) % 4
            elif instruction == 'r': # turn right, go down an index in orientation
                direction = (direction - 1) % 4

        return pos # return end position

    for i, _ in enumerate(maze_grid):
        for j, _ in enumerate(maze_grid[i]):
            for k in range(4):
                end_point = traverse_path([i,j], path, k)
                if end_point and maze_grid[i][j] == ' ':
                    print('From (%d, %d) to (%d, %d)' % (i, j, end_point[0], end_point[1]))


if __name__ == "__main__":
    maze = '''5
xxx
x x
x x
x x
xxx
2rr2ll2'''
    maze_2 = '''5
xxxxxxx
x   x x
x x x x
x x   x
xxxxxxx
1l2l2'''
    maze_3 = '''5
xxxxxxxxx
x   x   x
x x x x x
x   x   x
xxxxxxxxx
2r2r2'''
    reverse_maze(maze)
    #reverse_maze(maze_2)
    #reverse_maze(maze_3)