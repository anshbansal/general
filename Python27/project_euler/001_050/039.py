import time
def p():
    maximum = 0
    maximum_p = 3
    for p in xrange(3,1001):
        cur = 0
        for a in xrange(1,p-1):
            #This equation can be obtained by solving the two given equations 
            b = int((p * (p - 2 * a))/ (2.0 *(p - a)))
            c = p - a - b
            if c <= 0:
                break
            if a * a + b * b == c * c:
                cur += 1
        if cur > maximum:
            maximum = cur
            maximum_p  = p

    print "Reached ",maximum_p

p()
