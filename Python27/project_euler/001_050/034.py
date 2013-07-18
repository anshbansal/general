#Took 5.5 seconds
from math import factorial

#The limit of 2540161 is chosen becuause it is 7 * 9!
#Numbers higher than this give 7 digit-number which
#cannot be equal to 8 digit numbers

import time

def p():
    facts = [factorial(i) for i in xrange(10)]
    sums = 0
    for i in xrange(10, 2540161):
        sums_of_fact = 0
        temp = i
        while temp > 0:
            sums_of_fact += facts[temp % 10]
            temp = temp / 10

        if sums_of_fact == i:
            sums += i

    print sums

s = time.time()
p()
print (time.time() - s)

