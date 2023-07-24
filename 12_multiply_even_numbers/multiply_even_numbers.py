def multiply_even_numbers(nums):
    """Multiply the even numbers.
    
        >>> multiply_even_numbers([2, 3, 4, 5, 6])
        48
        
        >>> multiply_even_numbers([3, 4, 5])
        4
        
    If there are no even numbers, return 1.
    
        >>> multiply_even_numbers([1, 3, 5])
        1
    """
    #func accepts list of nums, should loop over list and use modulo %2 and if it is zero then we put into empty list and then loop over new list and multiply
    evens=[]

    for num in nums:
        if num % 2==0:
            evens.append(num)

    counter=1
    for even in evens:
        counter=counter * even
    print(counter)
    return counter

