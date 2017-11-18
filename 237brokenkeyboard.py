import pandas as pd                                                            
import re                                                                      
                                                                               
def broken_keyboard(keys):                                                     
    worddf = pd.DataFrame(pd.read_csv('/usr/share/dict/words'))                
    keyboard_keys = keys.split('\n')                                           
    keyboard_keys = map(str.strip,keyboard_keys)                               
    worddf.columns = ['word']                                                  
    worddf['word'] = worddf['word'].str.replace("'s",'')                       
                                                                               
    for key in keyboard_keys[1:]:                                              
        possible_words = worddf                                                
        for char in key:                                                       
            possible_words = possible_words[possible_words['word'].str.contains(char)]                                                                        
                                                                               
        print(possible_words.iloc[1].to_string())                              
print(broken_keyboard(                                                         
    '''3                                                                       
    test                                                                       
    dafg                                                                       
    pom                                                                        
    oql'''))                                                                   
                                                                               