def is_prime(num):
    '''Checks whether a number is prime or not'''
    import math
    
    if num == 2:
        return True
    if num % 2 == 0 or num < 2:
        return False
    
    temp = math.floor(math.sqrt(num)) + 1
    for i in range(3, temp, 2):
        if num % i == 0:
            return False
    return True
