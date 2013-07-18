import math

def is_prime(num):
    '''Checks whether a number is prime or not'''
    #REQUIRES MATH MODULE
    if num % 2 == 0 or num < 2:
        return False
    
    temp = int(round(math.sqrt(num))) + 1
    for i in xrange(3,temp,2):
        if num % i == 0:
            return False
    else:
        return True

def p():
    i = 9
    while True:
        if is_prime(i):
            i += 2
            continue
        else:
            temp = 1
            temp2 = i - 2 * temp ** 2
            while temp2 > 0:
                if is_prime(temp2):
                    #print "%5d = %5d + 2*(%5d^2)"%(i, temp2, temp)
                    i += 2
                    break
                else:
                    temp += 1
                    temp2 = i - 2 * temp ** 2
            else:
                print "Found the answer = %d"%(i)
                break
                
p()


        
