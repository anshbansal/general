import math

###
def sum_of_series(num):
    ''' This is the sum of n consecutive natural numbers'''
    return (  num * (num + 1)  )/2
###
def sum_of_squares(num):
    '''This is the sum of squares of n consecutive natural numbers '''
    return (  num * (num + 1) * ((2 * num) + 1)  )/6
###
def sum_of_cubes(num):
    '''This is the sum of cubes of n consecutive natural numbers'''
    return (sum_of_series(num) ** 2)
###
def fibonnaci(a, b, n):
    '''prints fibonnaci series upto n elements'''
    print a, b,
    for i in xrange(2, n + 1):
        a,b = b, a+b
        print b,      
###
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
def largest_prime_factor (num):
    '''returns the largest prime factor of a number'''
    if num < 1:
        return 0
    ans = 0

    if num % 2 == 0:
        ans = 2
        num /= 2
        while num % 2 == 0:
            num /= 2

    i = 3
    while i <= num:
        if num % i == 0:
            ans = i
            num /= i
            while num % i == 0:
                num /= i

        i += 2

    return ans
###
def reverse_num(num):
    '''returns the reverse of an integer '''
    if num < 0:
        return  - int(str(-num)[::-1])
    else:
        return  int(str(num)[::-1])
###
def is_palindrome(num):
    '''checks whether a number is palindrome or not'''
    if str(num) != str(num)[::-1]:
        return False
    else:
        return True
###
def sum_of_digits(num):
    '''Returns the sum of digits of a number '''
    total = 0
    for i in str(num):
        total += int(i)
    return total
###
def factorial(num):
    '''Returns factorial of the number '''
    ans = 1
    i = 1
    while i <= num:
        ans *= i
        i += 1
    return ans
###
def length_of_num(num):
    '''Returns the length of the number '''
    return len(str(num))
###
def circular_shift(num, shift):
    '''Returns a number circularly shifted '''
    num = str(num)
    length = len(num)
    shift %= length
    return int(num[length - shift:] + num [:length - shift])
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
def gcd(num1, num2):
    '''Finding GCD of a number '''
    '''IMPLEMENTS Euclid's algorithm for finding GCD'''
    if num1 == 0 or num2 == 0:
        return 0

    if num1 >= num2:
        a = num1
        b = num2
    else:
        a = num2
        b = num1

    while b != 0:
        c = a % b
        a,b = b,c
    else:
        return a
###
def primes_list(num):
    ''' Returns list of prime numbers'''
    ''' erat2() from the file "Generating List of prime numbers" '''
    #REQUIRES MATH MODULE
    if num < 2:
        return []

    isprime = [num for num in xrange(3,num + 1,2)]
    #temp2's expression placed in xrange function => performance-loss
    temp2 = int(math.sqrt(num)) + 1
    for i in xrange(3, temp2 ,2):
        if isprime[(i-3)/2]:
            j = 3
            temp = j * i
            while temp <= num:
                isprime[(temp-3)/2] = 0
                j += 2
                temp = j * i
    
    return [2] + filter(lambda x: x, isprime)
###
def is_prime(num):
    '''Checks whether a number is prime or not'''
    #REQUIRES MATH MODULE
    if num == 2:
        return True
    elif num % 2 == 0 or num < 2:
        return False
    
    temp = int(round(math.sqrt(num))) + 1
    for i in xrange(3,temp,2):
        if num % i == 0:
            return False
    else:
        return True
###
def nth_prime(n):
    #REQUIRES primes_list() function
    x = n
    fun = primes_list(x)
    while len(fun) < n:
        x *= 2
        fun = primes_list(x)
    return fun[n - 1]
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
def pentagonal_num(n):
    return (n * (3 * n - 1))/2
###
def triangle_num(n):
    return (n * (n + 1))/2
###
def hexagonal_num(n):
    return (n *(2*n - 1))
###
def is_pentagonal_num(n):
    #REQUIRES MATH MODULE
    temp = (1 + math.sqrt(1 + 24 * n))//6
    if temp == int(temp):
        return True
    else:
        return False
###
def is_triangle_num(n):
    #REQUIRES MATH MODULE
    temp = (-1 + math.sqrt(8 * n + 1))//2
    if temp == int(temp):
        return True
    else:
        return False
###
def is_hexagonal_num(n):
    #REQUIRES MATH MODULE
    temp = (1 + math.sqrt(1 + 8 * n))//4
    if temp == int(temp):
        return True
    else:
        return False
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
