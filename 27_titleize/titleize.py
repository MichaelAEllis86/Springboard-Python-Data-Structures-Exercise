def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    phrase_list=phrase.split(" ")
    capitalized_phrase_list=[word.capitalize() for word in phrase_list]
    return " ".join(capitalized_phrase_list)
  
    #logic use split to put the string into a list, iterate over list with s.capitalize method, then turn it back into a string and return it.
    #split to make intial list, list comprehension to transform words in list to capitalize first letter in string
    #use join method to return the list of phrases back to a string with appropriate syntax

      # there's a built-in method for this! DOH! we worked too hard!
        #return phrase.title()
    

