# Implement rule 90 
def cellular_automata(series):
    series = list(series)
    for _ in range(25):
        print(''.join(['x' if x == '1' else ' ' for x in series]))
        series = ['1' if i < len(series) - 1 and bool(int(series[i-1])) ^ bool(int(series[i+1])) == 1 else '0' for i in range(len(series))]

if __name__ == "__main__":
    # sierpinskis gasket
    cellular_automata('00000000000000000000000000000000000000000000000001000000000000000000000000000000000000000000000000')


