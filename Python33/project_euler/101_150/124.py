import itertools
import math

def product_of_prime_factors(num):
    ans = 1
    sqrt_num = math.floor(math.sqrt(num)) + 1
    for i in itertools.chain([2], range(3, sqrt_num, 2)):
        if not(num % i):
            ans *= i
            num //= i
        while not (num % i):
            num //= i
    return ans if num == 1 else ans * num

def prob_124():
    return sorted(
        [(product_of_prime_factors(i), i)
         for i in range(1, 100001)])[9999][1]

if __name__ == "__main__":
    print(prob_124())
