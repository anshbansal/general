from itertools import permutations
from primes import is_prime


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
