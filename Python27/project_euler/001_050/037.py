import math

def is_prime(num):
    '''Checks whether a number is prime or not'''
    if num == 2:
        return True
    elif num % 2 == 0 or num < 2:
        return False
    
    temp = int(round(math.sqrt(num))) + 1
    
    for i in xrange(3,temp,2):
        if num % i == 0:
            return False
    else:
        return True
   
def reverse_trunc(num, times = 1):
    '''Returns a number by truncating its Most Significant Digits

    By default it truncates one digit'''
    return num % (10 ** (len(str(num)) - times))
    
i = 7
total = 0
count = 0
while count < 11:
    i += 2
    if is_prime(i):
        checked = True
    else:
        continue

    temp = i
    while temp > 0:
        if not is_prime(temp):
            checked = False
            break
        temp /= 10

    if not checked:
        continue
    
    temp = i
    while temp > 0:
        if not is_prime(temp):
            checked = False
            break
        temp = reverse_trunc(temp)

    if checked:
        count += 1
        total += i

print total
