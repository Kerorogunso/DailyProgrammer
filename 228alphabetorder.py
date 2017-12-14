# Takes a word and determines if it is in alphabetical order
def alphabet_order(words):
	for word in words.split("\n"):
		if list(word) == sorted(list(word)):
			x = " IN ORDER"
		elif list(word) == sorted(list(word),reverse=True):
			x = " REVERSE ORDER"
		else:
			x = " NOT IN ORDER"
		print(word, x)

word_check = '''billowy
biopsy
chinos
defaced
chintz
sponged
bijoux
abhors
fiddle
begins
chimps
wronged'''

alphabet_order(word_check)
