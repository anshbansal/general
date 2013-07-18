import math

def erat(num):
    '''Returns list of Prime numbers

    Implements Sieve of eratosthenes '''
    isprime = [num for num in xrange(2,num + 1)]
    for i in xrange(2,num + 1):
        if isprime[i-2]:
            j = 2
            temp = j * i
            while temp <= num:
                isprime[temp-2] = 0
                j += 1
                temp = j * i
    
    return filter(lambda x: x, isprime)

def erat2(num):
    '''Returns list of Prime numbers

    Improves erat() function

    Advantage:
    Half memory usage'''
    #REQUIRES MATH MODULE
    if num < 2:
        return []

    isprime = [num for num in xrange(3,num + 1,2)]
    #temp2's expression placed in xrange function => performance-loss
    temp2 = int(math.sqrt(num)) + 1
    for i in xrange(3, temp2 ,2):
        if isprime[(i-3)/2]:
            j = 3
            temp = j * i
            while temp <= num:
                isprime[(temp-3)/2] = 0
                j += 2
                temp = j * i
    
    return [2] + filter(lambda x: x, isprime)

def erat3(num, isprime = [3]):
    '''Returns list of Prime numbers

    Changes erat() function using methods of erat2() function

    Advantage:
    Half memory usage
    Takes 1/10th time if called in the same run for same or lower number
    Improvement in speed if it has been called before

    Disadvantage:
    Has storage between function calls - Takes up a lot of memory space'''
    #REQUIRES MATH MODULE
    if num < 2:
        return []
    
    if num > 2 * len(isprime) + 2:
        def mapping(i):
            return (i -3)/2

        first_new = 2 * len(isprime) + 3
        isprime += [num for num in xrange(first_new ,num + 1, 2)]
        
        temp2 = int(math.sqrt(num)) + 1
        for i in xrange(3,first_new, 2):
            if isprime[mapping(i)]:
                j = first_new//i
                if j == 1:
                    j = 3
                elif j % 2 == 0:
                    j += 1

                temp = j * i
                while temp <= num:
                    isprime[mapping(temp)] = 0
                    j += 2
                    temp = j * i
                    
        for i in xrange(first_new,temp2, 2):
            if isprime[mapping(i)]:
                j = 3
                temp = j * i
                while temp <= num:
                    isprime[mapping(temp)] = 0
                    j += 2
                    temp = j * i
    
    return [2] + filter(lambda x: x, isprime[:(num - 1)//2])
