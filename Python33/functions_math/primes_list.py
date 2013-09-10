def primes_list(num):
    ''' Returns list of prime numbers'''
    ''' erat2() from the file "Generating List of prime numbers" '''
    import math
    if num < 2:
        return []

    isprime = [num for num in range(3,num + 1,2)]
    temp2 = int(math.sqrt(num)) + 1
    for i in range(3, temp2 ,2):
        if isprime[(i-3)//2]:
            j = 3
            temp = j * i
            while temp <= num:
                isprime[(temp-3)//2] = 0
                j += 2
                temp = j * i
    
    return [2] + [x for x in isprime if x]
