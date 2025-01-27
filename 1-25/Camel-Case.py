def process_data(input_str):
    lines = input_str.strip().split('\n')
    
    for line in lines:
        operation, type_, words = line.split(';')
        
        if operation == 'S':
            print(split_camel_case(words))
        else:
            print(combine_camel_case(type_, words))

def split_camel_case(words):
    words = words.replace('()', '')
    result = words[0].lower()
    
    for i in range(1, len(words)):
        if words[i].isupper():
            result += ' ' + words[i].lower()
        else:
            result += words[i]
            
    return result

def combine_camel_case(type_, words):
    word_list = words.strip().split(' ')  
    
    if type_ == 'C':
        result = ''.join(word.capitalize() for word in word_list)
    else:
        result = word_list[0].lower() + ''.join(word.capitalize() for word in word_list[1:])
    
    if type_ == 'M':
        result = result.strip() + '()'  
        
    return result

import sys
input_str = sys.stdin.read()
process_data(input_str)