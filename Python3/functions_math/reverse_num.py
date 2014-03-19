__author__ = 'Aseem'


def rev_num(num):
    if num < 0:
        return -int(str(-num)[::-1])
    else:
        return int(str(num)[::-1])
