def gcd_euclid(value1, value2):
    """
    Find the largest number that value1 and 2 can be divided by and return an integer.
    
    This algorithm uses Euclid's algorithm.
    """
    
    
    if value1 == value2:
        return value1
    
    if value1 > value2:
        value_large = value1
        value_small = value2
    else:
        value_large = value2
        value_small = value1
    
    remainder = 1    
    
    while remainder != 0:
        remainder = value_large%value_small
        value_large = value_small
        value_small = remainder
        
        if remainder == 0:
            return value_large