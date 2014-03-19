__author__ = 'Aseem'

from primes import primes_list


def nth_prime(num):
    #TODO Refactor to get this function in reusable functions
    x = num
    fun = primes_list(x)
    while len(fun) < num:
        x *= 2
        fun = primes_list(x)
    return fun[num - 1]

if __name__ == "__main__":
    print(nth_prime(10001))
