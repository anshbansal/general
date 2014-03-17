import time, math

def tri_num(num):
    return (  num * (num + 1)  )/2

def num_of_divisors(num):
    '''Returns the number of divisors of a number(num inclusive)'''
    #REQUIRES MATH MODULE
    if num < 1:
        return 0
    elif num == 1:
        return 1
    
    temp = math.sqrt(num)
    if temp == int(temp): #num => Perfect square
        divisors = 3
        temp = int(temp)
    else:
        temp = int(temp) + 1
        divisors = 2

    for i in xrange(2, temp):
        if num % i:
            pass #When i not divisor of num
        else:
            divisors += 2
    
    return divisors
#MAIN STARTS AFTER THIS

def p():
    nums = [tri_num(i) for i in xrange(10000)]
    triangle_num = 1
    num = 1
    max_div = 1
    
    while max_div < 500:
        div =  num_of_divisors(triangle_num)
        if div > max_div:
            max_div = div
            max_tri = triangle_num
        num += 1
        triangle_num = tri_num(num)
        
    else:
        print "\nreached %10d max_div = %5d triangle_num = %20d" %(num,max_div, max_tri)


s = time.time()
p()
print (time.time() - s)

