def sum_of_digits(num):
    '''Returns the sum of digits of a number '''
    num = str(num)
    total = 0
    for i in num:
        total += int(i)

    return total

x = range(1,100)
summ = 0
for a in x:
    for b in x:
        cur = a ** b
        cur = sum_of_digits(cur)
        if cur > summ:
            summ = cur
print summ
