def atbash(word):
    """returns the atbash cipher of the text passed"""
    case = [1 if x.isupper() else 0 for x in word]
    letter_reverses = [chr(219 - ord(str.lower(x))) if ord(str(x.lower())) in range(97,123)
                else x for x in word]
    return "".join([letter_reverses[i] if case[i] == 0 else letter_reverses[i].upper() for i in range(len(word))])

print(atbash('foobar'))
print(atbash('wizard'))
print(atbash('/r/dailyprogrammer'))
print(atbash('gsrh rh zm vcznkov lu gsv zgyzhs xrksvi'))

