import random                                                        
                                                                     
def tetremino(n):                                                    
    # returns a sequence of tetris blocks using the random bag system
    tetris_pieces = ['O','I','S','Z','L','J','T']                    
    current_bag = list(tetris_pieces)                                
    tetris_sequence = ''                                             
    for i in range(n):                                               
        random.shuffle(current_bag)                                  
        tetris_sequence += current_bag.pop(0)                        
        if current_bag == []:                                        
            current_bag = list(tetris_pieces)                        
                                                                     
    print(tetris_sequence)                                           
                                                                     
print(tetremino(50))                                                 
                                                                     