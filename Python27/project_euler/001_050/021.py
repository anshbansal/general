import time, math

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

def p():
    sums = []
    d = sum_of_proper_divisors
    for i in xrange(10000):
        sums.append(d(i))

    total = 0
    for i in xrange(10000):
        b = sums[i]

        if b >= 10000 or b == i:
            continue
        elif sums[b] == i:
            total += i

    print total

s = time.time()
p()
print (time.time() - s)
