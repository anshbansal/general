def factorial(num):
    '''Returns factorial of the number '''
    ans = 1
    i = 1
    while i <= num:
        ans *= i
        i += 1
    return ans

def combinations(n, r):
    '''Combinations'''
    #Requires factorial() function
    ans = factorial(n)
    ans /= factorial(r)
    ans /= factorial(n-r)
    return ans

larger = 0
for n in xrange(1,101):
    for r in xrange(n+1):
        temp = combinations(n,r)
        if temp > 1000000:
            larger += 1

print larger

