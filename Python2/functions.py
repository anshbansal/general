import math
def prime_factors(num):
    '''Returns the prime factors of a number'''
    if num < 1:
        return 0
    ans = []

    if num % 2 == 0:
        ans.append(2)
        num /= 2
        while num % 2 == 0:
            num /= 2

    i = 3
    while i <= num:
        if num % i == 0:
            ans.append(i)
            num /= i
            while num % i == 0:
                num /= i

        i += 2

    return ans
###
def zeros_in_fact(num):
    '''Returns the number of zeros at the end of factorial of num'''
    if num < 0:
        return 0
    fives = 0
    while num:
        num /=  5
        fives += num
    return fives
###
def sum_primes(num):
    '''Returns the sum of primes upto num(inclusive)'''
    #REQUIRES primes_list() function
    listt = primes_list(num)
    total = 0
    for i in listt:
        total += i
    return total
###
def reverse_trunc(num, times = 1):
    '''Returns a number by truncating its Most Significant Digits
    By default it truncates one digit'''
    return num % (10 ** (len(str(num)) - times))
###
def decimal_to_other(num,base):
    '''Converts from decimal to other number system'''
    add = num % base
    if num <= 1:
        return str(num)
    else:
        return str(decimal_to_other(num//base,base)) + str(add)
###
def num_of_divisors(num):
    '''Returns the number of divisors of a number(num inclusive)'''
    #REQUIRES MATH MODULE
    if num < 1:
        return 0
    elif num == 1:
        return 1
    
    temp = math.sqrt(num)
    if temp == int(temp): #num => Perfect square
        divisors = 3
        temp = int(temp)
    else:
        temp = int(temp) + 1
        divisors = 2

    for i in xrange(2, temp):
        if num % i:
            pass #When i not divisor of num
        else:
            divisors += 2
    
    return divisors
###
def is_bouncy_num(num):
    lisst1 = [int(i) for i in str(num)]
    lisst2 = sorted(lisst1)
    if (lisst1 == lisst2) or (lisst1 == lisst2[::-1]):
        return False
    else:
        return True
###
def sum_of_proper_divisors(num):
    '''Proper Divisors => Divisors less than num'''
    #REQUIRES MATH MODULE
    if num < 2:
        return 0
    temp = math.sqrt(num)
    if temp  == int(temp):
        total = 1 + int(temp)
    else:
        total = 1

    temp = int(temp)
    for i in xrange(2, temp):
        if num % i:
            pass
        else:
            total += i + (num/i)
    
    return total
