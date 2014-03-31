__author__ = 'Aseem'

import common
import files
import math
from itertools import count


RESOURCES = 'Resources'


def prob_067():
    return common.max_path_sum_tri_file(RESOURCES, "067.txt")


def prob_081():
    #TODO Refactor Maybe
    """"To understand how this works just make a (4,4) matrix"""
    size_matrix = 80
    mat = [[int(i) for i in line] for line in files.get_lines(RESOURCES, "081.txt", ',')]

    for i in range(1, size_matrix):
        for j in range(i + 1):
            if j == 0:
                mat[i][j] += mat[i - 1][j]
                mat[j][i] += mat[j][i - 1]
            else:
                mat[i][j] += mat[i][j - 1] if mat[i - 1][j] > mat[i][j - 1] \
                    else mat[i - 1][j]

                if i != j:
                    mat[j][i] += mat[j - 1][i] if mat[j][i - 1] > mat[j - 1][i] \
                        else mat[j][i - 1]

    return mat[size_matrix - 1][size_matrix - 1]


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
        print(RULER + RULER + fname + RULER + RULER)
        print(locals()[fname]())
        print("TIME " + RULER +  str(time.time() - timm_t))