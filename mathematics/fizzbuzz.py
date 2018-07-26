def fizz_buzz(value):
    """
    Input:
        A value
    
    Computation:
        goes over each integer up to the value. So for example n = 3, [1,2,3]
        
    Return:
        if value divisible by 3 prints fizz
        if value divisible by 5 prints buzz
        if value divisible by both, prints fizzbuzz
        else prints value
    """
    
    for val in range(value):
        
        val +=1
        
        if val%3 == 0 and val%5 == 0:
            print('fizzbuzz')
        elif val%3 == 0:
            print('fizz')
        elif val%5 == 0:
            print('buzz')
        else:
            print(val)
