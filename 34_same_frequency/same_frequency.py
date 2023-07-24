def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    string1=str(num1)
    string2=str(num2)
    counter1={}
    counter2={}
    for idx in string1:
        if idx in counter1:
            counter1[idx]=counter1.get(idx,1)+1
        else: counter1[idx]=counter1.get(idx,1)
    # print (counter1)

    for idx in string2:
        if idx in counter2:
            counter2[idx]=counter2.get(idx,1)+1
        else: counter2[idx]=counter2.get(idx,1)
    # print (counter2)

    if counter1==counter2:
        return True
    else:
        return False
    
# logic: turning each number into a string that can be interated over. We also need a counter for each num the function takes in. In this case, a dict is most appropriate because we need a value
# associated with each number. For each index in the string if a key exists for it already we increment the k/v pair by 1. If it doesnt exist we establish it and set a default value of 1.
# this is done by using the dictionary method get. Repeat for both func parameters than compare the two counters returning true or false. 



    # SpringBoard Solution to this

#     def freq_counter(coll):
#     """Returns frequency counter mapping of coll."""

#     counts = {}

#     for x in coll:
#         counts[x] = counts.get(x, 0) + 1

#     return counts


# def same_frequency(num1, num2):
#     """Do these nums have same frequencies of digits?

#         >>> same_frequency(551122, 221515)
#         True

#         >>> same_frequency(321142, 3212215)
#         False

#         >>> same_frequency(1212, 2211)
#         True
#     """

#     return freq_counter(str(num1)) == freq_counter(str(num2))
