#To do this I derived the formula for sum of corners in n x n spiral
#It's easy to find the pattern if you consider the outer ring only in spiral

def sum_of_outer_ring(n):
    if n == 1:
        return 1
    else:
        return 4*(n*n) - 6 * (n - 1)

def p(num):
    return sum_of_outer_ring(num)

total = 0
for i in xrange(1,1002,2):
    total += p(i)

print total
