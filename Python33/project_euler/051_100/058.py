#Taking 7.5 seconds
from itertools import count
import math

def is_prime(num):
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    
    temp = int(round(math.sqrt(num))) + 1
    for i in range(3,temp,2):
        if num % i == 0:
            return False
    return True

def prob_058():
    primes = 0
    non_primes = 1
    for n in count(3, 2):
        temp = n * n
        temp2 = n - 1
        for num in [temp - temp2, temp - 2*temp2,
                    temp - 3*temp2]:
            if is_prime(num):
                primes += 1
            else:
                non_primes += 1

        non_primes += 1
        if primes / (primes + non_primes) < 0.1:
            return n

if __name__ == "__main__":
    import time
    t = time.time()
    print(prob_058())
    print(time.time() - t)
