#Took 37 seconds
import math, time

def p():
    #num1 = int(math.floor(math.sqrt(10203040506070809)))
    num2 = int(math.floor(math.sqrt(19293949596979899)))
    #print num1, num2, num2 - num1

    for num1 in [101010103, 101010107]:
        for i in xrange(num1, num2 + 1, 10):
            sq = i ** 2
            sq2 = str(sq)
            for j in xrange(7,-1, -1):
                if int(sq2[2 * j]) == j + 1:
                    pass
                else:
                    break
            else:
                print i * 10
                return
    
s = time.time()
p()
print (time.time() - s)
