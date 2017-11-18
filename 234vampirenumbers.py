import itertools                                                               
from functools import reduce                                                   
from operator import mul                                                       
                                                                               
def vampire(n):                                                                
    # Determines if the number is a vampire number                             
    string_n = str(n)                                                          
    starting_digits = list(string_n)                                           
    for digits in itertools.permutations(starting_digits):                     
        digit_pairs = [int(digits[i] + digits[i+1]) for i in range(0, len(digits)-1, 2)]                                                                      
                                                                               
        if reduce(mul, digit_pairs, 1) == n:                                   
            return '*'.join(map(str,digit_pairs))                              
                                                                               
def find_vampires(digits, fangs):                                              
    for i in range(10**(digits-1),10**digits - 1):                             
        if i%1e5 == 0:                                                         
            print(i)                                                           
        x = vampire(i)                                                         
        if x:                                                                  
            print(i, ' = ', x)                                                 
                                                                               
                                                                               
find_vampires(4, 2)                                                            
find_vampires(6, 3)                                                             
