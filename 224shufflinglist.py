import random

def shuffle(my_list):
	# Fisher yates method
	my_list = list(map(str,my_list.split(' ')))
	for i in range(len(my_list)-1):
		r = random.randint(i,len(my_list)-1)
		x = str(my_list[i])
		my_list[i] = str(my_list[r])
		my_list[r] = x

	return ' '.join(my_list)

print(shuffle('1 2 3 4 5 6 7 8'))
print(shuffle('apple blackberry cherry dragonfruit grapefruit kumquat mango nectarine persimmon raspberry raspberry'))



