def coconuts(sailors):
	total_coconuts = 0
	completed = False

	while not completed:
		total_coconuts += 1
		successful_division = True
		# Start the coconut pile
		coconut_pile = float(total_coconuts)
		for _ in range(sailors):
			if coconut_pile%sailors == 1. and coconut_pile > sailors:
				# 1 for the monkey
				coconut_pile -= 1.
				# 1/N for the sailor
				coconut_pile *= (sailors - 1.) / sailors
				
			else:
				# Failed to be 1 mod N 
				successful_division = False

		
		if coconut_pile%sailors == 0 and coconut_pile > 0 and successful_division:
			completed = True
		else:
			continue


	return total_coconuts

print(coconuts(4))