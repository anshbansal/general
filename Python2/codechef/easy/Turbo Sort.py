import sys
from itertools import islice
def p():
    numbers = int(sys.stdin.readline())
    nums = [int(i) for i in islice(sys.stdin,numbers)]
    nums.sort()
    for i in nums:
        print i,
 
p()
