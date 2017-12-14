def balance_word(word):
	'''the position and letter itself to calculate the weight around the balance point. A word can be balanced if the weight on either side of the balance point is equal. Not all words can be balanced, but those that can are interesting for this challenge.
	The formula to calculate the weight of the word is to look at the letter position in the English alphabet (so A=1, B=2, C=3 ... Z=26) as the letter weight, then multiply that by the distance from the balance point, so the first letter away is multiplied by 1, the second away by 2, etc. 
	As an example: STEAD balances at T: 1 * S(19) = 1 * E(5) + 2 * A(1) + 3 * D(4))'''

	letter_list = list(word)
	letter_weights = list(map(lambda x: ord(x) - 64, letter_list)) # calculate the alphabetical position of the letter based on lowercase ordinal
	
	for i, letter in enumerate(letter_list):
		position_weights = list(map(lambda x: x - i, range(len(letter_list))))
		total_weights = [x*y for (x,y) in zip(letter_weights,position_weights)]
		if sum(total_weights) == 0:
			return ('%s %s %s - %d') % (''.join(letter_list[:i]), word[i] ,''.join(word[i+1:]), abs(sum(total_weights[:i])))

	return word, 'does not balance.'

print(balance_word('STEAD'))
print(balance_word('CONSUBSTANTIATION'))
print(balance_word('UNINTELLIGIBILITY'))