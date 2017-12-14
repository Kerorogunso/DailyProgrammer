# Takes a sentence and scrambles the word alphabetically by letter. Punctuation and capitalization stays.

# Bespoke bubble sort required to deal with the punctuation and capitals
def bubble_sort(the_array):
	n = len(the_array)
	thing_to_sort = list(the_array)
	while n > 0:
		for i in range(n-1):
			if all([ord(thing_to_sort[i].lower()) > ord(thing_to_sort[i+1].lower()), thing_to_sort[i].isalpha(), thing_to_sort[i+1].isalpha()]):
				thing_to_sort[i], thing_to_sort[i+1] = thing_to_sort[i+1], thing_to_sort[i]
		n -= 1
	return thing_to_sort

def word_mangler(words):
	word_list = words.split(' ')
	letter_array = [list(word) for word in word_list]
	sorted_letters = [bubble_sort(list(word)) for word in letter_array]
	case_sorted_letters = [[c.upper() if letter_array[j][i].isupper() else c.lower() for i, c in enumerate(word)] for j, word in enumerate(sorted_letters)]
	sorted_words = [''.join(word) for word in case_sorted_letters]

	return ' '.join(sorted_words)


print(word_mangler('This challenge doesn\'t seem so hard.'))



