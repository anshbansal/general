#Took 11.25 seconds
def sum_total(i = 0, j = 0, k = 0, l = 0,
              m = 0, n = 0, o = 0):
    return (i*100 + j*50 + k*20 + l*10 + m*5 + n*2 + o)

def p():
    ways = 1
    for i in xrange(3): #For 100
        for j in xrange(5): #for 50
            if sum_total(i,j) > 200:
                break
            for k in xrange(11): #For 20
                if sum_total(i,j,k) > 200:
                    break
                for l in xrange(21): #For 10
                    if sum_total(i,j,k,l) > 200:
                        break
                    for m in xrange(41): #For 5
                        if sum_total(i,j,k,l,m) > 200:
                            break
                        for n in xrange(101): #for 2
                            if sum_total(i,j,k,l,m,n) > 200:
                                break
                            for o in xrange(201): #For 1
                                if sum_total(i,j,k,l,m,n,o) == 200:
                                    ways += 1


    print ways

import time
s = time.time()
p()
print (time.time() - s)
                    
