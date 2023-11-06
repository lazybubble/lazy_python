import strings 
def alphabet_position(text):
    pass
listed = list(text)
if str == letters:
    for char in listed:
        print(''join.(my_list[char] = index + 1))
else 
    pass

textie = 'Hello beautiful world!'
alphabet_position(textie)


   #  make it into a list, slice it so that it can be easily replaced by the value in the dict
    #    position = 
##Final solution submitted

#1. create dict with alphabet and indexes + 1
#2. convert input into str so they are iterable
#3. iterate the input through a loop that will return values
#4. create loop that returns error message

import string

def alphabet_position(text):
    str_text = str(text)
    
    alphabet = string.ascii_lowercase
    alph_dict = {letters:str(index + 1)} for index, letter in enumerate
    
    text = str_text.lower
    result = [alpha_dict[char] for char in text if char.isalpha()]
    
    if not result:
        return 'There are no alphabetic characters in the input.'
    return ''.join(result)
    
textie = 'hello beautiful world!'
positions = alphabet_position(textie)
print(positions)
