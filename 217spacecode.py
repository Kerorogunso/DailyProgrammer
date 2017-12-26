import re

def space_code(code):

	def hoth_decrypt(code):
		# Add 10 to ascii code
		code_list = code.split()
		decrypted_code = list(map(lambda x: chr(int(x) - 10), code_list)) 
		return ''.join(decrypted_code)

	def ryza_decrypt(code):
		# Subtract 1 from ascii code
		code_list = code.split()
		decrypted_code = list(map(lambda x: chr(int(x) + 1), code_list))
		return ''.join(decrypted_code)

	def htrae_decrypt(code):
		# Reverse the characters
		code_list = code.split()
		decrypted_code = list(map(lambda x: chr(int(x)), code_list))[::-1]
		return ''.join(decrypted_code)

	def omnicron_decrypt(code):
		# Invert the 5th bit
		code = code.split()
		bin_int = lambda x : bin(int(x)) # split the binary representation
		invert = lambda y : [x if i != len(y) - 5 else str((int(x) + 1) % 2) for i, x in enumerate(y)] # invert the 5th bit   
		to_int = lambda z : chr(int(''.join(z),2)) # convert the list back to a string
		invert_fifth = lambda w: to_int(invert(bin_int(w)))

		decrypted_code = list(map(invert_fifth, code))
		return ''.join(decrypted_code)

	reg_string = r'(\w+ ){2,}'
	decryption_methods = {'Hoth': hoth_decrypt, 
						  'Ryza': ryza_decrypt, 
						  'Htrae': htrae_decrypt, 
						  'Omnicron': omnicron_decrypt}

	for method in decryption_methods:
		test = re.match(reg_string, decryption_methods[method](code))
		if test is not None:
			return method, decryption_methods[method](code)

if __name__ == "__main__":

	code = " 101 99 97 101 112 32 110 105 32 101 109 111 99 32 101 87 "
	print(space_code(code))

	test_code = [" 71 117  48 115 127 125 117  48 121 126  48  96 117 113 115 117 ",
				" 97 111  42 109 121 119 111  42 115 120  42 122 111 107 109 111 ",
				" 86 100  31  98 110 108 100  31 104 109  31 111 100  96  98 100 ",
				" 101  99  97 101 112  32 110 105  32 101 109 111  99  32 101  87 ",
				" 84 113 121 124 105  48  64  98 127 119  98 113 125 125 117  98  48 121  99  48  99  96 105 121 126 119  48 127 126  48 101  99 ",
				" 78 107 115 118 131  42  90 124 121 113 124 107 119 119 111 124  42 115 125  42 125 122 131 115 120 113  42 121 120  42 127 125 ",
				" 67  96 104 107 120  31  79 113 110 102 113  96 108 108 100 113  31 104 114  31 114 111 120 104 109 102  31 110 109  31 116 114 ",
				" 115 117  32 110 111  32 103 110 105 121 112 115  32 115 105  32 114 101 109 109  97 114 103 111 114  80  32 121 108 105  97  68 ",
				" 86 121  98 117  48 100 120 117  48  93 121  99  99 124 117  99 ",
				" 80 115 124 111  42 126 114 111  42  87 115 125 125 118 111 125 ",
				" 69 104 113 100  31 115 103 100  31  76 104 114 114 107 100 114 ",
				" 115 101 108 115 115 105  77  32 101 104 116  32 101 114 105  70 "]
	for c in test_code:
		print(space_code(c))