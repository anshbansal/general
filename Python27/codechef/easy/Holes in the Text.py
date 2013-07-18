import sys
from itertools import islice
def p():
    
    cases = int(sys.stdin.readline())
    strings = [i for i in islice(sys.stdin,cases)]
    
    for string in strings:
        holes = 0
        for i in string:
            if i == 'A' or i == 'D'or i=='O'or i=='P'or i=='Q'or i=='R':
                holes += 1
            elif i == 'B':
                holes += 2
        print holes

p()
