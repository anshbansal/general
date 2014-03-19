from math import sqrt
from itertools import count


def prob_045():
    for i in count(286):
        tri_num = (i * (i + 1))//2

        p = (1 + sqrt(1 + 24 * tri_num))/6
        if int(p) != p:
            continue
        
        h = (1 + sqrt(1 + 8 * tri_num))/4
        if int(h) == h:
            return tri_num

if __name__ == "__main__":
    print(prob_045())
