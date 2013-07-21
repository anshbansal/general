import math
from itertools import permutations

def is_prime(num):
    '''Checks whether a number is prime or not'''
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    
    temp = int(round(math.sqrt(num))) + 1
    for i in range(3,temp,2):
        if not(num % i):
            return False
    return True

def prob_041():
    largest = 0
    for i in range(1,9):
        for j in permutations(range(1,i + 1)):
            temp = 0
            for c in j:
                temp *= 10
                temp += c
            if temp > largest and is_prime(temp):
                largest =  temp
        
    return largest

if __name__ == "__main__":
    print(prob_041())
