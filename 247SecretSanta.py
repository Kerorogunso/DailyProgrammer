import random

def secret_santa(participants):
    pairings = [] # Final pairings at the end
    participant_list = [x.split(' ') for x in participants.splitlines()] # Split participants into list of families


    # Random member from largest family remaining
    largest_family = max(participant_list,key=len)
    family_id = [i for i, item in enumerate(participant_list) if item == largest_family][0]
    random.shuffle(participant_list[family_id])
    x = participant_list[family_id].pop()

    # While there are still givers unassigned
    while not all(len(family) == 0 for family in participant_list):   
        ''' Get the sizes of the two largest families 
            to account for ties and uneven family sizes
        '''
        largest_families = sorted(map(len, participant_list),reverse = True)[:1]
        # Get indicies of the largest/second largest families, take the first one
        family_id = [i for i, item in enumerate(participant_list) if i != family_id and len(item) in largest_families][0]
        random.shuffle(participant_list[family_id])
        # Take random person in the family
        y = participant_list[family_id].pop()
        pairings.append((x,y))
        # Recipiant is now the giver
        x = y

    print(pairings)




test_participants = '''Sean
Winnie
Brian Amy
Samir
Joe Bethany
Bruno Anna Matthew Lucas
Gabriel Martha Philip
Andre
Danielle
Leo Cinthia
Paula
Mary Jane
Anderson
Priscilla
Regis Julianna Arthur
Mark Marina
Alex Andrea
'''

secret_santa(test_participants)