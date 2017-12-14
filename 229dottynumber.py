import numpy as np
import math

# Find the fixed point of the equation
def dotty_number(f = lambda x : math.cos(x), starting = 0.5,tolerance=1e-4):
	dotty = f(starting)

	while abs(dotty - f(dotty)) > tolerance:
		dotty = f(dotty)

	return dotty

print(dotty_number(f = lambda x: x - math.tan(x),starting=2)) 
print(dotty_number(f = lambda x: 1 + 1.0/x,starting=0.5)) 
print(dotty_number(f = lambda x: 4 * x * (1-x),starting=2)) 

