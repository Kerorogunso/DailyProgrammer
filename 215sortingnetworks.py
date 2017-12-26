''' Sorting networks are a way of sorting numbers, where the numbers travel down a wire
and eventually hit a changing point between two lines called a comparator. The comparator
moves the lower number up the line and sends the larger one to the bottom. With enough 
comparators placed effectively, you can sort a list correctly. Think of it like the treasure
pipes mini game for mario party''' 

def validate_sorting_network(network):

    # Partition the input into wire #, comparator # and the list of comparators
    split_input = [list(map(int, x.split(' '))) for x in network.split('\n')]
    wires = split_input[0][0]
    number_of_comparators = split_input[0][1]
    comparator_list = split_input[1:]

    # Start with the list of length 0 and 1 and then generate all larger permutations using a loop
    items_to_switch = ['0','1']
    while len(items_to_switch) < 2 ** int(wires):
        # Keep multiplying out the set
        items_to_switch = [x + s for x in items_to_switch for s in ['0','1']]

    # Convert the lists into integers
    lists_to_sort = [list(map(int, list(x))) for x in items_to_switch]

    # Try to sort one list using an input
    def attempt_sort(my_list):
        for c in comparator_list:
            if my_list[c[0]] > my_list[c[1]]:
                my_list[c[0]], my_list[c[1]] = my_list[c[1]], my_list[c[0]]

        if my_list == sorted(my_list):
            return True
        else:
            return False

    # Check if all permutations are sorted correctly
    return all(list(map(attempt_sort, lists_to_sort)))



if __name__ == "__main__":
    network_1 = '''4 5
0 2
1 3
0 1
2 3
1 2'''
    network_2 = '''8 19
0 2
1 3
0 1
2 3
1 2
4 6
5 7
4 5
6 7
5 6
0 4
1 5
2 6
3 7
2 4
3 5
1 2
3 4
6 7'''
    network_3 = '''16 60
0 1
2 3
4 5
6 7
8 9
10 11
12 13
14 15
0 2
1 3
4 6
5 7
8 10
9 11
12 14
13 15
0 4
1 5
2 6
3 7
8 12
9 13
10 14
11 15
0 8
1 9
2 10
3 11
4 12
5 13
6 14
7 15
5 10
6 9
3 12
7 11
13 14
1 2
4 8
1 4
7 13
2 8
11 14
2 4
5 6
9 10
11 13
3 8
7 12
6 8
3 5
7 9
10 12
3 4
5 6
7 8
9 10
11 12
6 7
8 9'''
    print(validate_sorting_network(network_1))
    print(validate_sorting_network(network_2))
    print(validate_sorting_network(network_3))
