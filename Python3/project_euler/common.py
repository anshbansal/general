__author__ = 'Aseem'

import files


def max_path_sum_triangle(triangle):
    #TODO Refactor
    for row_num in range(1, len(triangle)):
        pre = triangle[row_num - 1]
        cur = triangle[row_num]

        for el_num in range(len(cur)):
            total = cur[el_num]
            if el_num == 0:
                total += pre[el_num]
            elif el_num == len(cur) - 1:
                total += pre[el_num - 1]
            else:
                total += max(pre[el_num - 1], pre[el_num])

            triangle[row_num][el_num] = total
    return max(triangle[- 1])


def max_path_sum_tri_file(path, file_name):
    triangle = [[int(i) for i in line]
                for line in files.get_lines(path, file_name, split_option=' ')]
    return max_path_sum_triangle(triangle)