## HW 2/3/5

def Two_Element_Sort(array: list) -> list:
    """Consider list to be a list containing two types of elements. 
    Babies with either Brown or Purple hair.
    
    Arguments:
        array: an array of ints corresponding to an enumerated type. 0 for brown, 1 for purple.
    Return:
        the sorted list 0s then 1s
    """    
    # index pointers
    head = 0
    tail = len(array) - 1
    
    # if head points at a brown hair baby, incriment it.
    while head < tail:
        while array[head] == 0 and head < tail:
           head += 1
        
        # head points at purple hair baby or end of list
        # decriment tail until it finds a brown hair baby
        while array[tail] == 1 and head < tail:
           tail -= 1
        
        # either done or ready to swap.
        if head < tail:
            # swap
            temp = array[head]
            array[head] = array[tail]
            array[tail] = temp
            head += 1
            tail -= 1
    
    return array
        
def Three_Element_Sort(array: list) -> list:
    """ Otherwise known as dutch flag algoythm. We need 3 pointers to do a linear in place sort
    Arguments:
        array: an array of three elements to be sorted by value. assumed to contain enum type of 
        0, 1, 2 corresponding to brown purple and black haird babies respectivly
        
    Return:
        The sorted list on three elements from least to greatest"""
    # three index pointers
    head = 0
    tail = len(array) - 1
    mid = 0

    # general concept, loop and swap incrimenting carfully to swap only where needed in one pass.
    while mid < len(array) and mid <= tail:
        # mid points at brown hair
        if array[mid] == 0:
            # swap mid and head and incriment both.
            temp = array[head]
            array[head] = array[mid]
            array[mid] = temp
            mid += 1
            head += 1
        elif array[mid] == 2:
            # swap, but only incriment tail, only tail is for sure correct, mid might be anything.
            temp = array[mid]
            array[mid] = array[tail]
            array[tail] = temp
            tail -= 1
        else:
            # mid is pointing at a 1 as desired.
            mid += 1
    return array

if __name__ == "__main__":
    two_way_array1 = [1,0,0,1,0,0,0,0,1,1,1,0,1,0,1,0,0,1,1,0,1,1,1,0]
    two_way_array2 = [1]
    two_way_array3 = [0]
    two_way_array4 = []
    two_way_array5 = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    three_way_array1 = [0,2,1,0,1,2,1,2,1,0,1,2]
    three_way_array2 = [2,1,0,1,0,2,0,1,0]
    three_way_array3 = [2]
    three_way_array4 = [1,2,1,2,2,2,2,2,1,1,1,2,1,2,1,2]

    print(Two_Element_Sort(two_way_array1))
    print(Two_Element_Sort(two_way_array2))
    print(Two_Element_Sort(two_way_array3))
    print(Two_Element_Sort(two_way_array4))
    print(Two_Element_Sort(two_way_array5))
    print(Three_Element_Sort(three_way_array1))
    print(Three_Element_Sort(three_way_array2))
    print(Three_Element_Sort(three_way_array3))
    print(Three_Element_Sort(three_way_array4))
    print(Three_Element_Sort(two_way_array1))
    print(Three_Element_Sort(two_way_array2))
    print(Three_Element_Sort(two_way_array3))
    print(Three_Element_Sort(two_way_array4))
    print(Three_Element_Sort(two_way_array5))

    


