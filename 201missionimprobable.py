from itertools import combinations

def calculate_probability(events):
    inputs = events.split('\n')
    instructions = inputs[0].split(' ')
    variables = instructions[1:]
    event_variables = variables + ['!' + x for x in variables]

    def mutex(events, var):
        events = [x.replace('!','') for x in events]
        var = var.replace('!', '')
        return var in events

    class probability_tree:
        def __init__(self, variables=[]):
            self.variables = variables
            self.probability = None
            if len(self.variables) == 2:
                self.children = None
            else:
                self.children = [probability_tree(self.variables+ [var]) for var in event_variables if not mutex(self.variables, var)]

        def assign_prob(self, event, p):
            if self.variables == event:
                self.probability = p
            elif self.children:
                for child in self.children:
                    child.assign_prob(event, p)

        def get_prob(self, event):
            if self.variables == event:
                return self.probability
            else:
                return max([child.get_prob(event) for child in self.children])
    
    def empty_set(event):
        a = set(event)
        b = set(map(lambda x: x.replace('!',''), event))

        if len(a) != len(b):
            return True
        else:
            return False

    def num_variables(event):
        return len(set(event.split(' & ')).intersection(set(variables))) - 1

    def complement(event):
        objects = event.split(' & ')
        for obj in objects:
            pass

    prob_tree = probability_tree()

    given_probabilities = [[x.split(': ')[0].split(' & '), x.split(': ')[1]] for x in inputs[1:-1]]
    
    for given_event in given_probabilities:
        prob_tree.assign_prob(given_event[0], given_event[1])

    print(prob_tree.variables)
    print(prob_tree.get_prob())
    event = inputs[-1]

    


if __name__ == "__main__":
    input_1 = '''3 B1 B2
!B1 & B2: 0.01
!B1 & !B2: 0.85
B2: 0.12
B1 & !B2'''
    calculate_probability(input_1)