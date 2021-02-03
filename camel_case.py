def camel_case(sentence):
    """ Convert sentence to camelCase, for example, "Display all books"
     is converted to "displayAllBooks" """
    if sentence == '':
        raise ValueError('Please enter a valid sentance')
    if sentence.isdigit():
        raise ValueError('No numbers please')
    
    title_case = sentence.title() # Uppercase first letter of each word
    upper_camel_cased = title_case.replace(' ', '')# remove spaces 
    # Lowercase first letter, join with rest of string
    # Slices don't produce index out of bounds errors test
    # So this still works on empty strings, strings of length 1
    
    return upper_camel_cased[0:1].lower() + upper_camel_cased[1:] 
 



#main
def main():
    sentence = input('Enter your sentence: ')
    camelcased = camel_case(sentence)
    print(camelcased)


if __name__ == '__main__':
    main()        