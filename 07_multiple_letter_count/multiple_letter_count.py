def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    counter={}
    for letter in phrase:
       counter[letter]=counter.get(letter,0)+1
    return counter

# iterate over phrase which is a string and then use dict constructor to make a dict using the results of string.count method?