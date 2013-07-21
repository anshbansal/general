import math
from itertools import count

def is_prime(num):
    temp = int(round(math.sqrt(num))) + 1
    for i in range(3,temp,2):
        if num % i == 0:
            return False
    return True

def prob_046():
    for i in count(9,2):
        if is_prime(i):
            continue
        for j in count(1):
            temp = i - 2 * j ** 2
            if temp < 0:
                return i
            if is_prime(temp):
                break

if __name__ == "__main__":
    print(prob_046())


        
