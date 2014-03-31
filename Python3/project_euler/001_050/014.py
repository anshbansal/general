__author__ = 'Aseem'

import time
import series


def prob_014():
    #TODO Optimize - 68 sec
    #Maintaining a dictionary should be the best way
    longest = 1
    longest_num = 1
    for i in range(1, 1000000):
        current = sum(1 for _ in series.collatz(i))
        if current > longest:
            longest = current
            longest_num = i
    print(longest_num, "produces sequence of length = ", longest)


s = time.time()
prob_014()
print(time.time() - s)
