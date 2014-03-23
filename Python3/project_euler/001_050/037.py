from itertools import count
from primes import is_prime


def check1(i):
    while i > 0:
        if not is_prime(i):
            return False
        i //= 10
    return True


def check2(i):
    while i > 0:
        if not is_prime(i):
            return False
        i %= 10 ** (len(str(i)) - 1)
    return True


def prob_037():
    total, nums = 0, 0
    for i in count(9, 2):
        if is_prime(i) and check1(i) and check2(i):
            nums += 1
            total += i
            if nums == 11:
                return total

if __name__ == "__main__":
    print(prob_037())
