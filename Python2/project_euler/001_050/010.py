import math

def primes_list(num):
    ''' Returns list of prime numbers'''
    ''' erat2() from the file "Generating List of prime numbers" '''
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

def prob_010():
    return sum(primes_list(2000000))
    
if __name__ == "__main__":
    print prob_010()
