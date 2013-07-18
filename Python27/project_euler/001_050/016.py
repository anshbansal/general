def sum_of_digits(num):
    '''Returns the sum of digits of a number '''
    num = str(num)
    total = 0
    for i in num:
        total += int(i)
    return total

#MAIN STARTS HERE
print sum_of_digits(2 ** 1000)
