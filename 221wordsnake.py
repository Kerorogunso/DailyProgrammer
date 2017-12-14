import numpy as np
def word_snake(words):
	# Create a snake of words based on the first and last letters, turning 90 degrees
	max_length = len(words) # Maximum grid length
	word_list = words.split(' ')

	x, y = 0, 0 # grid index
	d = [1, 0] # direction index
	for n, word in enumerate(word_list):
		word_list[n] = word[1:] if n != 0 else word
	grid = np.empty(shape=(max_length, max_length),dtype=str)
	for word in word_list:
		for k, char in enumerate(list(word)):
			word_length = len(word) # for change of direction
			x += d[0]
			y += d[1]
			grid[x][y] = char

			if k == word_length-1:
				# change direction
				d = [(d[0]+1)%2, (d[1]+1)%2] 
	
	# Fill empty cells with spaces
	grid[grid==''] = ' '
	for row in grid:
		print(' '.join(row))

test_word_list = 'SHENANIGANS SALTY YOUNGSTER ROUND DOUBLET TERABYTE ESSENCE'
word_snake(test_word_list)



