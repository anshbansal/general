__author__ = 'Aseem'

import math
import series


def rev_num(num):
    if num < 0:
        return -int(str(-num)[::-1])
    else:
        return int(str(num)[::-1])


def is_palindrome(num):
    if isinstance(num, str):
        return num == num[::-1]
    else:
        return num == rev_num(num)


def get_binary(num):
    return int(bin(num)[2:])


def triangle_num(n):
    return series.sum_numbers(n)


def is_triangle_num(n):
    temp = (-1 + math.sqrt(8 * n + 1)) / 2
    if temp == int(temp):
        return True
    return False


def pentagonal_num(n):
    return (n * (3 * n - 1)) // 2


def is_pentagonal_num(n):
    temp = (1 + math.sqrt(1 + 24 * n)) / 6
    if temp == int(temp):
        return True
    return False


def hexagonal_num(n):
    return n * (2 * n - 1)


def is_hexagonal_num(n):
    temp = (1 + math.sqrt(1 + 8 * n)) / 4
    if temp == int(temp):
        return True
    return False


def is_bouncy_num(num):
    lisst1 = [int(i) for i in str(num)]
    lisst2 = sorted(lisst1)
    if (lisst1 == lisst2) or (lisst1 == lisst2[::-1]):
        return False
    return True


def factorial(num):
    ans = 1
    while num > 1:
        ans *= num
        num -= 1
    return ans


def product_digits(str_num):
    product = 1
    for i in str_num:
        product *= int(i)
    return product


def circular_shift(num, shift=1):
    num = str(num)
    length = len(num)
    return int(num[length - shift:] + num[:length - shift])


def num_of_divisors(num):
    """Returns the number of divisors of a number(num inclusive)"""
    if num < 1:
        return 0
    elif num == 1:
        return 1

    temp = math.sqrt(num)
    if temp == int(temp):  #num => Perfect square
        divisors = 3
        temp = int(temp)
    else:
        temp = int(temp) + 1
        divisors = 2

    for i in range(2, temp):
        if num % i:
            pass  #When i not divisor of num
        else:
            divisors += 2

    return divisors