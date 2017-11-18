def jfork(x,y,*args):                                                          
    my_functions = list(args)                                                  
                                                                               
    if len(my_functions) == 3:                                                 
        # 3 functions left so J fork with middle function                      
        return my_functions[1](my_functions[0](y,x), my_functions[2](y,x))     
    elif len(my_functions)%2 == 1:                                             
        # More than 3 functions so f_1(f_0, jfork(...))                        
        return my_functions[1](my_functions[0](y, x), jfork(x,y,*my_functions[2:]))                                                                           
                                                                               
                                                                               
def sum(y, x=None):                                                            
    return x + y if x else y                                                   
                                                                               
def divide(y, x=None):                                                         
    return y/x if x else y                                                     
                                                                               
def count(y, x=None):                                                          
    return len([y] + [x] if x else y)                                          
                                                                               
print(jfork(2.,4.,sum,sum,sum,sum,divide,sum,sum))                             
