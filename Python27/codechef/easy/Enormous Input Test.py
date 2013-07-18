import sys
from itertools import islice
def p():
    numbers, div = map(int,sys.stdin.readline().split())
    nums = [int(i) for i in islice(sys.stdin,numbers)]
    ans = 0
    for i in nums:
        if i % div == 0:
            ans += 1

    print ans

p()
