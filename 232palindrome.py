def palindrome(words):
	x = list(words.lower())
	x = [y for y in x if y.isalnum()]

	return 'Palindrome' if (x[::-1] == x) else 'Not Palindrome'


print(palindrome('Was it a car or a cat i saw?'))
print(palindrome('A man, a plan, a canal, a hedgehog, a podiatrist, Panama!'))
print(palindrome('Are we not drawn onward, we few, drawn onward to new area?'))