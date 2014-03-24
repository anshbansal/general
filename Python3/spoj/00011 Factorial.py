import sys
from itertools import islice
def zeros_in_fact(num):
    '''Returns the number of zeros at the end of factorial of num'''
    fives = 0
    temp = 5
    while temp <= num:
        fives += num // temp
        temp *= 5
    return fives

def p():
    times = int(next(sys.stdin))
    num = [int(i) for i in islice(sys.stdin,times)]
    for i in range(times):
        print(zeros_in_fact(num[i]))

p()
