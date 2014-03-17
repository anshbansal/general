import sys
from itertools import islice
def q():
    nums = int(sys.stdin.readline())
    prob = [float(i) for i in islice(sys.stdin,nums)]
    for i in range(nums):
        temp = (1 - 2 * prob[i])
        if temp > 0:
            print "%6.6f"%(10000 + ( prob[i] * 10000 * temp ))
        else:
            print "%6.6f"%(10000 + ((prob[i] - 1)* 10000 * temp))

q()
