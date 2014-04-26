import os


def abs_path_cur():
    cur = os.path.dirname(os.path.abspath(__name__))
    prev = os.path.dirname(cur)
    while cur != prev:
        prev = cur
        cur = os.path.dirname(cur)

    return cur
