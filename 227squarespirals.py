def squarespirals(S, N=None, X=None, Y=None):
	directions = {0:'East',1:'North',2:'West',3:'South'}

	# Initialise empty grid
	grid = [['' for _ in range(S)] for _ in range(S)]
	counter = 1
	x, y = S//2, S//2
	grid[x][y] = counter
	dir_index = 0
	
	dir_map = [[0,1], [-1,0], [0,-1],[1,0]]

	while '' in [item for sublist in grid for item in sublist]:
		counter += 1

		if counter != 2 and grid[x+dir_map[(dir_index+1)%4][0]][y + dir_map[(dir_index+1)%4][1]] == '':
			dir_index = (dir_index + 1) % 4
		
		x += dir_map[dir_index][0]
		y += dir_map[dir_index][1]
		grid[x][y] = counter
		if counter == N:
			return x+1, y+1

	return grid[X-1][Y-1]

print(squarespirals(S=3,N=8))
print(squarespirals(S=7,X=1,Y=1))
