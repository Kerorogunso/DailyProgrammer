def xmas_lights(volt_drop, current, battery_voltage, battery_capacity, time):
    '''returns the maximum number of 9V 20mA lightbulbs that can
    be powered by a 1200mA battery'''

    serial_length = int(battery_voltage / volt_drop)
    rows = battery_capacity / (current * time)
    resistance = (battery_voltage - int(battery_voltage / volt_drop) * volt_drop) * rows * 1000 / battery_capacity

    print('Resistor: %f Ohms' % resistance)
    print('Scheme')
    print('*--' + '|>|---' * (serial_length - 1) + '|>|--*') 
    for _ in range(serial_length-1):
        print('|' + ' ' * (6 * (serial_length-1) + 2) + '|') 
        print('--' + '|>|---' * (serial_length-1) + '|>|--')

print(xmas_lights(1.7,20,9,1200,20))