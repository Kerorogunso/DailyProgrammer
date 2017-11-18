import math

def clarence_distance(ip_address):
    coordinate_dict = { '.' : [0, 0],
                        '1' : [0, 3],
                        '2' : [1, 3],
                        '3' : [2, 3],
                        '4' : [0, 2],
                        '5' : [1, 2],
                        '6' : [2, 2],
                        '7' : [0, 1],
                        '8' : [1, 1],
                        '9' : [2, 1],
                        '0' : [1, 0]} 

    def pythagoras(x, y):
        return math.sqrt((y[0] - x[0]) ** 2 + (y[1] - x[1]) ** 2)
        
    numbers = [str(c) for c in ip_address]

    return sum(pythagoras(coordinate_dict[numbers[i]], coordinate_dict[numbers[i+1]]) for i in range(len(numbers) - 1))

print clarence_distance('219.45.143.143')