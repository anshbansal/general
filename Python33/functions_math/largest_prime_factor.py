def largest_prime_factor(num):
    '''returns the largest prime factor for num > 0'''
    import itertools
    import math
    
    ans = 0
    sqrt_num = int(math.sqrt(num)) + 1
    for i in itertools.chain([2], range(3, sqrt_num, 2)):
        while not (num % i):
            ans = i
            num //= i
    return ans if num == 1 else num
