def chop(lst):

    """Removes the first and last elements of a list in-place.
    
    Parameters:
    lst (list): The list to modify.
    
    Returns:
    None"""

    if len(lst)>1:
        del lst[0]  # remove first element
        del lst[-1] # remove last elemnt
      #the function retuns none by default as no return statement is provided


def middle(lst):
    
    """Returns a new list that contains all but the first and last elements of the original list.
    
    Parameters:
    lst (list): The original list.
    
    Returns:
    list: A new list with the first and last elements of the original list removed."""

    return lst[1:-1]


original_list = [1,2,3,4,5]
chop_list = original_list.copy()
middle_list = middle(original_list)

chop(chop_list)

print(chop_list, middle_list)