def sum_of_digits(num):
    '''Returns the sum of digits of a number '''
    num = str(num)
    total = 0
    for i in num:
        total += int(i)
    return total

def factorial(num):
    ans = 1
    while num > 1:
        ans *= num
        num -= 1
    return ans

#MAIN STARTS AFTER THIS
print sum_of_digits(factorial(100))
