def find_factors(num):
    """Find factors of num, in increasing order.

    >>> find_factors(10)
    [1, 2, 5, 10]

    >>> find_factors(11)
    [1, 11]

    >>> find_factors(111)
    [1, 3, 37, 111]

    >>> find_factors(321421)
    [1, 293, 1097, 321421]
    """
    nums=[x for x in range(1,num+1)]
    return[y for y in nums if num%y==0]
    
#factor= find all of the whole numbers that argument num is divisible by, and put them into a list!
#logic turn num into a list of numbers ranging from 1 to whatever the "num" parameter is
# using modulo, divide the num parameter by each number below it, if there is no remainder or mod==0 then append that number into a new list of factors and return it