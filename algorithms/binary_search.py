def binary_search(value_list, target):
    """
    Takes an array of sorted integer values, then performs binary search
    to find if the target value exists in the array
    
    Return:
        Returns index of target in value_list, iff value exists in list.
        Otherwise returns string 'Your Value is not in list'
    """
    
    left = 0
    right = len(value_list)-1
    
    while left <= right:
        
        mid_index = (right + left) // 2
        mid_value = test[mid_index]
        if target == mid_value:
            return mid_index
        
        elif target > mid_value:
            left = mid_index + 1
        
        elif target < mid_value:
            right = mid_index - 1
            
    return 'Your Value is not in the list'
