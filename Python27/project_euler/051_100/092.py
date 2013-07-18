#Took 54 seconds
import time
from collections import Counter

def sum_of_squares_of_digits(num):
    ans = 0
    while num > 0:
        ans += (num % 10) ** 2
        num /= 10
    return ans

def p():
    ends = [0] * 10000001
    for i in xrange(1,10000000):
        members = set([i])
        q = members.update
        temp = i
        while not ends[temp] and (temp - 89) and (temp - 1):
            temp = sum_of_squares_of_digits(temp)
            q([temp])
            
        if ends[temp]:
            for i in members:
                ends[i] = ends[temp]
        else:
            for i in members:
                ends[i] = temp

    print Counter(ends)
    
        

t = time.time()
p()
print (time.time() - t)
