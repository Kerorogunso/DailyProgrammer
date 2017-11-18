from math import sqrt                                                        
                                                                             
def deficient_abundant(n):                                                   
    # sum divisors up to sqrt(n) + 1                                         
    sigma_n = sum([x + n/x for x in range(2,int(sqrt(n)+1)) if n%x == 0]) + 1
 add 1 for the division by 1                                                 
                                                                             
    # check if proper divisors above or below n                              
    if sigma_n > n:                                                          
        return '%d abundant by %d' % (n, sigma_n - n)                        
    elif sigma_n < n:                                                        
        return '%d deficient' % (n)                                          
    else:                                                                    
        return '%d neither' % (n)                                            
                                                                             
print(deficient_abundant(111))                                               
print(deficient_abundant(112))                                               
print(deficient_abundant(220))                                               
print(deficient_abundant(69))                                                
print(deficient_abundant(134))                                               
print(deficient_abundant(85))                                                
print(deficient_abundant(21))                                                
print(deficient_abundant(18))                                                
print(deficient_abundant(9))                                                 