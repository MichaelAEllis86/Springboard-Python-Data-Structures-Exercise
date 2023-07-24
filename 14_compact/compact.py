def compact(lst):
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """
    true_list=[idx for idx in lst if bool(idx)==True]
    return true_list
    #checking each element in a list for truthy or falsy values, and put into a new list if the value is truthy! Will use the bool() method to check! Using an list comprehension that will append to new list if truth check is met!
    