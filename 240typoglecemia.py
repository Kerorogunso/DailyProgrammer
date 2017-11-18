import random, re                                                              
                                                                               
def typoglycemia(sentence):                                                    
    # takes text and scrambles every letter apart from the first and last of ea
ch word.                                                                       
                                                                               
    word_list = sentence.split(' ')                                            
    typo_sentence = []                                                         
                                                                               
    for word in word_list:                                                     
            if len(list(word)) <= 2:                                           
                typo_sentence.append(word)                                     
            elif re.match('^[\w-]+$',word) is None:                            
                typo_sentence.append(list(word)[0] + ''.join(sorted(list(word)[
1:-2], key = lambda f : random.random())) + ''.join(list(word)[-2:]))          
            else:                                                              
                typo_sentence.append(list(word)[0] + ''.join(sorted(list(word)[
1:-1], key = lambda f : random.random())) +  list(word)[-1])                   
                                                                               
    return ' '.join(typo_sentence)                                             
                                                                               
print(typoglycemia('''According to a research team at Cambridge University, it do
esn''t matter in what order the letters in a word are, the only important thing
 is that the first and last letter be in the right place. The rest can be a tot
al mess and you can still read it without a problem. This is because the human 
mind does not read every letter by itself, but the word as a whole. Such a cond
ition is appropriately called Typoglycemia.''''))                                 