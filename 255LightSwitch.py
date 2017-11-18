def switch(light, x, y):
    """takes a range of lights and runs one iteration of the light switching"""
    for i in range(min(x,y), max(x,y)):
        light[i] = (light[i] + 1) % 2

    return light

def switch_result(N, runs):
    """takes a number of lights and a series of runs,
    generating the resulting light configuration"""

    the_lights = [0] * N
    
    # Parse input into easier format to iterate through
    light_switch_input = [map(int,x.split(' ')) for x in runs.split('\n')]

    for x in light_switch_input:
        the_lights = switch(the_lights,x[0],x[1])

    return the_lights
        

the_runs = """616 293
344 942
27 524
716 291
860 284
74 928
970 594
832 772
343 301
194 882
948 912
533 654
242 792
408 34
162 249
852 693
526 365
869 303
7 992
200 487
961 885
678 828
441 152
394 453"""

with open('lots_of_switches.txt','r') as f:
    N = int(f.readline())
    lights = [0] * N
    for line in f:
        lights = switch(lights, int(line.split(' ')[0]), int(line.split(' ')[1]))

    print lights
print(switch_result(1000,the_runs))