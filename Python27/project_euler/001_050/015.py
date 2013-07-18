from math import factorial

def combinations(n, r):
    '''Combinations'''
    ans = factorial(n)
    ans /= factorial(r)
    ans /= factorial(n-r)
    return ans

print combinations(40, 20)
