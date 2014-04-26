__author__ = 'Aseem'


def iterable_to_int(iter_able):
    ans = 0
    for n in iter_able:
        ans *= 10
        ans += int(n)
    return ans