def list_check(lst):
    """Are all items in lst a list?

        >>> list_check([[1], [2, 3]])
        True

        >>> list_check([[1], "nope"])
        False
    """
    return all([isinstance(idx,list)for idx in lst])

#loop through list check if each arug is instance of said list, if all are compliant return true
#using list comprehension which puts in true or false into new list based on the isinstance result, then calling the function all() on it to return true or false