## HW 2/3/5

def Two_Element_Sort(list: list) -> list:
    """Consider list to be a list containing two types of elements. 
    Babies with either Brown or Purple hair.
    
    Arguments:
        list: an array of ints corresponding to an enumerated type. 0 for brown, 1 for purple.
    Return:
        the sorted list 0s then 1s
    Note:
        Algorythm does not need list to be 0s and 1s, it will sort any two element list as
        function name implies. least to greatest.
    """    
    # index pointers
    head = 0
    tail = len(list) - 1
    
    # if head points at a brown hair baby, incriment it.
    while head < tail:
        while list[head] == 0 and head < tail:
           head += 1
        
        # head points at purple hair baby or end of list
        # decriment tail until it finds a brown hair baby
        while list[tail] == 1 and head < tail:
           tail -= 1
        
        # either done or ready to swap.
        if head < tail:
            # swap
            temp = list[head]
            list[head] = list[tail]
            list[tail] = temp
            head += 1
            tail -= 1
    
    return list
        
def Three_Element_Sort(list):
    """ Otherwise known as dutch flag algoythm. We need 3 pointers to do a linear in place sort
    Arguments:
        list: an array of three elements to be sorted by value. assumed to contain enum type of 
        0, 1, 2 corresponding to brown purple and black haird babies respectivly
        
    Return:
        The sorted list on three elements from least to greatest"""

    