import re, datetime                                                            
                                                                               
def date_converter(messy_string):                                              
    # Takes a messy date and converts it into the correct format               
                                                                               
    messy_string = messy_string.replace('/',' ').replace('-',' ') # replace non
alphanumeric characters                                                        
    numbers = map(int,messy_string.split(' '))                                 
                                                                               
                                                                               
    if re.search('[a-zA-Z]', str(numbers[0])):                                 
        # String found search dictionary                                       
        print("foo")                                                           
    elif len(str(numbers[0])) == 4:                                            
        # Length 4 year                                                        
        try:                                                                   
            return datetime.date(numbers[0],numbers[1],numbers[2]) # YYYY-MM-DD
        except:                                                                
            return datetime.date(numbers[0],numbers[2],numbers[1]) # YYYY-DD-MM
    else:                                                                      
        try:                                                                   
            return datetime.date(numbers[2], numbers[1], numbers[0]) # DD-MM-YYYY                                                                             
        except:                                                                
            return datetime.date(numbers[2], numbers[0], numbers[1]) # MM-DD-YYYY                                                                            
                                                                               
print(date_converter('2015-01-09'))                                            
print(date_converter('1999-13-1'))                                             
print(date_converter('30-12-2016'))                                            
print(date_converter('12/30/2016'))                                            
                                                                               