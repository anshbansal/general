from itertools import count
import primes


def prob_058():
    num_primes = 0
    non_primes = 1
    for n in count(3, 2):
        temp = n * n
        temp2 = n - 1
        for num in [temp - temp2, temp - 2*temp2,
                    temp - 3*temp2]:
            if primes.is_prime(num):
                num_primes += 1
            else:
                non_primes += 1

        non_primes += 1
        if num_primes / (num_primes + non_primes) < 0.1:
            return n

if __name__ == "__main__":
    import time
    t = time.time()
    print(prob_058())
    print(time.time() - t)
