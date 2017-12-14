from itertools import chain
import copy

go_board = '''bbbbb
 wwwb
bwbwb
 bbbb'''

go_board_2 = ''' bbbbb 
bbwwwwb
bww wb 
 bwwwwb
  bbbbb'''

# Goban routine to count points and clear stones with no liberties
class goban:
    def __init__(self,go_string = '\n'.join( [9 * ' '] * 9)):
        self.board = [[point for point in row] for row in go_string.split('\n')]

    # Checks the stone placed on the grid
    def stone_color(self, i, j):
        # Try statement in case of out of range
        try:
            return self.board[i][j]
        except:
            return None

    # Nicer printing method
    def print_board(self):
        
        stones = {'b': u'\u25CB', 'w': u'\u25CF'}
        empty = {'top left': u'\u250F', 
                 'top right': u'\u2513', 
                 'bottom left': u'\u2517', 
                 'bottom right': u'\u251B',
                 'left': u'\u2523', 
                 'right': u'\u252B',
                 'top': u'\u2533',
                 'bottom': u'\u253B',
                 'middle': u'\u254B'}

        print_board = copy.deepcopy(self.board)
        for i, _ in enumerate(print_board):
            for j, _ in enumerate(print_board[i]):
                
                # Top row
                if i == 0:
                    if j == 0:
                        go_character = 'top left'
                    elif j == len(print_board[i]) - 1:
                        go_character = 'top right'
                    else:
                        go_character = 'top'

                # First column
                elif j == 0:
                    if i == len(print_board) - 1:
                        go_character = 'bottom left'
                    else:
                        go_character = 'left'

                # Last column
                elif j == len(print_board[i]) - 1:
                    if i == len(print_board) - 1:
                        go_character = 'bottom right'
                    else:
                        go_character = 'right'

                # Last row
                elif i == len(print_board) - 1:
                    go_character = 'bottom'

                # Centre character
                else:
                    go_character = 'middle'

                # Stone
                if print_board[i][j] in ('b','w'):
                    print_board[i][j] = stones[print_board[i][j]] 
                else:
                    print_board[i][j] = empty[go_character]

        # Print letter labels on the top row first with a space before            
        print(' ', ' '.join([chr(65 + x) for x in range(len(print_board))]))

        for i, row in enumerate(print_board):
                print(i + 1, str(u'\u2501').join(row))
                
    # Establish the direct neighbours of a given point. Looking up, down, left and right
    def neighbours(self, i,j):
        potential_neighbours = [(i+1,j), (i-1,j), (i, j+1), (i, j-1)]
        neighbours = []

        for point in potential_neighbours:
            if self.stone_color(point[0],point[1]) == self.stone_color(i,j) and self.stone_color(point[0],point[1]) in ('b','w'):
                neighbours.append(point)

        return neighbours

    # Generator to pull values if unique 
    def unhashable_duplicate_remove(self, the_list):
        the_list = sorted(lambda x: x[0], )
        last = object()
        for item in the_list:
            if item == last:
                continue
            yield item
            last = item

    # Use the neighbour function to establish the group by repeating over all the points until it stops growing
    def group(self,i,j):
        my_group = [(i,j)]
        
        search_incomplete = True

        while search_incomplete:
            current_length = len(my_group)
            group_neighbours = [[x for x in self.neighbours(y[0],y[1])] for y in my_group] # List comprehension to get the neighbours
            group_neighbours = copy.deepcopy(chain.from_iterable(group_neighbours)) # flatten down into one list
            my_group += group_neighbours # append neighbours to group
            my_group = list(set(my_group))
            # my_group = list(self.unhashable_duplicate_remove(my_group))
            new_length = len(my_group)
            if current_length == new_length:
                search_incomplete = False

        return my_group

    # Determines the number of liberties of a group
    def liberties(self, group):
        empty_positions = set([]) 
        # Go through each stone in the group
        for x in group:
            neighbours_x = set([(x[0]+1,x[1]), (x[0]-1,x[1]), (x[0], x[1]+1), (x[0], x[1]-1)])
            empty_neighbours = set([y for y in neighbours_x if all([0 <= y[0] < len(self.board), # Within the grid
                                                               0 <= y[1] < len(self.board[0]), # Within the grid
                                                               self.stone_color(y[0],y[1]) == ' '])]) # Empty

            empty_positions = set(empty_positions.union(empty_neighbours))

        return len(empty_positions)

    # Places a stone on the board
    def play(self,i,j, color):
        if self.board[i][j] == ' ': 
            self.board[i][j] = color

            adjacent_stones = [(i+1,j), (i-1, j), (i, j+1), (i, j-1)]
            for y in adjacent_stones:
                # If neighbour stone is white and these no longer have liberties
                if self.stone_color(y[0],y[1]) and self.stone_color(y[0],y[1]) != color and self.liberties(self.group(y[0],y[1])) == 0:
                    for stone in self.group(y[0],y[1]):
                        self.board[stone[0]][stone[1]] = ' '

            # If the stone has no liberties after attempt to capture, remove and print invalid
            if self.liberties(self.group(i,j)) == 0:
                self.board[i][j] = ' '
                print("Invalid Move!")
                return False # Invalid move
            else:
                return True # Valid

        else:
            print("Invalid Move!")
            return False # Invalid move





if __name__ == "__main__":

    # my_goban = goban(go_board) # Create board
    # print('my board: ',my_goban.print_board) # Print the board in a nice format
    # print('2,3 stone color:',my_goban.stone_color(2,3)) # What is the stone color of (2,3)
    # print(my_goban.group(2,1))
    # print(my_goban)
    # print(my_goban.liberties(my_goban.group(2,0)))
    
    the_board = goban()
    the_board.print_board
    t = 0

    while True:
        turn = ['Black', 'White']
        move = input("%s's Turn: " % turn[t%2])
        

        try:
            # Check if the user wishes to pass turn.
            if move.lower() == "pass":
                t += 1
            # Check if the user wants to resign.
            elif move.lower() == "resign":
                resign_check = input("Are you sure? (y/n):")
                if resign_check == 'y':
                    print("%s resigns after %d turns." % (turn[t%2], t))
                    break

            # Attempt move.
            else:
                move = tuple(list(move))
                # Check if valid move
                if the_board.play(int(move[0])-1, ord(move[1].upper())-65, turn[t%2][0].lower()):
                    t += 1  # Switch turn
                    the_board.print_board() # Print board

        except:
            print("Sorry I don't understand")
            continue
            



