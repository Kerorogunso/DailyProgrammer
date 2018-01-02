import nltk
from nltk.corpus import words
from copy import deepcopy
import itertools

class SentenceTree:
    def __init__(self, grid):
        self.grid = grid
        self.traversed = [[0,0]]
        self.letter_history = [grid[0][0]]
        self.current_point = [0, 0]

    def apply_move(self, i, j):
        if 0 <= i < len(self.grid) and 0 <= j < len(self.grid[0]):
            new_grid = deepcopy(self)
            new_grid.traversed.append([i, j]) 
            new_grid.current_point = [i, j]
            new_grid.letter_history.append(new_grid.grid[i][j])
            return new_grid   
        else:
            raise IndexError("Move is not valid")

    def next_moves(self):
        directions = [[1,0], [0,-1], [-1,0], [0,1]]
        options = [[self.current_point[0] + d[0], self.current_point[1] + d[1]] for d in directions
            if 0 <= self.current_point[0] + d[0] < len(self.grid)
            and 0 <= self.current_point[1] + d[1] < len(self.grid[0])
            and [self.current_point[0] + d[0], self.current_point[1] + d[1]] not in self.traversed]

        return options

    def detect_english(self,string):
        length = len(string)

        max_words = 0

        for n in range(0, len(string)//3):
            splitting_indices = itertools.combinations(range(len(string)), n)
            for combo in splitting_indices:
                combo = sorted(list(combo))
                words_to_check = [string[combo[i]:combo[i+1]] for i in range(len(combo) - 2)]
                word_count = sum(list(map(lambda x: 1 if x in words.words() else 0, words_to_check)))
                if word_count > max_words:
                    max_words = word_count

        return max_words

    def evaluate(self):
        if not self.next_moves() and traversed != len(self.grid) * len(self.grid[0]):
            return float("-inf") # invalid path
        elif not self.next_moves() and traversed == len(self.grid) * len(self.grid[0]):
            return float(0) # complete valid path
        else:
            return self.detect_english(''.join(self.letter_history)) # count english words in the traversed

def sentence_unpack(sentence):
    instructions, letters = sentence.split('\n')[0].split(' '), [x.split(' ') for x in sentence.split('\n')[1:]]
    lines_to_read = int(instructions[0])
    start_node = [int(instructions[1]) - 1, int(instructions[2]) - 1]

    def max_value(tree):
        return max(tree.next_moves(), key = tree.evaluate)

    tree = SentenceTree(letters)
    while tree.next_moves():
        best_move = max(tree.next_moves(), key = lambda x: tree.apply_move(x[0],x[1]).evaluate())
        tree = tree.apply_move(best_move[0], best_move[1])

    return tree.traversed

def traverse(test):
    paths = [SentenceTree()]
    changing = True
    while changing:
        for path in paths:
            new_paths = []
            for move in path.next_moves():
                new_paths.append([path, move])

        if new_paths == paths:
            changing = False
        else:
            paths = new_paths

    return all_paths_length_36



        
if __name__ == "__main__":
    test = '''6 1 1
T H T L E D
P E N U R G
I G S D I S
Y G A W S I 
W H L Y N T
I T A R G I'''
    sentence_unpack(test)