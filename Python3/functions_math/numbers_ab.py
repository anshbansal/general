__author__ = 'Aseem'

from math import sqrt
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
    temp = (-1 + sqrt(8 * n + 1)) / 2
    if temp == int(temp):
        return True
    return False


def pentagonal_num(n):
    return (n * (3 * n - 1)) // 2


def is_pentagonal_num(n):
    temp = (1 + sqrt(1 + 24 * n)) / 6
    if temp == int(temp):
        return True
    return False


def hexagonal_num(n):
    return n * (2 * n - 1)


def is_hexagonal_num(n):
    temp = (1 + sqrt(1 + 8 * n)) / 4
    if temp == int(temp):
        return True
    return False


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