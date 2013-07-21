import itertools
import math
def prob_003(num):
    '''Returns the largest prime factor of an odd number'''
    ans = 0
    sqrt_num = math.floor(math.sqrt(num))
    for i in itertools.chain([2], range(3, sqrt_num, 2)):
        while not (num % i):
            ans = i
            num //= i
    return ans if ans else num

if __name__ == "__main__":
    print(prob_003(600851475143))
