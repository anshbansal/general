import math, time
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
    listt = []
    total = 0
    for i in xrange(1, 28124):
        if i < sum_of_proper_divisors(i):
            listt.append(1)
        else:
            listt.append(0)
            
        for j in xrange(1,i):
            if listt[j - 1] and listt[i - j - 1]:
                break
        else:
            total += i
        
    print  total

s = time.time()
p()
print (time.time() - s)
