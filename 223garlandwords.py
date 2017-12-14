def garland(word):
	# A word is garland of order N if the first N characters and the last N characters are the same. 
	# N being the highest order. 0 if the word doesn't start and end the same for all N.
	letter_list = list(word)
	n = len(letter_list)
	for i in range(n-1):
		if letter_list[:(n-1-i)] == letter_list[-(n-1-i):]:
			return word, n-1-i
	
	return word, 0

print(garland('onion'))
print(garland('alfalfa'))
print(garland('ceramic'))