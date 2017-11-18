# Draws a rectangle given RGB values and width, height
def paint_rectangle(rect_line):
    global paint_grid
    red, green, blue, x_0, y_0, width, height = [int(x) for x in rect_line.split(' ')]

    for i in range(height):
        for j in range(width):
            paint_grid[x_0 + i][y_0 + j] = [red, green, blue]

# Paint a point given RGB values and position
def paint_grid(point_line):
    global paint_grid
    red, green, blue, x_0, y_0 = [int(x) for x in point_line.split(' ')]
    paint_grid[x_0][y_0] = [red, green, blue]

# Paint a line given RGB values, position and destination
def paint_line(line_line):
    global paint_grid
    red, green, blue, x_0, y_0, x_1, y_1 = [int(x) for x in line_line.split(' ')]

    gradient = ((y_1 - y_0) / (x_1 - x_0)) if x_1 != x_0 else float("inf")

    # Gradient at least 1, move dy up for every 1 right
    if gradient >= 1:
        dx = 1
        dy = int(gradient)
    # Gradient is zero do not move in the y direction
    elif gradient == 0:
        dy = 0
        dx = 1

    # Gradient less than 1, move 1 up for every dx right
    else:
        dx = int(1 / gradient)
        dy = 1

    i, j = x_0, y_0
    paint_grid[i][j] = [red, green, blue]
    while i <= x_1 and j <= y_1:
        for _ in range(dy):
            j += 1
            if j > y_1:
                break
            else:
                paint_grid[i][j] = [red,green,blue] 
        for _ in range(dx):
            i += 1
            if i > x_1:
                break
            else:
                paint_grid[i][j] = [red,green,blue]

    for x in paint_grid:
        print(x)        

def paint_my_bitmap(bitmap_string):
    # Takes a Netpbm string and generates the bitmap image associated to it
    grid_width = 300
    grid_height = 400
    # Initialise empty grid
    paint_grid = [[[0,0,0] for _ in range(grid_height)] for _ in range(grid_width)]

grid_width = 20
grid_height = 10    
paint_grid = [[[0,0,0] for _ in range(grid_height)] for _ in range(grid_width)]
paint_grid = print(paint_line('1 2 3 0 0 2 4'))
