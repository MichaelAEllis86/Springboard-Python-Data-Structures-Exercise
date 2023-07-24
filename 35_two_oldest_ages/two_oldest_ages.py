def two_oldest_ages(ages):
    """Return two distinct oldest ages as tuple (second-oldest, oldest)..

        >>> two_oldest_ages([1, 2, 10, 8])
        (8, 10)

        >>> two_oldest_ages([6, 1, 9, 10, 4])
        (9, 10)

    Even if more than one person has the same oldest age, this should return
    two *distinct* oldest ages:

        >>> two_oldest_ages([1, 5, 5, 2])
        (2, 5)
    """

    # NOTE: don't worry about an optimized runtime here; it's fine if
    # you have a runtime worse than O(n)

    # NOTE: you can sort lists with lst.sort(), which works in place (mutates);
    # you may find it helpful to research the `sorted(iter)` function, which
    # can take *any* type of list-like-thing, and returns a new, sorted list
    # from it.
    sorted_ages=sorted(set(ages))
    sliced_ages=sorted_ages[-1:-3:-1]
    return tuple(sorted(sliced_ages))

    # sorted_sliced_ages=sorted(sliced_ages)
    # return tuple(sorted_sliced_ages)

    #logic: distinct oldest ages are required! thus, we need to first use a set to filter out repeats. Then since a set isn't ordered we need to sort it which via we do via the
    # sorted() function which gives us back a list. Then we can slice the list to return the last two entries which should always be the largest then use tuple constructor and return