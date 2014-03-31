__author__ = 'Aseem'

import os


def get_lines(path, file_name, split_option=None):
    with open(path + os.sep + file_name) as f:
        for line in f:
            yield _process_line(line, split_option)


def get_line(path, file_name, split_option=None):
    with open(path + os.sep + file_name) as f:
        return _process_line(f.readline(), split_option)


def _process_line(line, split_option):
    if split_option is None:
        return line.rstrip('\n')
    else:
        return line.rstrip('\n').split(split_option)


def read_int_from_lines(path, file_name, split_option=None):
    return [[int(i) for i in line]
            for line in get_lines(path, file_name, split_option=split_option)]