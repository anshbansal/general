__author__ = 'Aseem'

import files
import sys
import time

RULER = "====="

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
    return max_path_sum_triangle(files.read_int_from_lines(path, file_name, split_option=' '))


def run_all(module_name):
    cur_module = __import__(module_name)
    list_functions = [i for i in dir(sys.modules[module_name]) if i.startswith('prob_') is True]
    list_answers = {i[0]: i[1] for i in files.get_lines('Resources', 'answers.txt', split_option='^')}
    for func_name in list_functions:
        prob_num = func_name.lstrip("prob_0")

        timm_t = time.time()
        ans = str(getattr(cur_module, func_name)())
        temp_time = time.time() - timm_t

        if ans != list_answers[prob_num]:
            print("PROBLEM IN " + prob_num + "  ANSWER = " + ans)
        elif temp_time > 1.0:
            print(RULER + RULER + func_name + RULER + RULER + str(temp_time))