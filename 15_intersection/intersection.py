def intersection(l1, l2):
    """Return intersection of two lists as a new list::
    
        >>> intersection([1, 2, 3], [2, 3, 4])
        [2, 3]
        
        >>> intersection([1, 2, 3], [1, 2, 3, 4])
        [1, 2, 3]
        
        >>> intersection([1, 2, 3], [3, 4])
        [3]
        
        >>> intersection([1, 2, 3], [4, 5, 6])
        []
    """
    s1=set(l1)
    s2=set(l2)
    intersection_set=s1 & s2
    intersection_list=list(intersection_set)
    return intersection_list

# Alternatively, using built-in set math:
    # return list(set(l1) & set(l2))


    #make these things into sets and then intersect set method