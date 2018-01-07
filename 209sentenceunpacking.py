from nltk.corpus import words
from copy import deepcopy
import itertools
from collections import defaultdict

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

# Generate all the paths of length max length
def traverse(grid):
    paths = [SentenceTree(grid)]
    
    for i in range(1, len(grid) * len(grid[0]) + 1):
        new_list = [self.traversed]
        for obj in paths:
            for move in obj.next_moves():
                new_obj = deepcopy(obj).apply_move(move[0],move[1])
                new_list.append(new_obj)

        new_list = [x for x in new_list if len(x.traversed) == i + 1]
        paths = deepcopy(new_list)
        print(len(new_list), i, new_list[0].letter_history)

    return [x.letter_history for x in paths]

def sentence_unpack(sentence):
    instructions, letters = sentence.split('\n')[0].split(' '), [x.split(' ') for x in sentence.split('\n')[1:]]
    lines_to_read = int(instructions[0])
    start_node = [int(instructions[1]) - 1, int(instructions[2]) - 1]

    path_list = traverse(letters)
    return path_list

def trie(grid):
    sentence_tree = SentenceTree(grid)
    trie_path = defaultdict(key = lambda : {})
    
    trie_path[sentence_tree.current_point()] = {node for node in sentence_tree.next_moves()}
    


if __name__ == "__main__":
    test = '''6 1 1
T H T L E D
P E N U R G
I G S D I S
Y G A W S I 
W H L Y N T
I T A R G I'''
    print(sentence_unpack(test))