import math
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