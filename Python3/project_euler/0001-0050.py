__author__ = 'Aseem'

import algos
import combinatorics
import files
import lcm
import math
import numbers
import primes
import series
from itertools import count, permutations


RESOURCES = 'Resources'


def prob_001():
    return series.sum_multiples_upto((3, 5), 1000)


def prob_002():
    a, b, limit = 1, 2, 4000000
    total = sum(b for b in series.fibonacci(a, b, limit)
                if b % 2 == 0)
    return total


def prob_003():
    return primes.largest_prime_factor(600851475143)


def prob_004():
    largest = 0
    for i in range(100, 1000):
        for j in range(i + 1, 1000):
            num = i * j
            if num > largest and numbers.is_palindrome(num):
                largest = num
    return largest


def prob_005():
    return lcm.lcm_of_range(1, 21)


def prob_006():
    return series.sum_numbers(100) ** 2 - series.sum_squares(100)


def prob_007():
    return primes.nth_prime(10001)


def prob_008():
    number = ''
    for line in files.get_lines(RESOURCES, '008.txt'):
        number += line

    largest = 0
    consecutive = 5
    for i in range(len(number) - consecutive):
        product = numbers.product_digits(number[i:i+consecutive])
        if product > largest:
            largest = product
    return largest


def prob_009():
    for c in range(1, 997):
        c_square = c * c
        for b in range(1, c):
            a = 1000 - b - c
            if a * a + b * b == c_square and b > a > 0:
                return a * b * c


def prob_010():
    #TODO May be Optimized - Level 1 of 3
    return sum(primes.primes_list(2000000))


def prob_013():
    total = sum(int(line)
                for line in files.get_lines(RESOURCES, '013.txt'))
    return str(total)[:10]


def prob_015():
    return combinatorics.combinations(40, 20)


def prob_016():
    num = str(2 ** 1000)
    return sum(int(i) for i in num)


def prob_018():
    #TODO Refactor
    matrix = [[int(i) for i in line.split(' ')]
              for line in files.get_lines(RESOURCES, "018.txt")]
    for row_num in range(1, len(matrix)):
        pre = matrix[row_num - 1]
        cur = matrix[row_num]

        for el_num in range(len(cur)):
            total = cur[el_num]
            if el_num == 0:
                total += pre[el_num]
            elif el_num == len(cur) - 1:
                total += pre[el_num - 1]
            else:
                total += pre[el_num - 1] if pre[el_num - 1] > pre[el_num] \
                    else pre[el_num]

            matrix[row_num][el_num] = total
    return max(matrix[len(matrix) - 1])


def prob_019():
    total = 0
    days = 1 + 365
    #1 for monday
    #Added 365 because 1900 isn't a leap year
    for num_days in algos.get_days(1901, 2001):
        days += num_days[1]
        days %= 7
        if days == 0:
            total += 1
    return total


def prob_020():
    return sum(int(i) for i in str(math.factorial(100)))


def prob_022():
    for line in files.get_lines(RESOURCES, '022.txt'):
        names = line.split(',')
        names.sort()

    scores = 0
    for i in range(len(names)):
        score = 0
        for c in names[i][1:-1]:
            score += ord(c) - ord('A') + 1
        scores += (score * (i + 1))
    return scores


def prob_025():
    for b, i in zip(series.fibonacci_inf(1, 1), count(2)):
        if len(str(b)) > 999:
            return i


def prob_029():
    return len({pow(a, b)
                for a in range(2, 101)
                for b in range(2, 101)}
               )


def prob_040():
    s = ''
    for i in count(1):
        s += str(i)
        if len(s) >= 1000000:
            break

    total = 1
    for i in range(7):
        total *= int(s[10 ** i - 1])

    return total


def prob_041():
    largest = 0
    for i in range(1, 9):
        for j in permutations(range(1, i + 1)):
            temp = 0
            for c in j:
                temp *= 10
                temp += c
            if temp > largest and primes.is_prime(temp):
                largest = temp

    return largest


def prob_042():
    for line in files.get_lines(RESOURCES, "042.txt"):
        words = line.split(",")

    triangles = 0
    for word in words:
        value = sum((ord(c) - ord('A') + 1)
                    for c in word[1:-1])
        if numbers.is_triangle_num(value):
            triangles += 1

    return triangles


def prob_045():
    for i in count(286):
        tri_num = numbers.triangle_num(i)

        if numbers.is_pentagonal_num(tri_num) and numbers.is_hexagonal_num(tri_num):
            return tri_num


def prob_046():
    #TODO Refactor
    for i in count(9, 2):
        if primes.is_prime(i):
            continue
        for j in count(1):
            temp = i - 2 * j ** 2
            if temp < 0:
                return i
            if primes.is_prime(temp):
                break


def prob_047():
    #TODO May be Optimized - Level 1 of 3
    nums = 0
    for i in count(1):
        if primes.num_distinct_prime_factors(i) == 4:
            nums += 1
            if nums == 4:
                return i - 3
        else:
            nums = 0


def prob_048():
    return str(sum(i ** i for i in range(1, 1001)))[-10:]


if __name__ == "__main__":
    import sys

    RULER = "====="
    LIST_FUNC = [i for i in dir(sys.modules[__name__])
                 if i.startswith('prob_') is True]
    for fname in LIST_FUNC:
        print(fname + RULER, end="")
        print(locals()[fname]())