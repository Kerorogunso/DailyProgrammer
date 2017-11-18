import numpy as np                                                 
def game_of_threes(n):                                             
    while n > 1:                                                   
        print(n, int(0 if n%3 == 0 else np.sign(n%3 - 1.5)))       
        n = int((n + (0 if n%3 == 0 else np.sign(n%3 - 1.5))) // 3)
    print(n)                                                       
game_of_threes(100)                                                
game_of_threes(31337357)                                           
                                                                   