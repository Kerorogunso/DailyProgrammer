import random
from termcolor import colored, cprint
import colorama
import os
import numpy

colorama.init()

class minecraft:
    def __init__(self, width, height, depth):
        self.width = width
        self.height = height
        self.depth = depth
        self.blocks = ['A','D','S','L']
        self.grid = [[[numpy.random.choice(self.blocks, p = [0.2, 0.6, 0.2, 0.0]) for _ in range(width)] 
                        for _ in range(height)] 
                        for _ in range(depth)]

    def gravity(self):
        # First layer is the bedrock, iterate going up to the surface

        # Get the closest block above it that isn't an air block
        def block_above(i, j, k):
            for a in range(i + 1, len(self.grid)):
                try:
                    if self.grid[a][j][k] != 'A':
                        return a
                except:
                    pass

        for i, layer_i in enumerate(self.grid):
            for j, row_j in enumerate(self.grid[i]):
                for k, height_k in enumerate(self.grid[i][j]):
                    if self.grid[i][j][k] == 'A':
                        test = block_above(i, j, k)
                        if not test:
                            pass 
                        elif self.grid[test][j][k] == 'S':
                            self.grid[i][j][k] = 'S' # Sink the sand
                            self.grid[test][j][k] = 'A' # Replace the old sand with air
                        elif self.grid[test][j][k] == 'L':
                            self.grid[i][j][k] = 'L' # Flow the lava

class hero:
    def __init__(self, world):
        self.world = world
        self.position = [len(self.world.grid)-1,0,0]

    def move(self):
        lateral_moves = {'w': [-1,0], 'a': [0,-1], 's': [1,0], 'd': [0,1]}
        jump_moves = {'i':[1, -1, 0], 'j': [1, 0, -1], 'k': [1, 1, 0], 'l': [1, 0, 1]}

        direction = input()
        z, x, y = self.position
        ############################################################################        
        # Horiztonal moves
        if direction in ('w','a','s','d'):
            dx = lateral_moves[direction][0]
            dy = lateral_moves[direction][1]

            # Check what the next location is going to be.
            destination_block = self.world.grid[z][x + dx][y + dy]

            # Stopping conditions
            # If the character goes above the top/bottom/left/right boundary or there's a block in the way
            if any([x + dx >= len(self.world.grid[z]) or x + dx < 0,
                    y + dy >= len(self.world.grid[z][x]) or y + dy < 0,
                    destination_block in ('D','S')]):
                print("Can't move.")
            elif destination_block == 'L':
                print("You dead.")
            else:
                self.position[1] += dx
                self.position[2] += dy

        ############################################################################
        # Jumping moves
        elif direction in ('i','j','k','l'):
            dz = jump_moves[direction][0]
            dx = jump_moves[direction][1]
            dy = jump_moves[direction][2]

            if z == len(self.world.grid) - 1 or self.world.grid[z+1][x][y] != 'A':
                print("Can't jump.")
            elif self.world.grid[z + dz][x + dx][y + dy] in ('D','S'):
                print("Can't jump.")
            elif self.world.grid[z + dz][x + dx][y + dy] == 'L':
                print("You dead.")
            else:
                self.position[0] += dz
                self.position[1] += dx
                self.position[2] += dy
        # Invalid moves
        ############################################################################
        # Mining moves
        elif direction in ('mw','ma','ms','md'):
            dx = lateral_moves[direction[-1]][0]
            dy = lateral_moves[direction[-1]][1]
            if self.world.grid[z][x + dx][y + dy] in ('D','S'):
                self.world.grid[z][x + dx][y + dy] = 'A'
                self.world.gravity()
            else:
                print("Can't mine")
        ############################################################################ 
        else:
            pass

        # Check for falling
        holes = True
        while holes:
            new_z, new_x, new_y = self.position
            if new_z == 0:
                holes = False
            elif self.world.grid[new_z-1][new_x][new_y] == 'A':
                    self.position[0] -= 1
            else:
                holes = False


def print_world(grid, hero):
    # Colour the world
    col = lambda x: colored('  ',"white", "on_green") if x == 'D' else colored('  ',"white", "on_red") if x == 'L' else colored('  ',"white", "on_yellow") if x == 'S' else colored('  ', "white")
    
    # Print each row for the layer the hero is in
    for i, row in enumerate(grid):
        coloured_row = list(map(col, row))
        if hero.position[1] == i:
            # Change the hero block
            coloured_row[hero.position[2]] = colored('AA',"white", "on_blue")
        cprint(''.join(coloured_row))

class play_game:
    def __init__(self, depth, height, width):
        self.world = minecraft(depth, height, width)
        self.world.gravity()
        self.hero = hero(self.world)

    def play(self):
        print_world(self.world.grid[self.hero.position[0]], self.hero)
        while True:
            self.hero.move()
            os.system('cls')
            print_world(self.world.grid[self.hero.position[0]], self.hero)
            print(self.hero.position[0])
            
if __name__ == "__main__":
    game = play_game(10,10,5)
    game.play()
    

    