def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    counter={}
    for num in nums:
        if num not in counter:
            counter[num]=1
        else:
            counter[num]+=1
    filtered=[key for key,value in counter.items() if value==max(counter.values())]
    return filtered[0]

        
#make a counter which is a dict which will contain a number(key) and the value will be (count) or number of times in the nums list. 
# then we need to retrieve the key associated with the highest value in the counter dict, we did this by using a list comprehension iterating over the dict using the d.items()method
#we used a filter at the end of the comprehension that checks if a given value is highest and if so it's associated key is appended to a list. We need to conver that list to a number.
#since the list is only 1 element long since their should be only a single most common value we can retrieve the number by retrieving the only/first element in the list filtered[0]