def funky_plant(x, y):                                                         
    # returns the number of weeks taken to feed x people starting with y magic 
fruit                                                                          
                                                                               
    funky_farm = [0 for _ in range(y)] # list of trees and their yield         
    week = 1                                                                   
                                                                               
    while sum(funky_farm) < x:                                                 
        funky_farm = map(lambda x: x + 1, funky_farm) # increase yield per frui
t by 1                                                                         
        funky_farm = funky_farm + [0 for _ in range(sum(funky_farm))] # add all yield as new trees                                                            
        week +=1                                                               
                                                                               
    return week                                                                
                                                                               
print(funky_plant(15,1))                                                       
print(funky_plant(200,15))                                                     
print(funky_plant(50000,1))                                                    
print(funky_plant(150000,250))                                                 
                                                                               