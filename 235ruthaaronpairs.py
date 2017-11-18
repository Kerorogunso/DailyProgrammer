def ruth_aaron(a, b):                                                          
    # Checks if the sum of prime factors are equal                             
    def prime_factors(n):                                                      
        # Gets list of all prime factors                                       
        factors = []                                                           
        for i in range(2, n+1):                                                
            if n%i == 0 and all([i%y != 0 for y in factors]):                  
                factors.append(i)                                              
        return factors                                                         
                                                                               
    return 'VALID' if sum(prime_factors(a)) == sum(prime_factors(b)) else 'NOT VALID'                                                                         
                                                                               
print(ruth_aaron(5,6))                                                         
print(ruth_aaron(2107,2108))                                                   
print(ruth_aaron(492,493))                                                     
print(ruth_aaron(128,129))                                                     
                                                                               
                                                                                
