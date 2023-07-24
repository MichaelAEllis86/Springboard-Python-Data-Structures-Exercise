def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    #solution 2
    lower_cased=phrase.lower()
    counter={}
    vowels="aeiou"
    for character in lower_cased:
        if character in vowels:
           counter[character]=counter.get(character,1)+1
    return counter

