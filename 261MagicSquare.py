import math
def magic_square(square):
    """Checks if a magic square is valid"""
    d = int(math.sqrt(len(square))) # Square dimension
    square_total = sum(square[i] for i in range(d)) # column/row total to achieve

    one_number_each = False not in [square.count(i) == 1 for i in range(1,d ** 2 + 1)]
    rows = False not in [sum(square[d * j + i] for i in range(d)) == square_total for j in range(d)]
    columns = False not in [sum(square[j + d * i] for i in range(d)) == square_total for j in range(d)]
    diagonals = sum(square[i * (d + 1)] for i in range(d)) == square_total and sum(square[(d - 1) * (j + 1)] for j in range(d)) == square_total

    return one_number_each and rows and columns and diagonals

print magic_square([8, 1, 6, 3, 5, 7, 4, 9, 2])
print magic_square([2, 7, 6, 9, 5, 1, 4, 3, 8])
print magic_square([3, 5, 7, 8, 1, 6, 4, 9, 2])
print magic_square([8, 1, 6, 7, 5, 3, 4, 9, 2])
