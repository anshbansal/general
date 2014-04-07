__author__ = 'Aseem'

import combinatorics
import common
import files
import math
import numbers_ab
from itertools import count, product


RESOURCES = 'Resources'


def prob_052():
    for num in count(1):
        for j in range(2, 7):
            if set(str(j * num)) != set(str(num)):
                break
        else:
            return num


def prob_053():
    return sum(combinatorics.combinations(n, r) > 1000000
               for n in range(1, 101)
               for r in range(n + 1))


def prob_055():
    total = 0
    for num in range(1, 10000):
        for _ in range(1, 50):
            num += numbers_ab.rev_num(num)
            if numbers_ab.is_palindrome(num):
                break
        else:
            total += 1
    return total


def prob_056():
    sum_t = 0
    for a, b in product(range(1, 100), repeat=2):
        cur = sum(int(i) for i in str(a ** b))
        if cur > sum_t:
            sum_t = cur
    return sum_t


def prob_067():
    return common.max_path_sum_tri_file(RESOURCES, "067.txt")


def prob_081():
    #TODO Refactor Maybe
    """"To understand how this works just make a (4,4) matrix"""
    size_matrix = 80
    mat = files.read_int_from_lines(RESOURCES, "081.txt", split_option=',')

    for i in range(1, size_matrix):
        for j in range(i + 1):
            if j == 0:
                mat[i][j] += mat[i - 1][j]
                mat[j][i] += mat[j][i - 1]
            else:
                mat[i][j] += min(mat[i][j - 1], mat[i - 1][j])
                if i != j:
                    mat[j][i] += min(mat[j - 1][i], mat[j][i - 1])

    return mat[size_matrix - 1][size_matrix - 1]


def prob_097():
    return (28433 * pow(2, 7830457, 10 ** 10)) % (10 ** 10) + 1


def prob_099():
    largest = 0
    for i, line in zip(count(1), files.get_lines(RESOURCES, "099.txt", split_option=',')):
        a, b = map(int, line)
        current = b * math.log(a)
        if current > largest:
            largest = current
            line_largest = i

    return line_largest


if __name__ == "__main__":
    import sys
    import time

    RULER = "====="
    LIST_FUNC = [i for i in dir(sys.modules[__name__])
                 if i.startswith('prob_') is True]
    for fname in LIST_FUNC:
        timm_t = time.time()
        print(RULER + RULER + fname + RULER + RULER + str(locals()[fname]()))
        temp_time = time.time() - timm_t
        if temp_time > 0.5:
            print("TIME " + RULER +  str(temp_time))