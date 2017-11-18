import time
from msvcrt import getch,kbhit

# Equilibrium position of the door
def stop_door(position, direction):
    while True:
        if kbhit():
            key = ord(getch())
            if direction == 1:
                return open_door(position)
            else:
                return close_door(position)
        else:
            continue

def open_door(position):
    """Takes the position of the door and starts opening"""
    time_left = 10 - position
    start_time = time.time()
    print("Opening door.")

    while (time.time() - start_time) < time_left:
        if kbhit():
            key = ord(getch())
            if key == 13:

                # Button press
                print("Door stopped after %f seconds." % (time.time() - start_time))

            # Stop door and record the position with the next direction
                return stop_door(position + (time.time() - start_time), 0)
            else:
                continue

    # Time has elapsed so that door is fully open
    print("Door opened.")
    return stop_door(10, 0)

def close_door(position):
    """Takes the position of the door and starts closing"""
    time_left = position
    start_time = time.time()
    print("Closing door.")

    while (time.time() - start_time) < time_left:

        # Button press
        
        if kbhit():
            key = ord(getch())
            print("Door stopped after %f seconds." % (time.time() - start_time) )
            # Stop door and record the position with the next direction
            return stop_door(position + (start_time - time.time()), 1)
        else:
            continue

    # Time has elapsed so that door is fully shut
    print("Door closed")
    return stop_door(0,1)

stop_door(0,1)