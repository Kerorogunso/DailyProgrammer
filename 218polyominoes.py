import numpy as np

# Generate all possible strings n-imos. E.g. tetrimos are tetris blocks
# all possible joined combinations of 4 blocks 
def polyominoes(n):
	my_grid = np.zeros([n,n])
	my_grid[0][0] = 1

	# Identify the number of filled points given a grid
	def neighbouring_points(grid):
		# Determine what points are filled already in the grid
		filled_points = [(i,j) for i, _ in enumerate(grid) for j, _ in enumerate(grid) if grid[i][j] == 1]
		
		neighbours = set()

		# Iterate through filled points in the grid
		for x in filled_points:
			# List out their neighbours
			candidates = [(min(x[0]+1,len(grid)), x[1]), (max(x[0]-1,0),x[1]), (x[0],min(x[1]+1,len(grid))), (x[0], max((x[1]-1),0))]
			# Include the neighbour if its not filled yet otherwise pick nothing
			valid_points = set(map(lambda k: k if grid[k[0]][k[1]] == 0 else None, candidates))
			# Add to the list of possible neighbours
			neighbours.union(valid_points).difference({None})

		return neighbours # provide list of all neighbouring blank spots

	# Keep picking a point until you have enough for a polynomino	
	def pick_point(grid):
		options = neighbouring_points(grid) # Identify what neighbours there are

		if reduce(lambda x, y: x + y, grid) == n: # All points filled
			print(grid)
		else:
			for x in options: # Go through each option
				grid_copy = grid.copy()
				grid_copy[x[0]][x[1]] = 1 # Try it
				pick_point(grid_copy) # Run next iteration
			# Finished enumerating

	pick_point(my_grid)					   

if __name__ == "__main__":
	print(polyominoes(4))
