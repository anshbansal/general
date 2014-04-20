__author__ = 'Aseem'


def combinations(n, r):
    """Returns Combinations"""
    r = r if n - r > r else n - r
    ans = 1
    for i in range(1, r + 1):
        ans *= n + 1 - i
        ans //= i
    return ans