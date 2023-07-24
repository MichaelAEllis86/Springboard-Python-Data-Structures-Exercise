def last_element(lst):
    """Return last item in list (None if list is empty.
    
        >>> last_element([1, 2, 3])
        3
        
        >>> last_element([]) is None
        True
    """
    if lst==[]:
        return None
    else:
        return lst[-1]


    # using negative indices to go backwards in a list and use if logic so that if list is empty none is returned