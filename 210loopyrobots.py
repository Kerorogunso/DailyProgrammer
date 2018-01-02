def loopy_robots(commands):
    commands_list = list(commands)
    directions = [[0,1], [1,0], [0,-1], [-1,0]] # north, east, south, west

    rob_x = 0
    rob_y = 0
    orientation = 0 

    def run_commands(x, y, orientation, commands):
        for command in commands_list:
            if command == 'S':
                x += directions[orientation][0]
                y += directions[orientation][1]
            elif command == 'L':
                orientation = (orientation - 1) % 4
            elif command == 'R':
                orientation = (orientation + 1) % 4
            else:
                raise Exception("Does not compute")

        return x, y, orientation

    l = 0
    run = True
    while run and l < 1000000:
        rob_x, rob_y, orientation = run_commands(rob_x, rob_y, orientation, commands_list)
        l += 1
        if [rob_x, rob_y, orientation] == [0, 0, 0]:
            run = False

    print(l, 'Loop found!' if not run else 'No loop found.')


if __name__ == "__main__":
    loopy_robots('SRLLRLRLSSS')
    loopy_robots('SRLLRLRLSSSSSSRRRLRLR')
    loopy_robots('SRLLRLRLSSSSSSRRRLRLRSSLSLSLSRS')
    loopy_robots('LSRS')