import string, random                                                          
                                                                               
def make_word(string_pattern):                                                 
    # Returns arbitrary list of vowels and consonants based on specified format
    return ''.join(                                                            
            [random.sample(set(string.ascii_lowercase).difference(set(['a','e',
'i','o','u'])),1)[0] if x.lower() == 'c'                                       
                else random.sample(set(['a','e','i','o','u']),1)[0]            
            for x in list(string_pattern)                                      
            ])                                                                 
                                                                               
                                                                               
                                                                               
print(make_word('ccccvvcvv'))                                                  