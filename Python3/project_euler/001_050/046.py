from itertools import count
from primes import is_prime


def prob_046():
    for i in count(9, 2):
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