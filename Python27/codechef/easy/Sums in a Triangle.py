import sys
from itertools import islice

def p(): 
    cases = int(next(sys.stdin))
    for case in xrange(cases):
        height = int(next(sys.stdin))
        triangle = [map(int, i.split()) for i in islice(sys.stdin, height)]

        prev_row = triangle[0]
        for i in xrange(1, height):
            cur_row = triangle[i]

            cur_row[0] += prev_row[0]
            cur_row[len(cur_row) - 1] += prev_row[len(prev_row) - 1]

            for j in xrange(1, len(cur_row) - 1):
                if(prev_row[j - 1] > prev_row[j]):
                    cur_row[j] += prev_row[j - 1]
                else:
                    cur_row[j] += prev_row[j]

            prev_row = cur_row

        print max(prev_row)

p()
