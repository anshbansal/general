__author__ = 'Aseem'

import files


def _accumulate(row, sums):
    if sums is None:
        return row
    return ([row[0] + sums[0]]
            + [row[i] + max(sums[i - 1], sums[i]) for i in range(1, len(row) - 1)]
            + [row[-1] + sums[-1]])


def max_path_sum_triangle(rows):
    sums = None
    for row in rows:
        sums = _accumulate(row, sums)
    return max(sums) if sums else None


def max_path_sum_tri_file(path, file_name):
    rows = [[int(i) for i in line]
            for line in files.get_lines(path, file_name, split_option=' ')]
    return max_path_sum_triangle(rows)