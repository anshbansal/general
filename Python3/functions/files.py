__author__ = 'Aseem'

import os


def get_lines(path, file_name):
    with open(path + os.sep + file_name) as f:
        for line in f:
            yield line.rstrip('\n')